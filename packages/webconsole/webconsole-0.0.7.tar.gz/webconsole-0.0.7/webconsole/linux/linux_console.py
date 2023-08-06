import asyncio
from fastapi import FastAPI, WebSocket, APIRouter, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from paramiko import util
from paramiko import SSHClient
from paramiko import AutoAddPolicy


linux_webconsole = APIRouter()

# linux_webconsole = FastAPI()

# # use for @linux_webconsole.get("/"), but it's just for debug, xterm should  user by frontend project like VUE.
# linux_webconsole.mount("/static", StaticFiles(directory="static"), name="static")


html = """
<!DOCTYPE html>
<html lang="en">
<head>
     <link rel="stylesheet" href="static/xterm/dist/xterm.css">
    <meta charset="UTF-8">
    <title>docker web terminal</title>
</head>
<body>
<div id="terminal"></div>
<script src="static/js/jquery-1.12.4.js"></script>
<script src="static/xterm/dist/xterm.js"></script>
<script src="static/xterm/dist/addons/attach/attach.js"></script>
<script>
    let term = new Terminal({cursorBlink: true});
    term.open(document.getElementById('#terminal'));
    term.writeln("welcome to use docker web terminal!");
    let socket = new WebSocket('ws://127.0.0.1:8000/ws/linux?address=127.0.0.1&user=rbadmin_app1');
    term.attach(socket);
    socket.onclose = function () {
        term.writeln("Closed. Thank you for use!");
    };
</script>
</body>
</html>
"""

# let socket = new WebSocket('ws://127.0.0.1:8000/ws/linux?address=127.0.0.1&user=raypick&passwd=raypick');


# ignore command, most are combined commands, need to be improved.
ignore_list = ['\x0c', 'x7f']


@linux_webconsole.get("/")
async def get():
    return HTMLResponse(html)


class LinuxWebConsole():

    def __init__(self, address, user, passwd=None):
        self.address = address
        # Set the terminator we define
        self.EndSymbol = ['$ ', '# ', '> ', '* ']
        self.user = user
        self.passwd = passwd
        self.data = None
        self.ssh = None

    def handleConnected(self):
        print(self.address, 'connected')
        ip = self.address
        port = 22
        user = self.user
        passwd = self.passwd

        # # setting for record log
        # log_file = 'centos_ssh.log'
        # util.log_to_file(log_file)

        # Generate SSH client instance
        self.ssh = SSHClient()
        self.ssh.set_missing_host_key_policy(AutoAddPolicy())
        print('get ssh client')
        if passwd:
            self.ssh.connect(ip, port, user, passwd)
        else:
            self.ssh.connect(ip, port, user, key_filename='private_key')
        print('ssh login successfully')
        self.chan = self.ssh.invoke_shell()
        print('get invoke_shell')
        self.chan.settimeout(1000)
        # # Welcome to Ubuntu 16.04.6 LTS..   just some login information
        # LoginInfo = self.chan.recv(2048)
        # print(LoginInfo)

    def handleClose(self):
        print(self.address, 'closed')

    # receive command and execute it
    def runCommand(self, Command):
        print('exec command:'+Command)
        # Adding '\n' after an instruction indicates a line break
        self.chan.send(Command+'\n')
        Result = ''
        print('waiting for reply')
        while True:
            Temp = str(self.chan.recv(4096), encoding='utf-8')
            Result += Temp
            # Determine if the last two characters are the terminator we defined.
            if Result[-2:] in self.EndSymbol:
                break
        # The first line is the instruction we entered, there is no need to discard it.
        Final = Result.split('\n')[1:]
        # print('start print result')
        print('\n'.join(Final), end='')
        # print('end print result')
        # return Final[:-1]
        return '\n'.join(Final)


@linux_webconsole.websocket("/ws/linux")
async def websocket_endpoint(websocket: WebSocket, address: str,
                             user: str, passwd=None):
    await websocket.accept()
    lbc = LinuxWebConsole(address, user, passwd)
    lbc.handleConnected()
    tmp_message = ''
    loop_flag = True
    handled_flag = False
    while True:
        try:
            # socket forward to website
            result = ''
            while loop_flag:
                temp_res = str(lbc.chan.recv(4096), encoding='utf-8')
                result += temp_res
                # Determine if the last two characters are the terminator we defined.
                if result[-2:] in lbc.EndSymbol:
                    loop_flag = False
                    handled_flag = True
                    linuxStreamStdout = result
                # # The first line is the instruction we entered, there is no need to discard it.
                # linuxStreamStdout = Result.split('\n')[1:]
                # linuxStreamStdout = '\n'.join(linuxStreamStdout)

            if not loop_flag and not handled_flag:
                linuxStreamStdout = lbc.chan.recv(4096)
                if linuxStreamStdout is not None:
                    await websocket.send_text(str(linuxStreamStdout, encoding='utf-8'))
                    handled_flag = True

            if linuxStreamStdout is not None:
                await websocket.send_text(linuxStreamStdout)
            else:
                print("linux daemon socket is close")
                await websocket.close()
            # socket forward to linux
            try:
                message = await asyncio.wait_for(websocket.receive_text(), 1800)  # noqa
                if message != '\r' and message != '\x03' and message != '\x7f':
                    if message not in ignore_list:
                        tmp_message += message
                if message == '\x7f' and len(tmp_message) > 0:
                    if len(tmp_message) == 1:
                        tmp_message = ''
                    else:
                        tmp_message = tmp_message[:-1]
            except asyncio.TimeoutError:
                print('timeout for websocket connect')
                raise WebSocketDisconnect(reason='timeout for websocket connect')  # noqa
            except Exception as e:
                if '1001' in str(e):
                    print("websocket has disconnected.")
                    lbc.chan.close()
                    break
            if message is not None:
                lbc.chan.send(message)
                handled_flag = False
            if message == '\r':
                # \x0c : ctrl+l    \x7f : backspace   \x03 :  ETX
                if tmp_message.strip() == 'exit':  # noqa
                    tmp_message = ''
                    loop_flag = False
                    handled_flag = False
                else:
                    loop_flag = True
                    tmp_message = ''
            if message == '\x03':
                tmp_message = ''
        except Exception as e:
            print("linux daemon socket err: %s" % e)
            await websocket.close()
            lbc.chan.close()
            break

# powered by RayCheung.
import asyncio
import docker
from fastapi import FastAPI, WebSocket, APIRouter, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


docker_webconsole = APIRouter()
# docker_webconsole = FastAPI()
# # use for @linux_webconsole.get("/"), but it's just for debug, xterm should  user by frontend project like VUE.
# docker_webconsole.mount("/static", StaticFiles(directory="static"), name="static")

buffer_size = 4096

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
    let socket = new WebSocket('ws://127.0.0.1:8000/ws/f977748aabad');
    term.attach(socket);
    socket.onclose = function () {
        term.writeln("Closed. Thank you for use!");
    };
</script>
</body>
</html>
"""


@docker_webconsole.get("/")
async def get():
    return HTMLResponse(html)


@docker_webconsole.websocket("/ws/{container_id}")
async def websocket_endpoint(websocket: WebSocket, container_id, docker_address, port):
    await websocket.accept()
    # Connect to Docker engine
    client = docker.APIClient('http://' + docker_address + ':' + port, timeout=5)  # noqa
    # create exec
    execCommand = ["timeout", "10", "bash"]
    execOptions = {"tty": True, "stdin": True}
    exec_create_resp = client.exec_create(
        container_id, execCommand, **execOptions)
    # start exec
    terminalStream = client.exec_start(exec_id=exec_create_resp['Id'], socket=True, tty=True)._sock  # noqa
    # terminalStream.settimeout(10)

    while True:
        try:
            # socket forward to website
            dockerStreamStdout = ''
            res_flag = True
            while res_flag:
                part = str(terminalStream.recv(buffer_size), encoding='utf-8')
                dockerStreamStdout += part
                if len(part) < buffer_size:
                    #  either 0 or end of data
                    res_flag = False
            # dockerStreamStdout = terminalStream.recv(2048)
            if dockerStreamStdout is not None:
                await websocket.send_text(dockerStreamStdout)
            else:
                print("docker daemon socket is close")
                await websocket.close()
            # socket forward to docker
            try:
                message = await asyncio.wait_for(websocket.receive_text(), 1800)  # noqa
            except asyncio.TimeoutError:
                print('timeout for websocket connect')
                raise WebSocketDisconnect(reason='timeout for websocket connect')  # noqa
            except Exception as e:
                if '1001' in str(e):
                    print("websocket has disconnected.")
                    terminalStream.close()
                    break
            if message is not None:
                terminalStream.send(bytes(message, encoding='utf-8'))
        except Exception as e:
            print("docker daemon socket err: %s" % e)
            await websocket.close()
            terminalStream.close()
            break

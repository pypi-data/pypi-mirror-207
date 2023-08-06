from setuptools import setup, find_packages

setup(
    name="webconsole",
    version="0.0.7",
    keywords=["pip", "webconsole", "python", "docker"],
    description="webconsole",
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    author='RayCheung',
    packages=find_packages(),
    # packages=['webconsole'],
    package_data={'': ['static/**', 'templates/*']},
    # install_requires=['websockets', 'six', 'docker', 'uvicorn', 'fastapi'],
    install_requires=[
        'websockets==10.4',
        'docker==5.0.0',
        'setuptools==65.6.3',
        'paramiko==3.1.0'
        ],
    # include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

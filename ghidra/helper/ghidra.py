#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
import subprocess
import os
import re
import docker as dockerlib

# Requirements: flask, docker, python3, ghidra server admin tool
# 1. Install ghidra server
# 2. symbolically link ssh to ~ssh in the ghidra data directory

# Environment variables
# GHIDRA_DATA_DIR: where to store the user database and ssh keys
# GHIDRA_INSTALL_DIR: where to find the ghidra server admin tool
# GHIDRA_WEB_PORT: port to run the web server on
# WG_IP: ip to bind to
# JAVA_HOME: where to find java
# or java in the path
# GIT_DOCKER: if set, will use docker to run git commands

# No idea how to do config shit
GHIDRA_DATA_DIR= os.environ.get('GHIDRA_DATA_DIR', '/home/ghidra/data')
UPLOAD_FOLDER = GHIDRA_DATA_DIR+'/ssh'
USER_DB = GHIDRA_DATA_DIR+'/users.txt'
GHIDRA_INSTALL_DIR= os.environ.get('GHIDRA_INSTALL_DIR', '/home/ghidra/ghidra/data')
GHIDRA_ADMIN_TOOL = GHIDRA_INSTALL_DIR+'/server/svrAdmin'
GHIDRA_STATUS_TOOL = GHIDRA_INSTALL_DIR+'/server/ghidraSrv'
GIT_DOCKER_NAME = os.environ.get("GIT_DOCKER", None)
GIT_DOCKER_ENABLED = True if GIT_DOCKER_NAME is not None else False

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
docker = dockerlib.from_env() if GIT_DOCKER_ENABLED else None

# security...
pat = re.compile(r"^[a-zA-Z]{1,20}$")

@app.route('/add', methods=['POST'])
def add():
    user = request.form["username"].strip()
    if pat.fullmatch(user) is None:
        return "bad user name "+user
    else:
        users = []
        with open(USER_DB, "r") as f:
            users = f.read().splitlines()
        if user not in users:
            subprocess.run([GHIDRA_ADMIN_TOOL, "-add", user])
            with open(USER_DB, "a") as f:
                f.write(user+"\n")
            return "added user "+user
        else:
            return "user exists"

@app.route('/reset', methods=['POST'])
def reset():
    user = request.form["username"]
    if pat.fullmatch(user) is None:
        return "bad user name"
    else:
        users = []
        with open(USER_DB, "r") as f:
            users = f.read().splitlines()
        if user in users:
            subprocess.run([GHIDRA_ADMIN_TOOL, "-reset", user])
            return "reset pw for "+user
        else:
            return "bad user name "+user

@app.route('/key', methods=['POST'])
def key():
    user = request.form["username"]
    if 'file' not in request.files:
        return "didn't upload a file"
    file = request.files['file']
    if pat.fullmatch(user) is None:
        return "bad user name"
    else:
        users = []
        with open(USER_DB, "r") as f:
            users = f.read().splitlines()
        if user in users:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], user+".pub"))
            # Reset the docker container for git to have it use the same ssh keys enabled for ghidra
            if GIT_DOCKER_ENABLED:
                docker.containers.get(GIT_DOCKER_NAME).reset()
            return "uploaded key for "+user
        else:
            return "bad user name "+user
        
@app.route('/server', methods=['POST'])
def ghidra_health():
    a = subprocess.check_output([GHIDRA_STATUS_TOOL, "status"])
    # checkoutput of the subprocess run to see if the lines contain "Running     : true"
    if b"Running     : true" in a:
        return "ghidra is running"
    else:
        subprocess.run([GHIDRA_STATUS_TOOL, "start"])
        a = subprocess.check_output([GHIDRA_STATUS_TOOL, "status"])
        # checkoutput of the subprocess run to see if the lines contain "Running     : true"
        if b"Running     : true" in a:
            return "ghidra started"
        else:
            return "ghidra failed to start"

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to something.
    PRIVATE_HOST=os.environ.get('WG_IP')
    port = int(os.environ.get('GHIDRA_WEB_PORT', 7921))
    app.run(host=PRIVATE_HOST, port=port)

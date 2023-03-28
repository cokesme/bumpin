#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, redirect, render_template, request, abort, after_this_request
from urllib.parse import urlparse
import subprocess
import os
import re

# Environment variables
# GHIDRA_DATA_DIR: where to store the user database and ssh keys
# GHIDRA_HOME: where to store the user database and ssh keys
# GHIDRA_INSTALL_DIR: where to find the ghidra server admin tool
# GHIDRA_WEB_PORT: port to run the web server on
# WG_IP: ip to bind to

# No idea how to do config shit
GHIDRA_DATA_DIR= os.environ.get('GHIDRA_DATA_DIR', '/home/ghidra/data')
UPLOAD_FOLDER = GHIDRA_DATA_DIR+'/ssh'
USER_DB = GHIDRA_DATA_DIR+'/users.txt'
GHIDRA_HOME = os.environ.get('GHIDRA_HOME', '/home/ghidra/data')
GHIDRA_INSTALL_DIR= os.environ.get('GHIDRA_DATA_DIR', '/home/ghidra/ghidra/data')
GHIDRA_HOME = "/home/ghidra/ghidra/"
GHIDRA_ADMIN_TOOL = GHIDRA_INSTALL_DIR+'/server/svrAdmin'

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
            return "added user"+user
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
            return "uploaded key for "+user
        else:
            return "bad user name "+user

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to something.
    PRIVATE_HOST=os.environ.get('WG_IP')
    port = int(os.environ.get('GHIDRA_WEB_PORT', 7921))
    app.run(host=PRIVATE_HOST, port=port)

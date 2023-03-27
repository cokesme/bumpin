#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, redirect, render_template, request, abort, after_this_request
from urllib.parse import urlparse
import subprocess
import os
import re

UPLOAD_FOLDER = '/home/ghidra/repos/ssh'
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ghidra_dir = "/home/ghidra/ghidra/"

pat = re.compile(r"^[a-zA-Z]{1,20}$")

@app.route('/add', methods=['POST'])
def add():
    user = request.form["username"].strip()
    if pat.fullmatch(user) is None:
        return "bad user name "+user
    else:
        users = []
        with open(ghidra_dir+"/server/users.txt", "r") as f:
            users = f.read().splitlines()
        if user not in users:
            subprocess.run([ghidra_dir+"/server/svrAdmin", "-add", user])
            with open(ghidra_dir+"/server/users.txt", "a") as f:
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
        with open(ghidra_dir+"/server/users.txt", "r") as f:
            users = f.read().splitlines()
        if user in users:
            subprocess.run([ghidra_dir+"/server/svrAdmin", "-reset", user])
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
        with open(ghidra_dir+"/server/users.txt", "r") as f:
            users = f.read().splitlines()
        if user in users:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], user+".pub"))
            return "uploaded key for "+user
        else:
            return "bad user name "+user

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    PRIVATE_HOST=os.environ.get('PRIVATE_HOST')
    port = int(os.environ.get('PORT', 7921))
    app.run(host=PRIVATE_HOST, port=port)

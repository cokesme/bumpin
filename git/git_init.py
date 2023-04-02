#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
import os
import re
import pygit2 as git

# Requirements: flask, libgit2

# Environment variables
# REPOS: where to store the user database
# WEB_GIT_HELPER: port to run the web server on

# No idea how to do config shit
REPOS = os.environ.get("REPOS", "/data/repos")

app = Flask(__name__)

# security...
pat = re.compile(r"^[a-zA-Z]{1,100}$")

@app.route('/add', methods=['POST'])
def add():
    repo_name = request.form["repo"].strip()
    if pat.fullmatch(repo_name) is None:
        return "bad reponame. only a-zA-Z"+repo_name
    else:
        repo_name = git.init_repository(repo_name, bare=True, mode=git.GIT_REPOSITORY_INIT_SHARED_ALL, workdir_path=REPOS)
        return "repo created "+repo_name
        

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to something.
    PRIVATE_HOST=os.environ.get('WG_IP')
    port = int(os.environ.get('WEB_GIT_HELPER', 7921))
    app.run(host=PRIVATE_HOST, port=port)

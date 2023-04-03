#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
import os
import docker as dockerlib
import subprocess

# Requirements: flask, libgit2

# Environment variables
# GHIDRA_INSTALL_DIR: where to find the ghidra server admin tool
# WG_IP: ip to bind to
# SERVICE_HEALTH_PORT: port to run the web server on

GHIDRA_INSTALL_DIR= os.environ.get('GHIDRA_INSTALL_DIR', '/home/ghidra/ghidra/data')
GHIDRA_ADMIN_TOOL = GHIDRA_INSTALL_DIR+'/server/ghidraSvr'
# The compose project name
COMPOSE_TEMPLATE = "research-{}-1"

app = Flask(__name__)
docker = dockerlib.from_env()

@app.route('/docker/<service>', methods=['GET'])
def docker_health(service):
    try:
        docker.containers.get(COMPOSE_TEMPLATE.format(service))
        return {'status': 'running'}
    except dockerlib.errors.NotFound:
        return {'status': 'stopped'}, 404

@app.route('/ghidra', methods=['GET'])
def ghidra_health():
    a = subprocess.check_output([GHIDRA_ADMIN_TOOL, "status"])
    # checkoutput of the subprocess run to see if the lines contain "Running     : true"
    if b"Running     : true" in a:
        return {'status': 'running'}
    else:
        return {'status': 'stopped'}, 404
        
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to something.
    PRIVATE_HOST=os.environ.get('WG_IP')
    port = int(os.environ.get('SERVICE_HEALTH_PORT', 7921))
    app.run(host=PRIVATE_HOST, port=port)

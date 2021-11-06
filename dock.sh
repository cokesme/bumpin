#!/bin/bash
docker run -d -p 10.69.69.1:2222:22 -v /home/lol/keys:/git-server/keys -v /home/lol/git:/git-server/repos jkarlos/git-server-docker

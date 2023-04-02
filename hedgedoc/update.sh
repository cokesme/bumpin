#!/bin/bash

docker compose -p research cp ./history.js doc-app:/hedgedoc/lib/history.js
echo "now commit the container and update the docker service to use that image"
#/bin/bash

docker run -v ./gitgo:/app golang:alpine go build -C /app gitcgi.go

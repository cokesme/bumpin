#!/bin/bash

# revsync config
# Environment variables:
#  REDIS_PASSWORD
#  WG_IP
cat > config.json <<EOF
{
    "host": "$WG_IP",
    "port": 6379,
    "password": "$REDIS_PASSWORD",
    "nick": 
}
EOF

# Arguments 
# 1. ghidra data directory

cat >ser.diff<<EOF
--- /server/server.conf	2020-02-12 12:10:44.000000000 +0000
+++ server/server_new.conf	2020-11-01 16:47:28.661548715 +0000
@@ -101,7 +101,7 @@
 # Ghidra installation directory, although an absolute path is preferred if not using default.
 # This variable is also used by the svrAdmin script.
 
-ghidra.repositories.dir=./repositories
+ghidra.repositories.dir=$1
 
 # Ghidra server startup parameters.  
 #
@@ -155,7 +155,7 @@
 #                       used to store repositories.  Use of this variable to define the
 #                       repositories directory must be retained.
 wrapper.app.parameter.1=-a0
-wrapper.app.parameter.2=\${ghidra.repositories.dir}
+wrapper.app.parameter.5=\${ghidra.repositories.dir}
 
 # Establish server process owner
 # This should only be used when installing as a service using a nologin
@@ -240,3 +240,7 @@
 # Restart failed service after 1 minute delay
 wrapper.ntservice.failure_actions.actions=RESTART
 wrapper.ntservice.failure_actions.actions_delay=60000
+wrapper.app.account=$USER
+wrapper.app.parameter.2=-u
+wrapper.app.parameter.4=-i$WG_IP
+wrapper.app.parameter.3=-ssh
EOF
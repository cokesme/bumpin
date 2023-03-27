#!/bin/bash

# Need to configured some iptables shiz as well
# Make a new chain for the wg0 interfaces
# iptables -N wg0
# iptables -A wg0 -i wg0 -j wg0 -j ACCEPT
# The above doesn't work though. 
# Need to be very targetted with this

# Honestly, we don't need to forward to each other
# Mainly to prevent the following:
# anyone can connect to anyone else's local shit that default bind to all interfaces on the wg client right now, right



ip link add dev wg0 type wireguard
ip address add dev wg0 10.1.56.3/16

key=$(wg genkey)
echo $(echo $key | wg pubkey)
cat > ./conf << EOF
[Interface]
Privatekey = $key

[Peer]
PublicKey = $1
AllowedIPS= 10.1.56.1/32
PersistentKeepAlive=20
EOF

wg setconf wg0 ./conf
ip link set up dev wg0
echo "run \`wg\` to get the port"

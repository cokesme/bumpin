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

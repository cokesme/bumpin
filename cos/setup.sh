#!/bin/bash

#from https://askubuntu.com/a/30157
if [[ $(id -u) -eq 0 ]]; then
    echo "don't run as root"
    exit 1
fi

cd $HOME

# get depot_tools
# http://commondatastorage.googleapis.com/chrome-infra-docs/flat/depot_tools/docs/html/depot_tools_tutorial.html
git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
. PATH=$HOME/depot_tools:$PATH
export PATH=$HOME/depot_tools:$PATH

echo "export PATH=/path/to/depot_tools:$PATH" >> ~/.bashrc

# https://cloud.google.com/container-optimized-os/docs/how-to/building-from-open-source
mkdir $HOME/cos-src
cd $HOME/cos-src
repo init -u https://cos.googlesource.com/cos/manifest.git \
  --repo-url https://chromium.googlesource.com/external/repo.git \
  -b release-R89
repo sync

# https://stackoverflow.com/questions/2953081/how-can-i-write-a-heredoc-to-a-file-in-bash-script
cat <<EOF > ./build.sh
#!/bin/bash
./build_packages --board=lakitu
./build_image --board=lakitu test
EOF
chmod +x ./build.sh

cat <<EOF > ./run.sh
#!/bin/bash
kvm -m 1024 -nographic -net nic,model=virtio -net user,hostfwd=tcp:127.0.0.1:9222-:22 -hda src/build/images/lakitu/latest/chromiumos_test_image.bin
EOF
chmod +x ./run.sh

cat <<EOF > ./connect.sh
#!/bin/bash
ssh -t root@localhost -p 9222 -i src/build/images/lakitu/latest/id_rsa "cd /var/lib/cloud/;bash -l"
EOF
chmod +x ./connect.sh

cat <<EOF > ./scp.sh
#!/bin/bash
ssh -P 9222 -i src/build/images/lakitu/latest/id_rsa $1 root@localhost:/var/lib/cloud/
EOF
chmod +x ./scp.sh

# after you are in the cros_sdk, you can build the image 
cros_sdk --enter

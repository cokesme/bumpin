# Repos that I follow, forked,starred because ? not sure 
## Forked
Wow, the whole reason that I had forked repos because I was scared of people deleting shit. I was about to go wipe everything. The problem is that apparently github actually doesn't delete all forks when it deletes repos, well. It didn't at some points because I still have these two repos...
```
gh repo list --fork -L 300 --json parent,nameWithOwner -q '.[] | [.parent.owner.login,.parent.name, .nameWithOwner] | select(.[0] == null)'
[null,null,"cokesme/Exploit11.2"]
[null,null,"cokesme/jailbreakme103"]
```

###  Repos that I've actually done things with
```
gh repo list --fork -L 300 --json nameWithOwner,createdAt,updatedAt,pushedAt -q "map(select(.createdAt<.pushedAt))" | convertfrom-json | format-table nameWithOwner

nameWithOwner
-------------
cokesme/applepie
cokesme/bochscpu-build
cokesme/rewind
cokesme/edgetpuxray
cokesme/raspberrypi
cokesme/angr-doc
cokesme/ctf-tools
```
### All
gamozolabs/applepie cokesme/applepie
yrp604/bochscpu-build cokesme/bochscpu-build
quarkslab/rewind cokesme/rewind
geohot/edgetpuxray cokesme/edgetpuxray
gitbubaa/binaryninja-api cokesme/binaryninja-api
yrp604/bochscpu-bench cokesme/bochscpu-bench
MattPD/cpplinks cokesme/cpplinks
ioncodes/vacation3-emu cokesme/vacation3-emu
FIRMCORN-Fuzzing/FIRMCORN cokesme/FIRMCORN
CptGibbon/House-of-Corrosion cokesme/House-of-Corrosion
solar-wine/tools-for-hack-a-sat-2020 cokesme/tools-for-hack-a-sat-2020
zoogie/new-browserhax cokesme/new-browserhax
deptofdefense/HAS-Qualifier-Challenges cokesme/HAS-Qualifier-Challenges
google/security-research-pocs cokesme/script_gadgets_fork
grimm-co/NotQuite0DayFriday cokesme/NotQuite0DayFriday
0xeb-bp/cve-2020-1054 cokesme/cve-2020-1054
epakskape/whpexp cokesme/whpexp
ADDVulcan/ADDVulcan cokesme/ADDVulcan-1
williamshowalter/revsync_ghidra cokesme/revsync_ghidra
JustinOng/has20q-iseewhatyoudidthere cokesme/has20q-iseewhatyoudidthere
pdabacus/hackasat cokesme/hackasat
vivisect/vivisect cokesme/vivisect
intel/kernel-fuzzer-for-xen-project cokesme/kernel-fuzzer-for-xen-project
chompie1337/s8_2019_2215_poc cokesme/s8_2019_2215_poc
dwelch67/raspberrypi cokesme/raspberrypi
seemoo-lab/internalblue cokesme/internalblue
seemoo-lab/frankenstein cokesme/frankenstein
0xeb-bp/cve-2020-0796 cokesme/cve-2020-0796
google/fuzzbench cokesme/fuzzbench
nautilus-fuzz/nautilus cokesme/nautilus
atrosinenko/kbdysch cokesme/kbdysch
S2E/libcpu cokesme/libcpu
github/training-kit cokesme/training-kit
tetrane/reven2-resources cokesme/reven2-resources
mephi42/ctftool cokesme/ctftool
alephsecurity/xnu-qemu-arm64 cokesme/xnu-qemu-arm64
cromulencellc/shoggoth-extras cokesme/shoggoth-extras
cromulencellc/qemu-shoggoth cokesme/qemu-shoggoth
alephsecurity/xnu-qemu-arm64-tools cokesme/xnu-qemu-arm64-tools
kentavv/binary_viewer cokesme/binary_viewer
teesec/simta cokesme/simta
yossizap/angrcutter cokesme/angrcutter
andreafioraldi/angrdbg cokesme/angrdbg
andreafioraldi/qasan cokesme/qasan
Fire30/bad_hoist cokesme/bad_hoist
microsoft/pxt cokesme/pxt
SeanHeelan/HeapLayout cokesme/HeapLayout
greyd0g/Program-Analysis-Note cokesme/program-analysis-note
eqv/aflq_fast_cov cokesme/aflq_fast_cov
oshogbo/ghidra-lx-loader cokesme/ghidra-lx-loader
WithSecureLabs/Jandroid cokesme/Jandroid
googleprojectzero/ktrw cokesme/ktrw
Escapingbug/xctf-2019-final-tnj cokesme/xctf-2019-final-tnj
Comsecuris/gdbghidra cokesme/gdbghidra
leesh3288/CTF cokesme/CTF-2
Friz-zy/awesome-linux-containers cokesme/awesome-linux-containers
RUB-SysSec/grimoire cokesme/grimoire
Comsecuris/qemu-hexagon cokesme/qemu-hexagon
mm0r1/exploits cokesme/exploits
ray-cp/vm-escape cokesme/vm-escape
stereobooster/awesome-hiring-process cokesme/awesome-hiring-process
RUB-SysSec/redqueen cokesme/redqueen
likvidera/Documentation cokesme/Documentation
beafb1b1/challenges cokesme/challenges
OpenAtomFoundation/TencentOS-tiny cokesme/TencentOS-tiny
TeamContagion/CTF-archive cokesme/CTF-archive-1
mrkmarron/node-chakracore-time-travel-debugger cokesme/node-chakracore-time-travel-debugger
Qwaz/solved-hacking-problem cokesme/solved-hacking-problem
ww9210/kepler-cfhp cokesme/kepler-cfhp
NeSE-Team/OurChallenges cokesme/OurChallenges
google/minetest_pnr cokesme/minetest_pnr
yifengyou/LinuxKernelTravel cokesme/LinuxKernelTravel
KVM-VMI/kvm-vmi cokesme/kvm-vmi
kingkaki/Exploit-scripts cokesme/Exploit-scripts
HexHive/retrowrite cokesme/retrowrite
zardus/paper-templates cokesme/paper-templates
geohot/fromthetransistor cokesme/fromthetransistor
ComputerSystemLab/hqemu cokesme/hqemu
bkerler/ghidra_installer cokesme/ghidra_installer
NationalSecurityAgency/ghidra cokesme/ghidra
google/clusterfuzz cokesme/clusterfuzz
0vercl0k/windbg-scripts cokesme/windbg-scripts
Synacktiv-contrib/CVE-2018-4193 cokesme/CVE-2018-4193
f1yyy/RealWorldCTF cokesme/RealWorldCTF
RUB-SysSec/kAFL cokesme/kAFL
TeamMolecule/mep-wtf cokesme/mep-wtf
TeamMolecule/mepulator cokesme/mepulator
ValveSoftware/steamlink-sdk cokesme/steamlink-sdk-1
saelo/35c3ctf cokesme/35c3ctf-1
bkth/35c3ctf cokesme/35c3ctf
TeamMolecule/petite-mort cokesme/petite-mort
TeamMolecule/35c3-slides cokesme/35c3-slides
allpaca/V8Harvest cokesme/V8Harvest
RPwnage/Warri0r cokesme/Warri0r
TheOfficialFloW/h-encore cokesme/h-encore
hongriSec/CTF-Training cokesme/CTF-Training
decaf-project/DECAF cokesme/DECAF
theKidOfArcrania/abyss-exploit cokesme/abyss-exploit
0xAX/linux-insides cokesme/linux-insides
xboot/xboot cokesme/xboot
ww9210/kernel4.20_bpf_LPE cokesme/kernel4.20_bpf_LPE
greekn/rce-bug2.0 cokesme/rce-bug2.0
renorobert/virtualbox-virtualkd-bug cokesme/virtualbox-virtualkd-bug
WinMin/awesome-vm-exploit cokesme/awesome-vm-exploit
Cisco-Talos/pyrebox cokesme/pyrebox
fail0verflow/ps4-kexec cokesme/ps4-kexec
Zero-Tang/NoirVisor cokesme/NoirVisor
afang5472/binaryfang cokesme/binaryfang
greekn/rce-bug cokesme/rce-bug
mengqhui/baidudl cokesme/baidudl
vakzz/wasm-cheat-engine cokesme/wasm-cheat-engine
trimstray/iptables-essentials cokesme/iptables-essentials
vidar-team/HCTF2018 cokesme/HCTF2018
tbfleming/cib cokesme/cib
veritas501/hctf2018 cokesme/hctf2018-1
fantasyqt/hctf2018_share cokesme/hctf2018_share
MorteNoir1/virtualbox_e1000_0day cokesme/virtualbox_e1000_0day
CTFTraining/sctf_2018_babysyc cokesme/sctf_2018_babysyc
SoftSec-KAIST/GitCTF cokesme/GitCTF
bash-c/slides cokesme/slides
tsg-ut/cbctf2018-final cokesme/cbctf2018-final
lunixbochs/bnrepl cokesme/bnrepl
jserv/mini-arm-os cokesme/mini-arm-os
teambi0s/InCTFi cokesme/InCTFi
jas502n/CVE-2018-14665 cokesme/CVE-2018-14665
legitbs/finals-2015 cokesme/finals-2015
ctf-zone/final-services-2017 cokesme/final-services-2017
rosdyana/CTF cokesme/CTF-1
wmliang/windowsland cokesme/windowsland
Nan3r/myspider cokesme/myspider
kkHAIKE/tinyidb cokesme/tinyidb
RKX1209/kmemlearn cokesme/kmemlearn
pandazheng/IosHackStudy cokesme/IosHackStudy
cxm95/sDriller cokesme/sDriller
jbccollins/metro-monitor cokesme/metro-monitor
spencertipping/jit-tutorial cokesme/jit-tutorial
kaishack/sctf2018 cokesme/sctf2018
ww9210/Linux_kernel_exploits cokesme/Linux_kernel_exploits
shift-crops/EscapeMe cokesme/EscapeMe
swisskyrepo/PayloadsAllTheThings cokesme/PayloadsAllTheThings
veritas501/my-ctf-xinetd cokesme/my-ctf-xinetd
renorobert/rwctf-kid-vm cokesme/rwctf-kid-vm
szysec/ctftest cokesme/ctftest
danbev/learning-v8 cokesme/learning-v8
rocky/python-uncompyle6 cokesme/python-uncompyle6
xairy/kernel-exploits cokesme/kernel-exploits
trailofbits/appjaillauncher-rs cokesme/appjaillauncher-rs
ujin5/ctfwriteup cokesme/ctfwriteup
RolfRolles/Atredis2018 cokesme/Atredis2018
epinna/tplmap cokesme/tplmap
syuu1228/howto_implement_hypervisor cokesme/howto_implement_hypervisor
sycurelab/DECAFImages cokesme/DECAFImages
TeamMolecule/toshiba-mep-idp cokesme/toshiba-mep-idp
skysider/VulnPOC cokesme/VulnPOC
zwade/s-exploitation cokesme/s-exploitation
miyase256/exgdb cokesme/exgdb
can1357/CVE-2018-8897 cokesme/CVE-2018-8897
hama7230/ctftemp cokesme/ctftemp
siemens/jailhouse cokesme/jailhouse
Nu1LCTF/n1ctf-2018 cokesme/n1ctf-2018
siemens/freertos-cell cokesme/freertos-cell
travisgoodspeed/goodwatch cokesme/goodwatch
Apogee-Research/STAC cokesme/STAC
GoSecure/php7-opcache-override cokesme/php7-opcache-override
Manouchehri/zer0con2018_singi cokesme/zer0con2018_singi
jas502n/2018-QWB-CTF cokesme/2018-QWB-CTF
zjw88282740/QWB2018-Pwn cokesme/QWB2018-Pwn
integeruser/on-pwning cokesme/on-pwning
dangokyo/QEMU_ESCAPE cokesme/QEMU_ESCAPE
jas502n/Ubuntu-0day cokesme/Ubuntu-0day
jas502n/0day-security-software-vulnerability-analysis-technology cokesme/0day-security-software-vulnerability-analysis-technology
veritas501/CHIP-8_Emulator cokesme/CHIP-8_Emulator
DigApis-Michael/ctf_re cokesme/ctf_re
saaramar/execve_exploit cokesme/execve_exploit
neargle/PIL-RCE-By-GhostButt cokesme/PIL-RCE-By-GhostButt
viewer2018/ctf_web cokesme/ctf_web
k0keoyo/Dark_Composition_case_study_Integer_Overflow cokesme/Dark_Composition_case_study_Integer_Overflow
rmitton/goaldis cokesme/goaldis
oalieno/MYCTF-Challenge cokesme/MYCTF-Challenge
sroettger/gce-ctf cokesme/gce-ctf
kirschju/wiedergaenger cokesme/wiedergaenger
SECCON/SECCON2017_online_CTF cokesme/SECCON2017_online_CTF
SteamRE/SteamKit cokesme/SteamKit
moonlight-stream/moonlight-android cokesme/moonlight-android
mcd1992/steamlink-sdk cokesme/steamlink-sdk
moonlight-stream/moonlight-common-android cokesme/moonlight-common
RKX1209/kernel_exploit_world cokesme/kernel_exploit_world
Tzaoh/pwning cokesme/pwning
moonlight-stream/moonlight-common-c cokesme/moonlight-common-c
bluepichu/dungeonkit-temp cokesme/dungeonkit-temp
buserror/simavr cokesme/simavr
mailinneberg/BlueBorne cokesme/BlueBorne-1
ScottyBauer/Android_Kernel_CVE_POCs cokesme/Android_Kernel_CVE_POCs
theori-io/pwnjs cokesme/pwnjs
osirislab/CSAW-CTF-2017-Finals cokesme/CSAW-CTF-2017-Finals
platomav/MCExtractor cokesme/MCExtractor
yuawn/my-ctf-design cokesme/My_CTF_Design
Nimsay/LLL--Attack cokesme/LLL--Attack
ntddk/transcibe cokesme/transcibe
ArmisSecurity/blueborne cokesme/blueborne
cn0xroot/RFSec-ToolKit cokesme/RFSec-ToolKit
Dor1s/libfuzzer-workshop cokesme/libfuzzer-workshop
hayzamjs/Blueborne-CVE-2017-1000251 cokesme/Blueborne-CVE-2017-1000251
hook-s3c/blueborne-scanner cokesme/blueborne-scanner
shift-crops/House_of_Rabbit cokesme/House_of_Rabbit
Comsecuris/mtk-baseband-sanctuary cokesme/mtk-baseband-sanctuary
unamer/vmware_escape cokesme/vmware_escape
Comsecuris/ida_strcluster cokesme/ida_strcluster
mimoo/RSA-and-LLL-attacks cokesme/RSA-and-LLL-attacks
bee13oy/AV_Kernel_Vulns cokesme/AV_Kernel_Vulns
Vector35/traceapi cokesme/traceapi
voidALPHA/cgc_viz cokesme/cgc_viz
k0keoyo/SSCTF-pwn450-ms16-034-writeup cokesme/SSCTF-pwn450-ms16-034-writeup
iagox86/ctfworkshop-2017 cokesme/ctfworkshop-2017
jmpews/pwn2exploit cokesme/pwn2exploit
Insomnihack/Teaser-2017 cokesme/Teaser-2017
carzil/brainfuck-jit cokesme/brainfuck-jit
JideTechnology/remixos-kernel cokesme/remixos-kernel
RKX1209/TinyLinux cokesme/TinyLinux
zh-explorer/hctf2016-binarier cokesme/hctf2016-binarier
tutsplus/how-to-create-an-isometric-layout-with-css-3d-transforms cokesme/how-to-create-an-isometric-layout-with-css-3d-transforms
mist64/geos cokesme/geos
vitasdk/buildscripts cokesme/buildscripts
devttys0/IRis cokesme/IRis
vitasdk/vita-toolchain cokesme/vita-toolchain
greatscottgadgets/hackrf cokesme/hackrf
ANDnXOR/ANDnXOR_DC24_Badge cokesme/ANDnXOR_DC24_Badge
spang-a-lang/BLE-Security cokesme/BLE-Security
pwnieexpress/blue_hydra cokesme/blue_hydra
cryptovillage/badge2016 cokesme/badge2016
DeviationTX/deviation cokesme/deviation
chubbymaggie/pysymemu cokesme/pysymemu
Comsecuris/shannonRE cokesme/shannonRE
sharebrained/portapack-hackrf cokesme/portapack-hackrf
greatscottgadgets/greatfet-hardware cokesme/greatfet
travisgoodspeed/goodfet cokesme/goodfet
comex/xap cokesme/xap
juergh/lqs2mem cokesme/lqs2mem
moonlight-stream/moonlight-docs cokesme/moonlight-docs
jcmvbkbc/gcc-xtensa cokesme/gcc-xtensa
rad1o/f1rmware cokesme/f1rmware
Fuzion24/AndroidKernelExploitationPlayground cokesme/AndroidKernelExploitationPlayground
MaskRay/DEFCONCTFFinalsGameboxAdmin cokesme/DEFCONCTFFinalsGameboxAdmin
angr/angr-doc cokesme/angr-doc
zardus/ctf-tools cokesme/ctf-tools
rebelbot/binvis cokesme/binvis
umisama/seccon06 cokesme/seccon06
rad1o/hardware cokesme/hardware
pwndbg/pwndbg cokesme/pwndbg
akiym/adctf2014 cokesme/adctf2014
cryptovillage/badge2015 cokesme/badge2015
smealum/aemstro cokesme/aemstro
thetransistor/DefCon23 cokesme/DefCon23
seeess/Defcon-Shoot-23-Badge cokesme/Defcon-Shoot-23-Badge
fqj1994/XCTF2015-Missle cokesme/XCTF2015-Missle
stephen-kun/csr8670 cokesme/csr8670
unixist/camb cokesme/camb
k0keoyo/broppy cokesme/broppy
Vector35/HackingGames cokesme/HackingGames
Insomnihack/Insomnihack-2015 cokesme/Insomnihack-2015
saelo/armpwn cokesme/armpwn
LightningTH/GiTS cokesme/GiTS
Insomnihack/Teaser-2015 cokesme/Teaser-2015
mmistakes/so-simple-theme cokesme/jekyll-test
legitbs/quals-2014 cokesme/quals-2014
thetransistor/dc22-dc801-party-badge cokesme/dc22-dc801-party-badge
half-duplex/defcon-2014-ctf-quals-legitbs cokesme/defcon-2014-ctf-quals-legitbs
HackerDom/ructfe-2013 cokesme/ructfe-2013
guhe120/CVE20131491-JIT cokesme/CVE20131491-JIT
thetransistor/DC21_Badge cokesme/DC21_Badge
CunningLogic/LGPwn cokesme/LGPwn
0xdkay/recruit cokesme/recruit
rpw/flsloader cokesme/flsloader

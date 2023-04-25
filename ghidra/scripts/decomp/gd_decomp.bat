echo "running command:"
set server="10.2.44.101"
set reponame="hub"
:: folder path is provided as an argument. You do not need to specify the root folder because that is the repo/project name
set ghidra_project="ghidra://%server%/%reponame%/%1"

:: had to use specific keys
:: ssh-keygen -m pem -t rsa -b 2048

:: Process all files in a given folder.
analyzeHeadless %ghidra_project% -process -connect test -keystore %USERPROFILE%\.ssh\lol -readOnly -recursive -scriptPath . -postScript Decompile.java 
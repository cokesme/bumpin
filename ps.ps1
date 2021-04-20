while(1){ cmd.exe /c "wmic.exe path Win32_process get name, processid, commandline /format:list" | select-string -Pattern headless -Context 3,4; start-sleep -seconds 3; clear}

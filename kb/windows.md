# Win 11
Compatability [requirements](https://www.microsoft.com/en-us/windows/windows-11-specifications?r=1)...
laptop

1. ram: 4gb
2. storage: 64gb
1. uefi
1. tpm
`tpm.msc`
tpm: IFX, 5.40.1971.2, 2.0 
Infineon tpm
2. cpu
my cpu: i7-6500U
Not on the windows 11 [list](https://learn.microsoft.com/en-us/windows-hardware/design/minimum/supported/windows-11-supported-intel-processors)..., but is on the Windows 10

battery is much better without it. Should run the pc health check

# wine
https://gitlab.winehq.org/wine/wine/-/tree/wine-7.22

shit takes more than 1gb to build and I have to disable everything and it still builds too much into it on uuid.o... Ugh, and their configure f's up and doesn't provide the `lpthread` flag to `LDFLAGS` for ntdll.so?

and it doesn't matter because turns out the error tool is 32 bit so it won't work with my configuration

# drivers/wdk
## version shiz
no vs install
```
Copy-Item "\"${Env:ProgramFiles(x86)}\Windows Kits\10\Vsix\VS2019\WDK.vsix\"" 'C:\wdkvsix.zip'
Expand-Archive 'C:\wdkvsix.zip' -DestinationPath 'C:\WdkVsix'
Copy-Item 'C:\WdkVsix\$MSBuild\Microsoft\*' -Destination 'C:\BuildTools2019\MSBuild\Microsoft' -Recurse -Force
Remove-Item 'C:\WdkVsix' -Force -Recurse 
Remove-Item 'C:\wdkvsix.zip' -Force


installing the correct version of the sdk for the wdk 
C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\MSBuild\Microsoft
spectre libs
we dont ship

run as admin to test sign
```

## Error Codes
Lookup tool: https://learn.microsoft.com/en-us/windows/win32/debug/system-error-code-lookup-tool
- 0x800F0900: CBS_E_XML_PARSER_FAILURE (during update some manifest shit)
- 0x80240009: something else happening at same time (update issue installing optional driver)
- 0x80004005: generic (Intel SGX AESM, cphs)
- 0xC00000D4: STATUS_NOT_SAME_DEVICE (kernel boot fast-start failure)
- 0x80240016: WU_E_INSTALL_NOT_ALLOWED (defender av kb)
- 0x80073D02: ERRO_PACKAGES_IN_USE

## startup shit
Windows PCs typically operate in a number of Advanced Configuration and Power Interface (ACPI) power states. An S0 power state, for example, is when your PC is running and ready to respond to your input. There are a number of sleep states, including S1, S2, and S3, and there's also a hybrid sleep state where hibernation is used in tandem with a sleep state.

Hibernation is considered an S4 power state. While hibernating, your PC will seem like it's completely off, but there will be a saved hibernation file ready to be used to boot back to where you were during your last user session. Some power is usually still routed to peripherals so that you can, say, tap your keyboard and have the PC boot.

An S5 power state (soft off) is when your PC is shut down and rebooted completely. There's no hibernation file and no saved user session. There is also a G3 power state, which is when your PC consumes absolutely no power and is completely turned off.

With fast startup enabled, choosing to shut down your PC might look like you're completely shutting things down, but in reality, your PC is entering a mix between a shutdown and hibernation. A hibernation file is indeed used, although it is smaller than usual. Why? You're logged off before the file is created, meaning your session is not recorded. The speed boost comes from the Windows kernel being saved on your hard drive and loaded when booting. [source](https://www.windowscentral.com/how-disable-windows-10-fast-startup) cale hunt

## fix update issues
- troubleshooter
- sfc /scannow
- dism checkhealth
internet advise that doesn't work
```
net stop wuauserv
net stop cryptSvc
net stop bits
net stop msiserver
ren C:\Windows\SoftwareDistribution SoftwareDistribution.old
ren C:\Windows\System32\catroot2 catroot2.old
net start wuauserv
net start cryptSvc
net start bits
net start msiserver
```
downloading from the catalog
```
move *.mum C:\Windows\servicing\Packages\
C:\Users\test\Downloads\package_1_for_kb5012170~31bf3856ad364e35~amd64~~10.0.1.1.mum
C:\Users\test\Downloads\package_2_for_kb5012170~31bf3856ad364e35~amd64~~10.0.1.1.mum
C:\Users\test\Downloads\package_3_for_kb5012170~31bf3856ad364e35~amd64~~10.0.1.1.mum
```

Relevant directories:
1. C:\Windows\servicing\Packages
2. C:\Windows\SoftwareDistribution
3. C:\Windows\Logs\CBS
4. C:\Windows\winsxs\

Try to remove 
```
\winsxs\manifests\amd64_microsoft-windows-s..boot-firmwareupdate_31bf3856ad364e35_10.0.19041.1880_none_294d9e3cbae1ff57.manifest
```
no luck

## TrustedInstaller Shit
1. https://bugs.chromium.org/p/project-zero/issues/detail?id=997
```
REM START
sc config TrustedInstaller binPath= "cmd.exe /C sc stop windefend && sc delete windefend" && sc start TrustedInstaller
REM END
```


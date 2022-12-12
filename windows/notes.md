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
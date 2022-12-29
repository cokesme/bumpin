# Linux
## Docs
- https://docs.kernel.org/search.html?q=kcsan&check_keywords=yes&area=default#

## Bugs
- Best part is the attachment with generic ish kaslr defeat https://bugs.chromium.org/p/project-zero/issues/detail?id=2351
- heap reuse to lead to credential overrite: https://github.com/Markakd/DirtyCred
- ksmbd has remote which is smb in the kernel even though iouring with samba (smbd) is faster, and there were tons of signs of it being a terrible kernel driver
    - https://www.zerodayinitiative.com/advisories/ZDI-22-1690/
    ```
    This vulnerability allows remote attackers to execute arbitrary code on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability, but only systems with ksmbd enabled are vulnerable.

    The specific flaw exists within the processing of SMB2_TREE_DISCONNECT commands. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the kernel.    
    ``` 
    - [fix](https://cdn.kernel.org/pub/linux/kernel/v5.x/ChangeLog-5.15.61)
    - [rough start](https://lwn.net/Articles/871866/)
    - [perf](https://samba.plus/blog/detail/ksmbd-a-new-in-kernel-smb-server)
    - [openwrt](https://github.com/openwrt/openwrt/pull/11603)
       
   

## fuzzers
### syzkaller
- https://github.com/google/syzkaller
- https://github.com/SunHao-0/healer (rust, uses syzlang and some relational shiz)

### Mitigations
[sanitizers](https://google.github.io/kernel-sanitizers/)
[Issue backlog for sanitizer work](https://bugzilla.kernel.org/buglist.cgi?component=Sanitizers&product=Memory%20Management&resolution=---)
#### kcsan
- https://google.github.io/kernel-sanitizers/kcsan/LPC2020-KCSAN.pdf
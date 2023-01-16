# Linux
## Docs
- https://docs.kernel.org/search.html?q=kcsan&check_keywords=yes&area=default#

## Bugs
1. kctf bugs and exploit techniques from google: https://docs.google.com/document/d/1a9uUAISBzw3ur1aLQqKc5JOQLaJYiOP5pe_B4xCT1KA/edit#, https://docs.google.com/presentation/d/e/2PACX-1vR4mpH3aARLMOhJemVGEw1cduXPEo_PvrbZMum8QwOJ6rhZvvezsif4qtgSydVVt8jPT1fztgD5Mj7q/pub?slide=id.g14c89387e5b_3_106
1. Best part is the attachment with generic ish kaslr defeat https://bugs.chromium.org/p/project-zero/issues/detail?id=2351
2. heap reuse to lead to credential overrite: https://github.com/Markakd/DirtyCred
3. found with default syzkaller in 2022 and used against kctf (introduced in 2019): https://www.willsroot.io/2022/01/cve-2022-0185.html?m=1
4. ksmbd has remote which is smb in the kernel even though iouring with samba (smbd) is faster, and there were tons of signs of it being a terrible kernel driver
    - https://www.zerodayinitiative.com/advisories/ZDI-22-1690/
    ```
    This vulnerability allows remote attackers to execute arbitrary code on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability, but only systems with ksmbd enabled are vulnerable.

    The specific flaw exists within the processing of SMB2_TREE_DISCONNECT commands. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the kernel.    
    ``` 
    - [fix](https://cdn.kernel.org/pub/linux/kernel/v5.x/ChangeLog-5.15.61)
    - [rough start](https://lwn.net/Articles/871866/)
    - [perf](https://samba.plus/blog/detail/ksmbd-a-new-in-kernel-smb-server)
    - [openwrt](https://github.com/openwrt/openwrt/pull/11603)

5. CVE-2022-32250
    - 5.13 [writeup](https://web.archive.org/web/20221205220534/https://research.nccgroup.com/2022/09/01/settlers-of-netlink-exploiting-a-limited-uaf-in-nf_tables-cve-2022-32250/)
    - 5.15 [writeup](https://web.archive.org/web/20220830204358/https://blog.theori.io/research/CVE-2022-32250-linux-kernel-lpe-2022/)
    - 5.18.1 [writeup](https://web.archive.org/web/20221222074310/https://blog.exodusintel.com/2022/12/19/linux-kernel-exploiting-a-netfilter-use-after-free-in-kmalloc-cg/)
"The aforementioned exploitation strategies are different from each other and from the one detailed here since the targeted kernel versions have different peculiarities. In version 5.13, allocations performed with either the GFP_KERNEL flag or the GFP_KERNEL_ACCOUNT flag are served by the kmalloc-* slab caches. In version 5.15, allocations performed with the GFP_KERNEL_ACCOUNT flag are served by the kmalloc-cg-* slab caches. While in both 5.13 and 5.15 the affected object, nft_expr, is allocated using GFP_KERNEL, the difference in exploitation between them arises because a commonly used heap spraying object, the System V message structure (struct msg_msg), is served from kmalloc-* in 5.13 but from kmalloc-cg-* in 5.15. Therefore, in 5.15, struct msg_msg cannot be used to exploit this vulnerability.
In 5.18.1, the object involved in the use-after-free vulnerability, nft_expr, is itself allocated with GFP_KERNEL_ACCOUNT in the kmalloc-cg-* slab caches. Since the exploitation strategies presented by the NCC Group and Theori rely on objects allocated with  GFP_KERNEL, they do not work against the latest vulnerable version of the Linux kernel."
       
   

## fuzzers
### syzkaller
- https://github.com/google/syzkaller
    - syzkaller needed this patch](https://github.com/google/syzkaller/commit/18f846ca807cfc6df9c3da3c0ab08251277dfef0) to rerun syscalls to catch bug 3 above. That wasn't introduced until dec 2021
- https://github.com/SunHao-0/healer (rust, uses syzlang and some relational shiz)

### Mitigations
[sanitizers](https://google.github.io/kernel-sanitizers/)
[Issue backlog for sanitizer work](https://bugzilla.kernel.org/buglist.cgi?component=Sanitizers&product=Memory%20Management&resolution=---)
#### kcsan
- https://google.github.io/kernel-sanitizers/kcsan/LPC2020-KCSAN.pdf
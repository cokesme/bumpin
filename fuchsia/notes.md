# What is this os 
- zircon, c++

## usermode
https://fuchsia.dev/fuchsia-src/concepts/components/v2/components_vs_processes
```
The relationship between components and Zircon tasks differs, often as defined by component runners, which implement strategies for launching component instances.

- ELF Runner launches components by creating a new job that contains a process that's created from a given executable file in ELF format.
- Dart Runner launches a new Dart isolate in a Dart Virtual Machine. A Dart VM is implemented as a process that can host one or more Dart isolate. Dart isolates execute on threads, but don't necessarily have an assigned thread (this is a VM implementation detail).
- Web runner can launch one or more web pages as components, and host them the same web engine container or in separate containers per its isolation policy. Web pages are typically isolated by being hosted in separate processes.
```

## Update system
https://news.ycombinator.com/item?id=31497827
```
Hi there, I work on Fuchsia, specifically on our Software Delivery system [1].
You hit on exactly the right point: it's _possible_ to download and run software on demand, but it's also possible (and recommended) for products to turn off that capability if it's not useful or valuable for their use case. We pin packages for the base system itself, as well as lots of configurations of products.

The ability to run code on demand is really valuable for our development flows and quick prototyping: built a new test or experiment? No need to update your device, just try to run it, and it runs!

[1]: https://fuchsia.dev/fuchsia-src/get-started/learn/intro/pack...


	
erickt 6 months ago | root | parent | next [–]

I also work on Fuchsia’s Software delivery team.
For some more detail on how we secure downloading components, we implement a concept called verified execution [1]. We establish a chain of trust from:

* a hardware key (on hardware that supports it), which checks the signature of

* the bootloader, which has a key baked into it and verifies that each boot slot has a properly signed vbmeta structure. This vbmeta then contains a hash of the zircon kernel, and the merkle root for the user space system image blob.

* we boot up zircon, which eventually starts up blobfs, our content addressed file system. It then reads the system image from blobfs, and launches Component Manager and Package Cache (which implements a package filesystem on top of blobs).

* package cache gets launched with the system image merkle from vbmeta, which allows us to know which packages are part of the base package set.

* base packages are then launched upon demand.

This establishes a direct line of trust from the hardware key to the base packages.

For over the air updates and ephemerally resolved packages, we use The Update Framework [2] and Omaha [3] for our package repositories. Each entry contains the merkle root for the package metadata, which in turn bakes in the merkle roots for each blob in the packages. We bake in the public keys for TUF and Omaha into our system image. This allows us to indirectly verify from hardware up that we are fetching the correct software.

[1]: https://fuchsia.dev/fuchsia-src/concepts/security/verified_e...

[2]: https://theupdateframework.io/

[3]: https://chromium.googlesource.com/chromium/src.git/+/master/...
```

## Security
### linux researcher writeup
https://a13xp0p0v.github.io/img/Alexander_Popov-Fuchsia_pwn.pdf
https://swarm.ptsecurity.com/a-kernel-hacker-meets-fuchsia-os/

### ctf chall
- https://ctftime.org/task/9233
- https://ctftime.org/task/9234

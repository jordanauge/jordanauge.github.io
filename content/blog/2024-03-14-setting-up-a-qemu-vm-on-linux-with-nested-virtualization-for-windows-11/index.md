---
title: Setting up a development QEmu VM on Linux with nested virtualization for Windows 11 with WSL2
date: 2024-03-14
slug: dev-qemu-windows
status: published
---

I exclusively run Linux at home, and needed a Windows VM for building the
[virtual pinball suite](https://github.com/vpinball/vpinball)
and other software that required me to use the Windows Subsystem for Linux
(WSL2).

## Virtualbox vs QEmu

I initially chose Virtualbox for simplicity but never managed to install WSL2 on
it. It appears that WSL2 is implemented on top of Windows HyperV technology, and
it thus requires nested virtualization features to be used inside a VM.

Unlike what is announced in official documentation [wsl-virtualbox], it seems
nested virtualization support for HyperV did not make it to the latest 7.0 Virtualbox
release (7.0.14-Debian as of this writing), and thus it was not possible to
install WSL2 [vbox-hyperv]. This might change with the release of 7.1.

```
WslRegisterDistribution failed with error: 0x80370102
Please enable the Virtual Machine Platform Windows feature and ensure virtualization is enabled in the BIOS.
For information please visit https://aka.ms/enablevirtualization
```

This is the opportunity to give a try at QEmu which supports it and promises to
be more efficient with the use of KVM and virtio.

## QEmu setup

I followed the excellent writeup by [raphtlw], for which the steps are equivalent
for Windows 11 (beyond a couple of remaining IDE occurrences that should be
SATA). The most important steps are summarized here and you can refer to
the original page for a detailed explanation with screenshots.

### Dependencies

```
sudo apt-get install qemu-kvm  bridge-utils virt-manager qemu-system virt-viewer spice-vdagent

```

### Regular setup

Before starting the installation process, you will need to download two ISO:

- Windows 11, available on [microsoft website][win11-download]
- [VirtoIO drivers ISO](virtio-iso), that will be needed to setup both virtio
devices which are required during installation (network is indeed mandatory),
and will be mounted as a second CDROM drive.

Create a new VM that will be installed from a ISO file:

- '''CPU, memory''' : I left default settings
- '''disk size''': At least 60GB is recommended as Windows itself will take
around 30GB, and build tools will require an additional 10/20 GB. You should always
be able to extend the partition after installation.
- Create a second CDROM drive in the Storage menu (don't forget to select the
  medium type to CDROM), and point to the downloaded ISO.
- Enable boot from the SATA CDROM in Boot options. You should still be able to
select it via the BIOS menu if the machine does not boot.
- Swtich to virtio driver in both the HDD and the NIC for improved performance.

### Fine-tuning HyperV support

The current setup worked fine until I installed WSL2 and rebooted and got
greeted with the infamous blue screen and the message:
SYSTEM_THREAD_EXCEPTION_NOT_HANDLED, which it never managed to recover.

I found directions in this excellent [writeup from Redpill
Linpro][qemu-redpill], and after a couple of tries with the XML editor in the
"Processor" section of the VM configuration, I managed to boot Windows again
with these settings:

```xml
  <features>
    <acpi/>
    <apic/>
    <pae/>
    <hyperv mode="custom">
      <vpindex state="on"/>
      <synic state="on"/>
    </hyperv>
    <smm state="on"/>
  </features>
  <cpu mode="custom" match="exact" check="partial">
    <model fallback="allow">Broadwell-noTSX-IBRS</model>
    <feature policy="disable" name="hypervisor"/>
    <feature policy="require" name="vmx"/>
  </cpu>
  <clock offset="utc">
    <timer name="rtc" tickpolicy="catchup"/>
    <timer name="pit" tickpolicy="delay"/>
    <timer name="hpet" present="no"/>
    <timer name="hypervclock" present="yes"/>
    <timer name="kvmclock" present="yes"/>
  </clock>
```


I did not try yet to optimize those settings beyond confirming disabling the CPU
passthrough and setting the correct CPU architecture were part of the solution.
The next step would be to dig more into the documentation and/or continue the
trial and error process to find which properties are indeed required, or lead to
the best performance, And as the article says, your results may vary...

As a reference, that was the original configuration proposed by QEmu.

```xml
  <features>
    <acpi/>
    <apic/>
    <hyperv>
      <relaxed state="on"/>
      <vapic state="on"/>
      <spinlocks state="on" retries="8191"/>
    </hyperv>
    <vmport state="off"/>
  </features>
  <cpu mode="host-passthrough"/>
  <clock offset="localtime">
    <timer name="rtc" tickpolicy="catchup"/>
    <timer name="pit" tickpolicy="delay"/>
    <timer name="hpet" present="no"/>
    <timer name="hypervclock" present="yes"/>
  </clock>
```


## Windows 11 installation

You can simply let the installer guide you until you reach the step where you
choose on which disk to install Windows, which should show an empty list.

You need to select the "Load drivers" option, and browse the second CDROM (E:)
to find the correct drivers for your OS and platform (note that sometimes there
is no win11 version but win10 is also fine):
- E:\viostor\w11\amd64 (for disk)
- E:\NetKVM\w11\amd64 (for NIC)
- E:\qxldod\w10\amd64 (for graphic card)

By checking "Hide drivers that are not compatible with this computer's hardware"
you'll ensure that the correct drivers are found. Nothing showing might be a
sign that you forgot for instance to switch a device to virtio.

Further down in the installation process, you won't have the opportunity to load
new drivers through the GUI. You might reach a step where the installer tries to
find a network connection, and gets stuck because there is no network interface.
In such a situation, you can hit Shift+F10 to open a shell, navigate in the
respective folders, and run the following commands;

```
pnputil /add-driver *.inf
pnputil /scan-devices
```

It happened to me that the installer found the network interface but refused to
connect because of no internet connection. Running a ping from the shell
confirmed the issue. In the host, the packets arrived to the bridge but were not
forwarded, likely because of missing iptables rules. The simplest solution is
then to restart libvirtd, that will not affect running VMs:

```
sudo service libvirtd restart
```

## Guest agent and additional drivers

- E:\virtio-win-guest-tools.exe
- [spice-guest-tools][spice], in the Guest / Windows binaries section of the
page, to get advanced features such as copy/paste between the host and guest



## Visual Studio and related tools

You can freely download the [installer online][vstudio] with the community edition.

These are the settings I used for my current use case, in the workloads tab.
They will approximately require 10 additional GB.

```markdown
Web & Cloud
    [ ] ASP.NET and web development
    [ ] Azure development
    [X] Python development, could be useful
    [ ] Node.js developmen
Desktop & Mobile
    [ ] .NET Multi-platform App UI development
    [ ] .NET Desktop development
    [X] Desktop development with C++
    [ ] Universal Windows Platform development
    [ ] Mobile development with C++
Gaming
    [X] Game development with Unity
    [X] Game development with C++
Other toolsets
    [ ] Data storage and processing
    [ ] Data science and analytical applications
    [ ] Visual Studio extension development
    [ ] Office / SharePoint development
    [X] Linux and embedded development with C++
```

Git will be required, and you can find Windows binaries from [the official
webwite][git].

## WSL2

You can install WSL2 directly from the [Microsoft store][wsl-store], and it
seems you can also install a Distribution from there (eg Debian). We will go
through the steps to install it via commandline.

Choose cmd.exe in the start menu, and Run as administrator:

```
wsl --install
```

If you have Windows 11, or a recent enough version of windows 10, you should
already has WSL2. You can confirm with:

```
$ wsl -v
WSL version: 2.1.4.0
Kernel version: 5.15.146.1-2
WSLg version: 1.0.60
MSRDC version: 1.2.5105
Direct3D version: 1.611.1-81528511
DXCore version: 10.0.25131.1002-220531-1700.rs-onecore-base2-hyp
Windows version: 10.0.22631.2861
```

More information can be found in [wslinfo], [wsl1] and [wsl2]. The system will
ask you to reboot your machine.

You can then setup a Linux distribution (eg. Debian) through the following
command:

```
$ wsl --install --distribution Debian

Installing Windows optional component: VirtualMachinePlatform

Deployment Image Servicing and Management tool
Version: 10.0.22621.2792

Image Version: 10.0.22631.2861

Enabling feature(s)
[==========================100.0%==========================]
The operation completed successfully.
The requested operation is successful. Changes will not be effective until the system is rebooted.
Installing: Debian GNU/Linux
Debian GNU/Linux has been installed.
The requested operation is successful. Changes will not be effective until the system is rebooted.

Need to reboot. Installation takes a couple of minutes

```

After choosing a login a password, you should have a linux shell.

## Maintainance

If you even get out of disk space, you can either try to reclaim some space, or
extend the windows image files.

### Reclaim space: Compact OS, virtual memory and hibernation files

You can first try to uninstall useless applications, although the setup we did
has hardly any software installed.

You can reclaim a few GB by compressing system files, following [this
tutorial][win10-footprint], which exploits the "Compact OS" feature of Windows:

- Open Start.
- Search for Command Prompt, right-click the result, and select Run as administrator.
- Type the following command to verify that your system is not already compressed and press Enter:Compact.exe /CompactOS:query
- Type the following command to reduce the size of Windows 10 and apps and press Enter:Compact.exe /CompactOS:always
- Once you completed these steps, Compact OS will begin the compression process, which could take up to 20 minutes.
- You can always revert the changes using the same instructions, but on step No. 4, use this command Compact.exe /CompactOS:never and press Enter.

A further way to gain space is to save on the virtual memory and hibernation
data files:

Open Start.
Search for Command Prompt, right-click the result, and select Run as administrator.
Type the following command to make Hiberfil.sys smaller and press Enter:powercfg /h /type reduced

The above command reduces the size of the hibernation file by 30 percent. If you want to remove the file completely, you can use the

powercfg /h /off
command instead.

If you want to change the hibernation settings back to the full amount, simply follow the same instructions, but on step No. 3, make sure to use this command

powercfg /h /size 100

### Extending the QEMU image size

Augment the qemu image size

While the host if down:

```
sudo qemu-img resize /var/lib/libvirt/images/win11.qcow2 +10G
```

You can then directly use Windows' Disk Manager to extend the filesystem over
the newly available space.

I could not manage to move the other system partition sitting in between my C
drive and unallocated space.

sudo modprobe nbd max_part=16
sudo qemu-nbd -c /dev/nbd0  /var/lib/libvirt/images/win11.qcow2

kde partition manager does not see the additional 10G
gparted does, but raises the following warning:
Not all of the space available to /dev/nbd0 appears to be used, you can fix the GPT to use all of the space (an extra 20971520 blocks) or continue with the current setting?

Once repaired it is okay in kde partition manager too.

sudo gparted /dev/nbd0

sudo qemu-nbd -d /dev/nbd0

## References


[wsl-virtualbox]: https://learn.microsoft.com/en-us/windows/wsl/faq#will-i-be-able-to-run-wsl-2-and-other-3rd-party-virtualization-tools-such-as-vmware--or-virtualbox-

[vbox-hyperv]: https://forums.virtualbox.org/viewtopic.php?t=110039

[raphtlw]: How to set up a KVM / QEMU Windows 10 VM, by Raphael
https://raphtlw.medium.com/how-to-set-up-a-kvm-qemu-windows-10-vm-ca1789411760

[qemu-redpill]: https://www.redpill-linpro.com/techblog/2021/04/07/nested-virtualization-hyper-v-in-qemu-kvm.html


[w11-download]: https://www.microsoft.com/software-download/windows11

[virtio-iso]: Virtio Drivers ISO
https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/archive-virtio/?C=M;O=D
https://pve.proxmox.com/wiki/Windows_VirtIO_Drivers

[spice]: https://www.spice-space.org/download.html

[vstudio]: https://visualstudio.microsoft.com/downloads/

[git]: https://git-scm.com/download/win


[wslstore]
https://aka.ms/wslstorepage

[wslinfo]
https://aka.ms/wslstoreinfo

[wsl1]
https://support.microsoft.com/fr-fr/windows/activer-la-virtualisation-sur-windows-11-pc-c5578302-6e43-4b4b-a449-8ced115f58e1

[wsl2]
https://learn.microsoft.com/fr-fr/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package

[win10-footprint]
https://www.windowscentral.com/how-reduce-windows-10-footprint-your-pc





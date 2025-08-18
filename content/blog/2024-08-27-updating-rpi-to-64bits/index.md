migration to bookworm from bullseye
https://thierrytalbert.fr/2023/10/13/raspios-de-bullseye-a-bookworm/

for homeassistant-supervised

------------------------------------------

gromit@home:~ $ dpkg --print-architecture
armhf

gromit@home:~ $ uname -a
Linux home 5.10.103-v7l+ #1529 SMP Tue Mar 8 12:24:00 GMT 2022 armv7l GNU/Linux

many things are not available anymore for 32bit systems (eg linuxservers.io)
power and efficiency

sudo apt update; sudo apt dist-upgrade

gromit@home:~ $ sudo su
[sudo] password for gromit:
root@home:/home/gromit# sudo rpi-update
 *** Raspberry Pi firmware updater by Hexxeh, enhanced by AndrewS and Dom
 *** Performing self-update
 *** Relaunching after update
 *** Raspberry Pi firmware updater by Hexxeh, enhanced by AndrewS and Dom
FW_REV:a0d314ac077cda7cbacee1850e84a57af9919f94
BOOTLOADER_REV:ef2fc67d235d037b2b468813e646e20890fcea07
rpi-eeprom firmware package appears to be too old. Skipping bootloader updates
WANT_32BIT:1 WANT_64BIT:1 WANT_PI4:1 WANT_PI5:0
##############################################################
WARNING: This update bumps to rpi-6.6.y linux tree
See: https://forums.raspberrypi.com/viewtopic.php?p=2191175

'rpi-update' should only be used if there is a specific
reason to do so - for example, a request by a Raspberry Pi
engineer or if you want to help the testing effort
and are comfortable with restoring if there are regressions.

DO NOT use 'rpi-update' as part of a regular update process.
##############################################################
Would you like to proceed? (y/N)
 *** Downloading specific firmware revision (this will take a few minutes)
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100  128M    0  128M    0     0  4638k      0 --:--:--  0:00:28 --:--:-- 2570k
100  143M    0  143M    0     0  2965k      0 --:--:--  0:00:49 --:--:-- 1084k
 *** Updating firmware
 *** Updating kernel modules
 *** depmod 6.6.47-v8+
 *** depmod 6.6.47+
 *** depmod 6.6.47-v7l+
 *** depmod 6.6.47-v8-16k+
 *** depmod 6.6.47-v7+
 *** Updating VideoCore libraries
 *** Running ldconfig
 *** Storing current firmware revision
 *** Deleting downloaded files
 *** Syncing changes to disk
 *** If no errors appeared, your firmware was successfully updated to a0d314ac077cda7cbacee1850e84a57af9919f94
 *** A reboot is needed to activate the new firmware


------------------------------------------


TODO:
eeprom
apt packages

------------------------------------------

cross grading

                                                                           ┌──────────────────────────┤ Samba server and utilities ├───────────────────────────┐
                                                                           │                                                                                   │ 
                                                                           │ Line by line differences between versions                                         │ 
                                                                           │                                                                                   │ 
                                                                           │ --- /etc/samba/smb.conf root.root 0644 2024-08-27 01:04:29                        │ 
                                                                           │ +++ /run/samba/upgrades/smb.conf root.root 0644 2024-08-27 01:04:29               │ 
                                                                           │ @@ -23,9 +23,6 @@                                                                 │ 
                                                                           │                                                                                   │ 
                                                                           │  [global]                                                                         │ 
                                                                           │                                                                                   │ 
                                                                           │ - min protocol = SMB2                                                             │ 
                                                                           │ -                                                                                 │ 
                                                                           │ -                                                                                 │ 
                                                                           │  ## Browsing/Identification ###                                                   │ 
                                                                           │                                                                                   │ 
                                                                           │  # Change this to the workgroup/NT-domain name your Samba server will part of     │ 
                                                                           │ @@ -102,8 +99,8 @@                                                                │ 
                                                                           │  ########## Domains ###########                                                   │ 
                                                                           │                                                                                   │ 
                                                                           │  #                                                                                │ 
                                                                           │ -# The following settings only takes effect if 'server role = primary             │ 
                                                                           │ -# classic domain controller', 'server role = backup domain controller'           │ 
                                                                           │ +# The following settings only takes effect if 'server role = classic             │ 
                                                                           │ +# primary domain controller', 'server role = classic backup domain controller'   │ 
                                                                           │  # or 'domain logons' is set                                                      │ 
                                                                           │  #                                                                                │ 
                                                                           │                                                                                   │ 
                                                                           │ @@ -131,7 +128,7 @@                                                               │ 
                                                                           │  # This allows Unix users to be created on the domain controller via the SAMR     │ 
                                                                           │  # RPC pipe. The example command creates a user account with a disabled Unix      │ 
                                                                           │  # password; please adapt to your needs                                           │ 
                                                                           │ -; add user script = /usr/sbin/adduser --quiet --disabled-password --gecos "" %u  │ 
                                                                           │ +; add user script = /usr/sbin/useradd --create-home %u                           │ 
                                                                           │                                                                                   │ 
                                                                           │  # This allows machine accounts to be created on the domain controller via the    │ 
                                                                           │  # SAMR RPC pipe.                                                                 │ 
                                                                           │ @@ -216,7 +213,7 @@                                                               │ 
                                                                           │  [printers]                                                                       │ 
                                                                           │  comment = All Printers                                                           │ 
                                                                           │  browseable = no                                                                  │ 
                                                                           │ - path = /var/spool/samba                                                         │ 
                                                                           │ + path = /var/tmp                                                                 │ 
                                                                           │  printable = yes                                                                  │ 
                                                                           │  guest ok = no                                                                    │ 
                                                                           │  read only = yes     


References:
https://makerhelp.fr/comment-mettre-a-jour-le-firmware-dun-raspberry-pi/








jellyfin: 

/usr/bin/jellyfin --ffmpeg=/usr/lib/jellyfin-ffmpeg/ffmpeg -w /usr/share/jellyfin/web

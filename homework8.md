### 1. Imagine you was asked to add new partition to your host for backup purposes. To simulate appearance of new physical disk in your server, please create new disk in Virtual Box (5 GB) and attach it to your virtual machine.
Also imagine your system started experiencing RAM leak in one of the applications, thus while developers try to debug and fix it, you need to mitigate OutOfMemory errors; you will do it by adding some swap space.
/dev/sdc - 5GB disk, that you just attached to the VM (in your case it may appear as /dev/sdb, /dev/sdc or other, it doesn't matter)

```bash
[student@localhost ~]$ lsblk -o "NAME,MAJ:MIN,RM,SIZE,RO,FSTYPE,MOUNTPOINT,UUID"
NAME            MAJ:MIN RM  SIZE RO FSTYPE      MOUNTPOINT UUID
sda               8:0    0    8G  0                        
|-sda1            8:1    0    1G  0 xfs         /boot      ff4827fa-9410-47dc-a3bd-cae701b1d44b
`-sda2            8:2    0    7G  0 LVM2_member            Ag4vks-pRHq-64WV-b5y3-VcxG-3Vwo-Qa1WwN
  |-centos-root 253:0    0  6.2G  0 xfs         /          28142071-6b47-4036-8aba-a300a0dbe61e
  `-centos-swap 253:1    0  820M  0 swap        [SWAP]     fb44c106-ef06-434a-ba0f-2ca459ec1a99
sdb               8:16   0    5G  0                        
sr0              11:0    1 1024M  0 
```
#### 1.1. Create a 2GB   !!! GPT !!!   partition on /dev/sdc of type "Linux filesystem" (means all the following partitions created in the following steps on /dev/sdc will be GPT as well)
```bash
[student@localhost ~]$ sudo parted /dev/sdb mklabel gpt && sudo parted /dev/sdb mkpart "Linux_filesystem" xfs 0 2095
```

```bash
[student@localhost ~]$ lsblk -o "NAME,MAJ:MIN,RM,SIZE,RO,FSTYPE,MOUNTPOINT,UUID"
NAME            MAJ:MIN RM  SIZE RO FSTYPE      MOUNTPOINT UUID
sda               8:0    0    8G  0                        
|-sda1            8:1    0    1G  0 xfs         /boot      ff4827fa-9410-47dc-a3bd-cae701b1d44b
`-sda2            8:2    0    7G  0 LVM2_member            Ag4vks-pRHq-64WV-b5y3-VcxG-3Vwo-Qa1WwN
  |-centos-root 253:0    0  6.2G  0 xfs         /          28142071-6b47-4036-8aba-a300a0dbe61e
  `-centos-swap 253:1    0  820M  0 swap        [SWAP]     fb44c106-ef06-434a-ba0f-2ca459ec1a99
sdb               8:16   0    5G  0                        
`-sdb1            8:17   0    2G  0 xfs                    952a56ca-09ea-4e85-ada1-38b7016fcb2c
sr0              11:0    1 1024M  0                        

```
#### 1.2. Create a 512MB partition on /dev/sdc of type "Linux swap"
```bash
sudo parted /dev/sdb mkpart "Linux_swap" linux-swap  2096 2633
```
```bash 
[student@localhost ~]$ lsblk -o "NAME,MAJ:MIN,RM,SIZE,RO,FSTYPE,MOUNTPOINT,UUID"
NAME            MAJ:MIN RM  SIZE RO FSTYPE      MOUNTPOINT UUID
sda               8:0    0    8G  0                        
|-sda1            8:1    0    1G  0 xfs         /boot      ff4827fa-9410-47dc-a3bd-cae701b1d44b
`-sda2            8:2    0    7G  0 LVM2_member            Ag4vks-pRHq-64WV-b5y3-VcxG-3Vwo-Qa1WwN
  |-centos-root 253:0    0  6.2G  0 xfs         /          28142071-6b47-4036-8aba-a300a0dbe61e
  `-centos-swap 253:1    0  820M  0 swap        [SWAP]     fb44c106-ef06-434a-ba0f-2ca459ec1a99
sdb               8:16   0    5G  0                        
|-sdb1            8:17   0    2G  0 xfs                    952a56ca-09ea-4e85-ada1-38b7016fcb2c
`-sdb2            8:18   0  512M  0                        
sr0              11:0    1 1024M  0           
```
#### 1.3. Format the 2GB partition with an XFS file system
```bash
sudo mkfs.xfs -f /dev/sdb1
```
#### 1.4. Initialize 512MB partition as swap space
```bash
[student@localhost ~]$ sudo mkswap /dev/sdb2
Setting up swapspace version 1, size = 524284 KiB
no label, UUID=b932d823-74b7-44ec-bd93-a2de693bd163
swapon /dev/sdb2
[student@localhost ~]$ sudo swapon /dev/sdb2
```
#### 1.5. Configure the newly created XFS file system to persistently mount at /backup
```bash
[student@localhost ~]$ sudo mkdir backup && sudo mount /dev/sdb1 /backup
[student@localhost ~]$ lsblk -o "NAME,MAJ:MIN,RM,SIZE,RO,FSTYPE,MOUNTPOINT,UUID"
NAME            MAJ:MIN RM  SIZE RO FSTYPE      MOUNTPOINT UUID
sda               8:0    0    8G  0                        
|-sda1            8:1    0    1G  0 xfs         /boot      ff4827fa-9410-47dc-a3bd-cae701b1d44b
`-sda2            8:2    0    7G  0 LVM2_member            Ag4vks-pRHq-64WV-b5y3-VcxG-3Vwo-Qa1WwN
  |-centos-root 253:0    0  6.2G  0 xfs         /          28142071-6b47-4036-8aba-a300a0dbe61e
  `-centos-swap 253:1    0  820M  0 swap        [SWAP]     fb44c106-ef06-434a-ba0f-2ca459ec1a99
sdb               8:16   0    5G  0                        
|-sdb1            8:17   0    2G  0 xfs         /backup    1032d10c-90f9-48ae-a284-461bc5753807
`-sdb2            8:18   0  512M  0 swap        [SWAP]     b932d823-74b7-44ec-bd93-a2de693bd163
sr0              11:0    1 1024M  0                      
```
#### 1.6. Configure the newly created swap space to be enabled at boot
```bash
sudo vi /etc/fstab 
UUID=1032d10c-90f9-48ae-a284-461bc5753807 /backup xfs default 0 0
UUID=b932d823-74b7-44ec-bd93-a2de693bd163 swap swap defaults 0 0
```
#### 1.7. Reboot your host and verify that /dev/sdc1 is mounted at /backup and that your swap partition  (/dev/sdc2) is enabled
```bash
[student@localhost ~]$ lsblk -o "NAME,MAJ:MIN,RM,SIZE,RO,FSTYPE,MOUNTPOINT,UUID"
NAME            MAJ:MIN RM  SIZE RO FSTYPE      MOUNTPOINT UUID
sda               8:0    0   10G  0                        
|-sda1            8:1    0    1G  0 xfs         /boot      c7ba9e12-2b13-4234-924c-6179bb4c0c39
`-sda2            8:2    0    9G  0 LVM2_member            BTnDrB-h1MA-LbiH-JR5Z-18OH-TCTp-PN1dba
  |-centos-root 253:0    0    8G  0 xfs         /          1365866b-9ae0-40ba-9351-764295026de8
  `-centos-swap 253:1    0    1G  0 swap        [SWAP]     63499df3-2082-49f2-b54a-0318f10db513
sdb               8:16   0    5G  0                        
|-sdb1            8:17   0    2G  0 xfs         /backup    1032d10c-90f9-48ae-a284-461bc5753807
`-sdb2            8:18   0  512M  0 swap        [SWAP]     b932d823-74b7-44ec-bd93-a2de693bd163
sr0              11:0    1 1024M  0                        

...
(parted) print                                                            
Model: ATA VBOX HARDDISK (scsi)
Disk /dev/sdb: 5369MB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags: 

Number  Start   End     Size    File system     Name              Flags
 1      17.4kB  2095MB  2095MB  xfs             Linux_filesystem
 2      2096MB  2633MB  537MB   linux-swap(v1)  Linux_swap


```

### 2. LVM. Imagine you're running out of space on your root device. As we found out during the lesson default CentOS installation should already have LVM, means you can easily extend size of your root device. So what are you waiting for? Just do it!
#### 2.1. Create 2GB partition on /dev/sdc of type "Linux LVM"
```bash
sudo parted /dev/sdb mkpart "Linux_LVM" xfs 2633 4733
[student@localhost ~]$ lsblk -o "NAME,MAJ:MIN,RM,SIZE,RO,FSTYPE,MOUNTPOINT,UUID"
NAME            MAJ:MIN RM  SIZE RO FSTYPE      MOUNTPOINT UUID
sda               8:0    0   10G  0                        
|-sda1            8:1    0    1G  0 xfs         /boot      c7ba9e12-2b13-4234-924c-6179bb4c0c39
`-sda2            8:2    0    9G  0 LVM2_member            BTnDrB-h1MA-LbiH-JR5Z-18OH-TCTp-PN1dba
  |-centos-root 253:0    0    8G  0 xfs         /          1365866b-9ae0-40ba-9351-764295026de8
  `-centos-swap 253:1    0    1G  0 swap        [SWAP]     63499df3-2082-49f2-b54a-0318f10db513
sdb               8:16   0    5G  0                        
|-sdb1            8:17   0    2G  0 xfs         /backup    beb806fe-f07c-495f-9a94-532f97dc9716
|-sdb2            8:18   0  512M  0 swap        [SWAP]     21979ade-ac3d-416d-bcd4-ff3ff9eb9dd3
`-sdb3            8:19   0    2G  0                        
sr0              11:0    1 1024M  0                        
```
#### 2.2. Initialize the partition as a physical volume (PV)
```bash
[student@localhost ~]$ sudo pvcreate /dev/sdb3
WARNING: xfs signature detected on /dev/sdb3 at offset 0. Wipe it? [y/n]: y
  Wiping xfs signature on /dev/sdb3.
  Physical volume "/dev/sdb3" successfully created.

[student@localhost ~]$ sudo pvs
  PV         VG     Fmt  Attr PSize  PFree 
  /dev/sda2  centos lvm2 a--  <9.00g     0 
  /dev/sdb3         lvm2 ---  <1.96g <1.96g
```
#### 2.3. Extend the volume group (VG) of your root device using your newly created PV
```bash
[student@localhost ~]$ sudo vgextend centos /dev/sdb3
  Volume group "centos" successfully extended
[student@localhost ~]$ sudo vgs
  VG     #PV #LV #SN Attr   VSize   VFree
  centos   2   2   0 wz--n- <10.95g 1.95g

```
#### 2.4. Extend your root logical volume (LV) by 1GB, leaving other 1GB unassigned
```bash
[student@localhost ~]$ sudo lvextend -l+50%FREE /dev/centos/root
  Size of logical volume centos/root changed from <8.00 GiB (2047 extents) to 8.97 GiB (2297 extents).
  Logical volume centos/root successfully resized.
```
#### 2.5. Check current disk space usage of your root device
```bash
lsblk -o "NAME,MAJ:MIN,RM,SIZE,RO,FSTYPE,MOUNTPOINT,UUID"
NAME            MAJ:MIN RM  SIZE RO FSTYPE      MOUNTPOINT UUID
sda               8:0    0   10G  0                        
|-sda1            8:1    0    1G  0 xfs         /boot      c7ba9e12-2b13-4234-924c-6179bb4c0c39
`-sda2            8:2    0    9G  0 LVM2_member            BTnDrB-h1MA-LbiH-JR5Z-18OH-TCTp-PN1dba
  |-centos-root 253:0    0    9G  0 xfs         /          1365866b-9ae0-40ba-9351-764295026de8
  `-centos-swap 253:1    0    1G  0 swap        [SWAP]     63499df3-2082-49f2-b54a-0318f10db513
sdb               8:16   0    5G  0                        
|-sdb1            8:17   0    2G  0 xfs         /backup    beb806fe-f07c-495f-9a94-532f97dc9716
|-sdb2            8:18   0  512M  0 swap        [SWAP]     21979ade-ac3d-416d-bcd4-ff3ff9eb9dd3
`-sdb3            8:19   0    2G  0 LVM2_member            72N6yc-W3hU-xzvq-GsB3-LMzE-qX8m-AgZnua
  `-centos-root 253:0    0    9G  0 xfs         /          1365866b-9ae0-40ba-9351-764295026de8
sr0              11:0    1 1024M  0       
```
#### 2.6. Extend your root device filesystem to be able to use additional free space of root LV
```bash
sudo lvextend -l+100%FREE /dev/centos/root
  Size of logical volume centos/root changed from 8.97 GiB (2297 extents) to <9.95 GiB (2547 extents).
  Logical volume centos/root successfully resized.
[student@localhost ~]$ lsblk -o "NAME,MAJ:MIN,RM,SIZE,RO,FSTYPE,MOUNTPOINT,UUID"
NAME            MAJ:MIN RM  SIZE RO FSTYPE      MOUNTPOINT UUID
sda               8:0    0   10G  0                        
|-sda1            8:1    0    1G  0 xfs         /boot      c7ba9e12-2b13-4234-924c-6179bb4c0c39
`-sda2            8:2    0    9G  0 LVM2_member            BTnDrB-h1MA-LbiH-JR5Z-18OH-TCTp-PN1dba
  |-centos-root 253:0    0   10G  0 xfs         /          1365866b-9ae0-40ba-9351-764295026de8
  `-centos-swap 253:1    0    1G  0 swap        [SWAP]     63499df3-2082-49f2-b54a-0318f10db513
sdb               8:16   0    5G  0                        
|-sdb1            8:17   0    2G  0 xfs         /backup    beb806fe-f07c-495f-9a94-532f97dc9716
|-sdb2            8:18   0  512M  0 swap        [SWAP]     21979ade-ac3d-416d-bcd4-ff3ff9eb9dd3
`-sdb3            8:19   0    2G  0 LVM2_member            72N6yc-W3hU-xzvq-GsB3-LMzE-qX8m-AgZnua
  `-centos-root 253:0    0   10G  0 xfs         /          1365866b-9ae0-40ba-9351-764295026de8
sr0              11:0    1 1024M  0 
```
#### 2.7. Verify that after reboot your root device is still 1GB bigger than at 2.5.
```bash 
[student@localhost ~]$ lsblk -o "NAME,MAJ:MIN,RM,SIZE,RO,FSTYPE,MOUNTPOINT,UUID"
NAME            MAJ:MIN RM  SIZE RO FSTYPE      MOUNTPOINT UUID
sda               8:0    0   10G  0                        
|-sda1            8:1    0    1G  0 xfs         /boot      c7ba9e12-2b13-4234-924c-6179bb4c0c39
`-sda2            8:2    0    9G  0 LVM2_member            BTnDrB-h1MA-LbiH-JR5Z-18OH-TCTp-PN1dba
  |-centos-root 253:0    0   10G  0 xfs         /          1365866b-9ae0-40ba-9351-764295026de8
  `-centos-swap 253:1    0    1G  0 swap        [SWAP]     63499df3-2082-49f2-b54a-0318f10db513
sdb               8:16   0    5G  0                        
|-sdb1            8:17   0    2G  0 xfs         /backup    beb806fe-f07c-495f-9a94-532f97dc9716
|-sdb2            8:18   0  512M  0 swap        [SWAP]     21979ade-ac3d-416d-bcd4-ff3ff9eb9dd3
`-sdb3            8:19   0    2G  0 LVM2_member            72N6yc-W3hU-xzvq-GsB3-LMzE-qX8m-AgZnua
  `-centos-root 253:0    0   10G  0 xfs         /          1365866b-9ae0-40ba-9351-764295026de8
sr0              11:0    1 1024M  0   

```

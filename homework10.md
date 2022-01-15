####  Boot process

##### 1. enable recovery options for grub, update main configuration file and find new item in grub2 config in /boot.
```
sudo vi /etc/default/grub
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

```
[student@localhost ~]$ ll /boot/
total 112096
-rw-------. 1 root root  3616707 Oct 19  2020 System.map-3.10.0-1160.el7.x86_64
-rw-r--r--. 1 root root   153591 Oct 19  2020 config-3.10.0-1160.el7.x86_64
drwxr-xr-x. 3 root root       17 Jan  9 23:23 efi
drwxr-xr-x. 2 root root       27 Jan  9 23:24 grub
drwx------. 5 root root       97 Jan 10 10:50 grub2
-rw-------. 1 root root 62126094 Jan  9 23:27 initramfs-0-rescue-1885f95ab4cffa4493dbf83326a78be8.img
-rw-------. 1 root root 21475322 Jan  9 23:29 initramfs-3.10.0-1160.el7.x86_64.img
-rw-------. 1 root root 13543606 Jan  9 23:42 initramfs-3.10.0-1160.el7.x86_64kdump.img
-rw-r--r--. 1 root root   320648 Oct 19  2020 symvers-3.10.0-1160.el7.x86_64.gz
-rwxr-xr-x. 1 root root  6769256 Jan  9 23:27 vmlinuz-0-rescue-1885f95ab4cffa4493dbf83326a78be8
-rwxr-xr-x. 1 root root  6769256 Oct 19  2020 vmlinuz-3.10.0-1160.el7.x86_64
```
##### 2. modify option vm.dirty_ratio:

######   - using echo utility
   ```
su root
echo 40 >  /proc/sys/vm/dirty_ratio
```
######   - using sysctl utility
```
sudo sysctl vm.dirty_ratio = 32
```
######   - using sysctl configuration files
```
sudo vi /etc/sysctl.conf
vm.dirty_ratio = 80
sysctl -p
```

### Selinux

#### Disable selinux using kernel cmdline

```
Ctrl+X  --> e
...
root (hd0,0)
    kernel *** selinux=0
    initrd /initramfs-3.10.1160.el7.x86_64.img
...

```
#### Firewalls
##### 1. Add rule using firewall-cmd that will allow SSH access to your server *only* from network 192.168.56.0/24 and interface enp0s8 (if your network and/on interface name differs - change it accordingly).

```bash

sudo firewall-cmd --zone=internal --add-source=192.168.56.0/24
sudo firewall-cmd --zone=public --remove-service=ssh
```

##### 2. Shutdown firewalld and add the same rules via iptables.

```bash
iptables -A INPUT -i enp0s8 -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A INPUT -i enp0s8 -p tcp -s 192.168.56.0/24 --dport 22 -j ACCEPT
iptables -A INPUT -i enp0s8 -j DROP
iptables -A INPUT -i enp0s3 -j DROP
```

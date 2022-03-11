## Repositories and Packages

### Use rpm for the following tasks:
#### 1. Download sysstat package.
```
sudo yum install yum-utils
yumdownloader sysstat
```
#### 2. Get information from downloaded sysstat package file.
```
[student@localhost ~]$ rpm -qip sysstat-10.1.5-19.el7.x86_64.rpm
Name        : sysstat
Version     : 10.1.5
Release     : 19.el7
Architecture: x86_64
Install Date: (not installed)
Group       : Applications/System
Size        : 1172488
License     : GPLv2+
Signature   : RSA/SHA256, Sat Apr  4 00:08:48 2020, Key ID 24c6a8a7f4a80eb5
Source RPM  : sysstat-10.1.5-19.el7.src.rpm
Build Date  : Wed Apr  1 07:36:37 2020
Build Host  : x86-01.bsys.centos.org
Relocations : (not relocatable)
Packager    : CentOS BuildSystem <http://bugs.centos.org>
Vendor      : CentOS
URL         : http://sebastien.godard.pagesperso-orange.fr/
Summary     : Collection of performance monitoring tools for Linux
Description :
The sysstat package contains sar, sadf, mpstat, iostat, pidstat, nfsiostat-sysstat,
tapestat, cifsiostat and sa tools for Linux.
...
```
#### 3. Install sysstat package and get information about files installed by this package.
```

[student@localhost ~]$ sudo rpm -ivh sysstat-10.1.5-19.el7.x86_64.rpm --nodeps
[student@localhost ~]$ rpm -ql sysstat
/etc/cron.d/sysstat
/etc/sysconfig/sysstat
/etc/sysconfig/sysstat.ioconf
/usr/bin/cifsiostat
/usr/bin/iostat
/usr/bin/mpstat
/usr/bin/nfsiostat-sysstat
/usr/bin/pidstat
...
```
###  Add NGINX repository (need to find repository config on https://www.nginx.com/) and complete the following tasks using yum:

```
sudo yum install nginx
```
1. Check if NGINX repository enabled or not.
/etc/yum.repos.d/nginx.repo
```
[nginx-stable]
name=nginx stable repo
baseurl=http://nginx.org/packages/centos/$releasever/$basearch/
gpgcheck=1
enabled=1
gpgkey=https://nginx.org/keys/nginx_signing.key
module_hotfixes=true

[nginx-mainline]
name=nginx mainline repo
baseurl=http://nginx.org/packages/mainline/centos/$releasever/$basearch/
gpgcheck=1
enabled=0
gpgkey=https://nginx.org/keys/nginx_signing.key
module_hotfixes=true
```
```
sudo yum-config-manager --enable nginx-stable
yum repolist enabled |grep "nginx*"
```
2. Install NGINX.
```
sudo yum install nginx
```
3. Check yum history and undo NGINX installation.
```
sudo yum history list
Failed to set locale, defaulting to C
Loaded plugins: fastestmirror
ID     | Login user               | Date and time    | Action(s)      | Altered
-------------------------------------------------------------------------------
     3 | student <student>        | 2021-12-23 22:42 | Install        |    1 E<
     2 | student <student>        | 2021-12-23 22:13 | I, U           |    5 >
     1 | System <unset>           | 2021-12-23 21:53 | Install        |  299   
history list

```

```
[student@localhost ~]$ sudo yum history info  3
Failed to set locale, defaulting to C
Loaded plugins: fastestmirror
Transaction ID : 3
Begin time     : Thu Dec 23 22:42:36 2021
Begin rpmdb    : 304:127c3f9ee1f3b98766af543983233381ec3ce2f0
End time       :            22:42:37 2021 (1 seconds)
End rpmdb      : 305:c138964bf49c8043af01fd9d1fea696b962f4711
User           : student <student>
Return-Code    : Success
Command Line   : install nginx
Transaction performed with:
    Installed     rpm-4.11.3-45.el7.x86_64                        @anaconda
    Installed     yum-3.4.3-168.el7.centos.noarch                 @anaconda
    Installed     yum-plugin-fastestmirror-1.1.31-54.el7_8.noarch @anaconda
Packages Altered:
    Install nginx-1:1.21.4-1.el7.ngx.x86_64 @nginx-mainline
Rpmdb Problems:
    requires: sysstat-10.1.5-19.el7.x86_64 has missing requires of libsensors.so.4()(64bit)
        Installed     sysstat-10.1.5-19.el7.x86_64 installed
Scriptlet output:
   1 ----------------------------------------------------------------------
   2
   3 Thanks for using nginx!
   4
   5 Please find the official documentation for nginx here:
   6 * https://nginx.org/en/docs/
   7
   8 Please subscribe to nginx-announce mailing list to get
   9 the most important news about nginx:
  10 * https://nginx.org/en/support.html
  11
  12 Commercial subscriptions for nginx are available on:
  13 * https://nginx.com/products/
  14
  15 ----------------------------------------------------------------------
history info

```
```
sudo yum history undo 3

```
4. Disable NGINX repository.
```
sudo yum-config-manager --disable nginx-\*

```
5. Remove sysstat package installed in the first task.
```
yum remove sysstat
```
6. Install EPEL repository and get information about it.
```
sudo yum install epel-release
```
```
sudo yum search epel-release
Failed to set locale, defaulting to C
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
epel/x86_64/metalink                                                  |  33 kB  00:00:00     
 * base: mirror.awanti.com
 * epel: mirror.nsc.liu.se
 * extras: mirror.axelname.ru
 * updates: mirror.awanti.com
epel                                                                  | 4.7 kB  00:00:00     
(1/3): epel/x86_64/group_gz                                           |  96 kB  00:00:00     
(2/3): epel/x86_64/primary_db                                         | 7.0 MB  00:00:01     
(3/3): epel/x86_64/updateinfo                                         | 1.0 MB  00:00:07     
================================= N/S matched: epel-release =================================
epel-release.noarch : Extra Packages for Enterprise Linux repository configuration

  Name and summary matches only, use "search all" for everything.
```
7. Find how much packages provided exactly by EPEL repository.
```
sudo yum repo-pkgs epel list
```

8. Install ncdu package from EPEL repo.
```
 sudo yum repo-pkgs epel list | grep ncdu

```

### *Extra task:
   #### Need to create an rpm package consists of a shell script and a text file. The script should output words count stored in file.
    
```
yum install rpm-build rpmdevtools
rpmdev-setuptree
cd ~/rpmbuild/SOURCES
```
script.sh
```
#!/bin/sh
cd "$(dirname "${BASH_SOURCE[0]}")"
cat text.txt | wc -w 
```
text.txt
```
New FIA president Mohammed ben Sulayem has refused to rule out punishing Lewis Hamilton for boycotting its awards ceremony on Thursday.
Hamilton and Mercedes team principal Toto Wolff did not attend in protest at the handling of the Abu Dhabi Grand Prix last Sunday.
Formula 1 rules dictate that the top three drivers in the championship must attend.
"If there is any breach, there is no forgiveness in this," Ben Sulayem said. 
Asked to clarify whether he was saying Hamilton would be penalised for not attending the gala, he said: "Forgiveness is always there. But rules are rules.
"I know Lewis is really sad about what happened. I would say he is broken. 
But we have to look into if there is any breach. [After] a few hours now as president, I cannot give answers without going back to the facts."
Wolff said on Thursday that Hamilton was "disillusioned" after the events of Abu Dhabi and that he could not guarantee the seven-time champion would return to F1 next year.
```
```
tar czf scripttest-1.0.tar.gz scripttest-1
vi  ~/rpmbuild/SPECS/myscripttest.spec

```
myscripttest.spec
```
Name:           scripttest
Version:        1
Release:        0
Summary:        Script

BuildArch:      noarch
License:        GPL
Source0:        scripttest-1.0.tar.gz

%description
It's my script to count words in the file

%prep
%setup -q
%build
%install
install -m 0755 -d $RPM_BUILD_ROOT/etc/scripttest
install -m 0755 text.txt $RPM_BUILD_ROOT/etc/scripttest/text.txt
install -m 0755 script.sh $RPM_BUILD_ROOT/etc/scripttest/script.sh

%files
/etc/scripttest
/etc/scripttest/text.txt
/etc/scripttest/script.sh

%changelog
* Fri Dec 24 2021 Evgenii Momot
-Initial rpm release
```
```
[student@localhost ~]$ rpmbuild -ba ~/rpmbuild/SPECS/myscripttest.spec
[student@localhost ~]$ cd /home/student/rpmbuild/RPMS/noarch/
[student@localhost ~]$ rpm -qip scripttest-1-0.noarch.rpm 
Name        : scripttest
Version     : 1
Release     : 0
Architecture: noarch
Install Date: (not installed)
Group       : Unspecified
Size        : 1043
License     : GPL
Signature   : (none)
Source RPM  : scripttest-1-0.src.rpm
Build Date  : Fri Dec 24 17:41:18 2021
Build Host  : localhost
Relocations : (not relocatable)
Packager    : scripttest
Summary     : Script
Description :
It's my script to count words in the file
```
```
[student@localhost ~]$ rpm -qi scripttest
Name        : scripttest
Version     : 1
Release     : 0
Architecture: noarch
Install Date: Fri Dec 24 17:44:27 2021
Group       : Unspecified
Size        : 1043
License     : GPL
Signature   : (none)
Source RPM  : scripttest-1-0.src.rpm
Build Date  : Fri Dec 24 17:41:18 2021
Build Host  : localhost
Relocations : (not relocatable)
Packager    : scripttest
Summary     : Script
Description :
It's my script to count words in the file
```
```
[student@localhost ~]$ tree ~/rpmbuild
/home/student/rpmbuild
|-- BUILD    
|   |   
|   `-- scripttest-1
|       |-- debugfiles.list
|       |-- debuglinks.list
|       |-- debugsources.list
|       |-- elfbins.list
|       |-- script.sh
|       `-- text.txt
|-- BUILDROOT
|-- RPMS
|   `-- noarch
|       `-- scripttest-1-0.noarch.rpm
|-- SOURCES
|   |-- scripttest-1
|   |   |-- script.sh
|   |   `-- text.txt
|   `-- scripttest-1.0.tar.gz
|-- SPECS
|   `-- myscripttest.spec
`-- SRPMS
    `-- scripttest-1-0.src.rpm

10 directories, 14 files

```
```
[student@localhost ~]$ rpm -ql scripttest
/etc/scripttest
/etc/scripttest/script.sh
/etc/scripttest/text.txt
````
### Work with files

#### 1. Find all regular files below 100 bytes inside your home directory.
```
find ~/ -type f -size -100c
./.bash_logout
./rpmbuild/SOURCES/scripttest-1/script.sh
./rpmbuild/BUILD/scripttest/script.sh
./rpmbuild/BUILD/scripttest-1/script.sh
./rpmbuild/BUILD/scripttest-1/debugsources.list
./rpmbuild/BUILD/scripttest-1/debugfiles.list
./rpmbuild/BUILD/scripttest-1/debuglinks.list
./rpmbuild/BUILD/scripttest-1/elfbins.list
./stdout
./stderr
./.lesshst

```
#### 2. Find an inode number and a hard links count for the root directory. The hard link count should be about 17. Why?
```
ls -ali /
```
```
[student@localhost ~]$ ls -ali / &&  ls -la /etc/
total 16
      64 dr-xr-xr-x.  17 root root  224 Dec 23 22:05 .
      64 dr-xr-xr-x.  17 root root  224 Dec 23 22:05 ..
...

```
```..``` указывает на своего родителя. 
```.``` указывает на сам каталог, то есть на самого себя. 
Каждый новый каталог добавляет ссылку при создании в корневом каталоге.

#### 3. Check what inode numbers have "/" and "/boot" directory. Why?

```
ls -ali / /boot
```
```/``` и ```/boot``` - это разные файловые системы. Номер inode должен быть уникальным только в пределах одной файловой системы.
```
[student@localhost ~]$ df -h
Filesystem               Size  Used Avail Use% Mounted on
...
/dev/mapper/centos-root  6.2G  1.8G  4.5G  28% /
/dev/sda1               1014M  137M  878M  14% /boot
...
```
#### 4. Check the root directory space usage by du command. Compare it with an information from df. If you find differences, try to find out why it happens.
```
df -h /
sudo du -hc / 2> /dev/null | tail  -n 1
```

#### 5. Check disk space usage of /var/log directory using ncdu
```
ncdu /var/log
```
```
--- /var/log -------------------------------------------------------------------------------------------------------------------
    1.9 MiB [##################] /anaconda                                                                                      
  480.0 KiB [####              ]  dnf.librepo.log
  192.0 KiB [#                 ]  messages
   40.0 KiB [                  ]  dnf.log
   36.0 KiB [                  ]  secure
   32.0 KiB [                  ]  dmesg
   32.0 KiB [                  ]  dmesg.old
   20.0 KiB [                  ]  boot.log-20211224
   12.0 KiB [                  ]  lastlog
   12.0 KiB [                  ]  hawkey.log
   12.0 KiB [                  ]  wtmp
    8.0 KiB [                  ]  tallylog
    8.0 KiB [                  ]  boot.log
    8.0 KiB [                  ]  dnf.rpm.log
    8.0 KiB [                  ]  maillog
    8.0 KiB [                  ]  cron
    4.0 KiB [                  ] /tuned
    4.0 KiB [                  ]  yum.log
    4.0 KiB [                  ]  firewalld
    4.0 KiB [                  ]  grubby_prune_debug
    0.0   B [                  ] /nginx
!   0.0   B [                  ] /audit
e   0.0   B [                  ] /sa
e   0.0   B [                  ] /rhsm
    0.0   B [                  ]  spooler
    0.0   B [                  ]  btmp


```

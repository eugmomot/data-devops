#### 1. add secondary ip address to you second network interface enp0s8. Each point must be presented with commands and showing that new address was applied to the interface. To repeat adding address for points 2 and 3 address must be deleted (please add deleting address to you homework log) Methods:
  ##### 1. using ip utility (stateless)
  ```bash
  [student@localhost ~]$ ip -4 a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 10.0.2.15/24 brd 10.0.2.255 scope global noprefixroute dynamic enp0s3
       valid_lft 86386sec preferred_lft 86386sec
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 192.168.56.102/24 brd 192.168.56.255 scope global noprefixroute dynamic enp0s8
       valid_lft 584sec preferred_lft 584sec
[student@localhost ~]$ sudo ip addr add  192.168.56.101/24 dev enp0s8
[sudo] password for student: 
[student@localhost ~]$ ip -4 a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 10.0.2.15/24 brd 10.0.2.255 scope global noprefixroute dynamic enp0s3
       valid_lft 86343sec preferred_lft 86343sec
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 192.168.56.102/24 brd 192.168.56.255 scope global noprefixroute dynamic enp0s8
       valid_lft 541sec preferred_lft 541sec
    inet 192.168.56.101/24 scope global secondary enp0s8
       valid_lft forever preferred_lft forever
[student@localhost ~]$ sudo ip addr del  192.168.56.101/24 dev enp0s8
[student@localhost ~]$ ip -4 a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 10.0.2.15/24 brd 10.0.2.255 scope global noprefixroute dynamic enp0s3
       valid_lft 86297sec preferred_lft 86297sec
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 192.168.56.102/24 brd 192.168.56.255 scope global noprefixroute dynamic enp0s8
       valid_lft 497sec preferred_lft 497sec
  ```
##### 2. using centos network configuration file (statefull)
  ```bash
sudo vi /etc/sysconfig/network-scripts/ifcfg-enp0s8:1
DEVICE=enp0s8:1
BOOTPROTO=static
IPADDR=192.168.56.101
NETMASK=255.255.255.0
ONBOOT=yes
[student@localhost ~]$ sudo ifup ifcfg-enp0s8:1
[student@localhost ~]$ ip -4 a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 10.0.2.15/24 brd 10.0.2.255 scope global noprefixroute dynamic enp0s3
       valid_lft 86399sec preferred_lft 86399sec
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 192.168.56.102/24 brd 192.168.56.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever
    inet 192.168.56.101/24 brd 192.168.56.255 scope global secondary noprefixroute enp0s8:1
       valid_lft forever preferred_lft forever

[student@localhost ~]$ sudo ifdown ifcfg-enp0s8:1
[student@localhost ~]$ ip -4 a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 10.0.2.15/24 brd 10.0.2.255 scope global noprefixroute dynamic enp0s3
       valid_lft 86371sec preferred_lft 86371sec
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 192.168.56.102/24 brd 192.168.56.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever
[student@localhost ~]$ sudo rm /etc/sysconfig/network-scripts/ifcfg-enp0s8:1

  ```
  

##### 3. using nmcli utility (statefull)
  ```bash
  [student@localhost ~]$ ip -4 a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 10.0.2.15/24 brd 10.0.2.255 scope global noprefixroute dynamic enp0s3
       valid_lft 86310sec preferred_lft 86310sec
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 192.168.56.102/24 brd 192.168.56.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever
[student@localhost ~]$ sudo nmcli dev mod enp0s8 ipv4.method manual ipv4.addresses "192.168.56.102/24,192.168.56.101/24"
Connection successfully reapplied to device 'enp0s8'.
[student@localhost ~]$ sudo nmcli con mod enp0s8 ipv4.method manual ipv4.addresses "192.168.56.102/24,192.168.56.101/24"
[student@localhost ~]$ ip -4 a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 10.0.2.15/24 brd 10.0.2.255 scope global noprefixroute dynamic enp0s3
       valid_lft 86230sec preferred_lft 86230sec
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 192.168.56.102/24 brd 192.168.56.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever
    inet 192.168.56.101/24 brd 192.168.56.255 scope global secondary noprefixroute enp0s8
       valid_lft forever preferred_lft forever
       
[student@localhost ~]$ sudo nmcli dev mod enp0s8 ipv4.method manual ipv4.addresses "192.168.56.102/24"
Connection successfully reapplied to device 'enp0s8'.
[student@localhost ~]$ sudo nmcli con mod enp0s8 ipv4.method manual ipv4.addresses "192.168.56.102/24"
[student@localhost ~]$ ip -4 a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 10.0.2.15/24 brd 10.0.2.255 scope global noprefixroute dynamic enp0s3
       valid_lft 84835sec preferred_lft 84835sec
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 192.168.56.102/24 brd 192.168.56.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever
  ```
#### 2. You should have a possibility to use ssh client to connect to your node using new address from previous step. Run tcpdump in separate tmux session or separate connection before starting ssh client and capture packets that are related to this ssh connection. Find packets that are related to TCP session establish.
```bash
[student@localhost ~]$ sudo tcpdump -vvv -i enp0s8 dst 192.168.56.102
tcpdump: listening on enp0s8, link-type EN10MB (Ethernet), capture size 262144 bytes
tcpdump: listening on enp0s8, link-type EN10MB (Ethernet), capture size 262144 bytes
23:35:57.372334 IP (tos 0x0, ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 64)
    192.168.56.1.60106 > localhost.localdomain.ssh: Flags [SEW], cksum 0xf3d8 (correct), seq 2075345828, win 65535, options [mss 1460,nop,wscale 6,nop,nop,TS val 646545385 ecr 0,sackOK,eol], length 0
23:35:57.372646 IP (tos 0x0, ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.56.1.60106 > localhost.localdomain.ssh: Flags [.], cksum 0xb27e (correct), seq 2075345829, ack 2296074984, win 2058, options [nop,nop,TS val 646545385 ecr 2858465], length 0
23:35:57.372914 IP (tos 0x2,ECT(0), ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 73)
    192.168.56.1.60106 > localhost.localdomain.ssh: Flags [P.], cksum 0xf0b8 (correct), seq 0:21, ack 1, win 2058, options [nop,nop,TS val 646545385 ecr 2858465], length 21
23:35:57.386162 IP (tos 0x0, ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.56.1.60106 > localhost.localdomain.ssh: Flags [.], cksum 0xb23b (correct), seq 21, ack 22, win 2058, options [nop,nop,TS val 646545398 ecr 2858477], length 0
23:35:57.387271 IP (tos 0x2,ECT(0), ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 1444)
    192.168.56.1.60106 > localhost.localdomain.ssh: Flags [P.], cksum 0x9faf (correct), seq 21:1413, ack 22, win 2058, options [nop,nop,TS val 646545399 ecr 2858477], length 1392
23:35:57.390387 IP (tos 0x0, ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.56.1.60106 > localhost.localdomain.ssh: Flags [.], cksum 0xa7d6 (correct), seq 1413, ack 1302, win 2038, options [nop,nop,TS val 646545402 ecr 2858482], length 0
23:35:57.392691 IP (tos 0x2,ECT(0), ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 100)
    192.168.56.1.60106 > localhost.localdomain.ssh: Flags [P.], cksum 0xbb97 (correct), seq 1413:1461, ack 1302, win 2048, options [nop,nop,TS val 646545404 ecr 2858482], length 48
23:35:57.398811 IP (tos 0x0, ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.56.1.60106 > localhost.localdomain.ssh: Flags [.], cksum 0xa625 (correct), seq 1461, ack 1666, win 2042, options [nop,nop,TS val 646545410 ecr 2858491], length 0
23:35:57.403633 IP (tos 0x2,ECT(0), ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 68)
    192.168.56.1.60106 > localhost.localdomain.ssh: Flags [P.], cksum 0x9be2 (correct), seq 1461:1477, ack 1666, win 2048, options [nop,nop,TS val 646545414 ecr 2858491], length 16
23:35:57.486472 IP (tos 0x2,ECT(0), ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 96)
    192.168.56.1.60106 > localhost.localdomain.ssh: Flags [P.], cksum 0xa002 (correct), seq 1477:1521, ack 1666, win 2048, options [nop,nop,TS val 646545482 ecr 2858565], length 44
23:35:57.487061 IP (tos 0x0, ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.56.1.60106 > localhost.localdomain.ssh: Flags [.], cksum 0xa50a (correct), seq 1521, ack 1710, win 2047, options [nop,nop,TS val 646545496 ecr 2858579], length 0
23:35:57.487217 IP (tos 0x2,ECT(0), ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 120)
    192.168.56.1.60106 > localhost.localdomain.ssh: Flags [P.], cksum 0x391d (correct), seq 1521:1589, ack 1710, win 2048, options [nop,nop,TS val 646545496 ecr 2858579], length 68
23:35:57.510063 IP (tos 0x0, ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.56.1.60106 > localhost.localdomain.ssh: Flags [.], cksum 0xa445 (correct), seq 1589, ack 1794, win 2046, options [nop,nop,TS val 646545519 ecr 2858602], length 0
23:35:59.699038 IP (tos 0x2,ECT(0), ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 136)
    192.168.56.1.60106 > localhost.localdomain.ssh: Flags [P.], cksum 0xb055 (correct), seq 1589:1673, ack 1794, win 2048, options [nop,nop,TS val 646547702 ecr 2858602], length 84
23:35:59.730333 IP (tos 0x0, ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.56.1.60106 > localhost.localdomain.ssh: Flags [.], cksum 0x9283 (correct), seq 1673, ack 1822, win 2047, options [nop,nop,TS val 646547732 ecr 2860822], length 0
23:35:59.730537 IP (tos 0x2,ECT(0), ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 164)
    192.168.56.1.60106 > localhost.localdomain.ssh: Flags [P.], cksum 0x4a05 (correct), seq 1673:1785, ack 1822, win 2048, options [nop,nop,TS val 646547732 ecr 2860822], length 112
23:35:59.934062 IP (tos 0x0, ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.56.1.60106 > localhost.localdomain.ssh: Flags [.], cksum 0x8e91 (correct), seq 1785, ack 2322, win 2040, options [nop,nop,TS val 646547933 ecr 2861026], length 0
23:35:59.934238 IP (tos 0x0, ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.56.1.60106 > localhost.localdomain.ssh: Flags [.], cksum 0x8e5e (correct), seq 1785, ack 2366, win 2047, options [nop,nop,TS val 646547933 ecr 2861026], length 0
23:35:59.934450 IP (tos 0x4a,ECT(0), ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 496)
    192.168.56.1.60106 > localhost.localdomain.ssh: Flags [P.], cksum 0x5e76 (correct), seq 1785:2229, ack 2366, win 2048, options [nop,nop,TS val 646547933 ecr 2861026], length 444
 ```
#### 3. Close session. Find in tcpdump output packets that are related to TCP session closure.
```bash
23:36:17.141533 IP (tos 0x4a,ECT(0), ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 112)
    192.168.56.1.60106 > localhost.localdomain.ssh: Flags [P.], cksum 0xa16f (correct), seq 2697:2757, ack 3486, win 2048, options [nop,nop,TS val 646565067 ecr 2878233], length 60
23:36:17.141552 IP (tos 0x48, ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.56.1.60106 > localhost.localdomain.ssh: Flags [F.], cksum 0x000b (correct), seq 2757, ack 3486, win 2048, options [nop,nop,TS val 646565067 ecr 2878233], length 0
23:36:17.151543 IP (tos 0x48, ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.56.1.60106 > localhost.localdomain.ssh: Flags [.], cksum 0xfff6 (correct), seq 2758, ack 3487, win 2048, options [nop,nop,TS val 646565076 ecr 2878243], length 0
  ```
#### 4. run tcpdump and request any http site in separate session. Find HTTP request and answer packets with ASCII data in it.  Tcpdump command must be as strict as possible to capture only needed packages for this http request.


```bash
 curl http://info.cern.ch

[student@localhost ~]$ sudo tcpdump -A -i enp0s3 src 10.0.2.15 and tcp and port http 
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on enp0s3, link-type EN10MB (Ethernet), capture size 262144 bytes
00:00:52.240766 IP localhost.localdomain.59692 > webafs706.cern.ch.http: Flags [S], seq 2348415030, win 29200, options [mss 1460,sackOK,TS val 4353333 ecr 0,nop,wscale 7], length 0
E..<..@.@...
......l.,.P...6......r..a.........
.Bm5........
00:00:52.313796 IP localhost.localdomain.59692 > webafs706.cern.ch.http: Flags [.], ack 787648002, win 29200, length 0
E..(..@.@...
......l.,.P...7....P.r..M..
00:00:52.314095 IP localhost.localdomain.59692 > webafs706.cern.ch.http: Flags [P.], seq 0:76, ack 1, win 29200, length 76: HTTP: GET / HTTP/1.1
E..t..@.@..K
......l.,.P...7....P.r.....GET / HTTP/1.1
User-Agent: curl/7.29.0
Host: info.cern.ch
Accept: */*


00:00:52.388279 IP localhost.localdomain.59692 > webafs706.cern.ch.http: Flags [.], ack 879, win 30730, length 0
E..(..@.@...
......l.,.P.......pP.x
.M..
00:00:52.388765 IP localhost.localdomain.59692 > webafs706.cern.ch.http: Flags [F.], seq 76, ack 880, win 30730, length 0
E..(..@.@...
......l.,.P.......qP.x
.M..


  ```

#  Homework 5

## Processes

### 1. Run a sleep command three times at different intervals
```
sleep 10001 &
sleep 10002 &
sleep 10003 &
```
### 2. Send a SIGSTOP signal to all of them in three different ways.
```
[student@localhost ~]$ ps
  PID TTY          TIME CMD
 1289 pts/0    00:00:00 bash
 1308 pts/0    00:00:00 sleep
 1309 pts/0    00:00:00 sleep
 1310 pts/0    00:00:00 sleep
 1316 pts/0    00:00:00 ps
```

```
kill -s SIGSTOP 1308
kill -s 19 1309
kill -SIGSTOP 1310
```

### 3. Check their statuses with a job command
```
[student@localhost ~]$ jobs
[1]   Stopped                 sleep 10001
[2]-  Stopped                 sleep 10002
[3]+  Stopped                 sleep 10003

```
### 4. Terminate one of them. (Any)
```
kill -s SIGTERM 1308
```
### 5. To other send a SIGCONT in two different ways.
```
kill -s SIGCONT 1309
kill -SIGCONT 1310
```
### 6. Kill one by PID and the second one by job ID
```
kill -s SIGKILL 1310 / kill -s SIGKILL $(jobs -p 2)
fg 2 # Ctrl+C
```
Результат
```
[student@localhost ~]$ jobs
[1]+  Stopped                 sleep 10001
[3]-  Killed                  sleep 10003
```
```
[student@localhost ~]$ ps
  PID TTY          TIME CMD
 1308 pts/0    00:00:00 sleep
```

## Systemd

### 1. Write two daemons: one should be a simple daemon and do ```sleep 10``` after a start and then do ```echo 1 > /tmp/homework```, the second one should be oneshot and do ```echo 2 > /tmp/homework``` without any sleep
/etc/systemd/system/ - место находжение юнитов. 

daemon1.service
```
[Service]
ExecStartPre=/bin/sleep 10
ExecStart=/usr/bin/bash -c 'sudo /usr/bin/echo 1 > /tmp/homework'
[Install]
WantedBy=multi-user.target
```  
                                                             
daemon2.service
```
[Service]
Type=oneshot
ExecStart=/usr/bin/bash -c 'sudo /usr/bin/echo 2 > /tmp/homework'
[Install]
WantedBy=multi-user.target
```
```
systemctl daemon-reload
systemctl start daemon1.service
systemctl start daemon2.service
```
### 2. Make the second depended on the first one (should start only after the first)

```
[Unit]
Requires=daemon1.service
After=daemon1.service
```
systemctl start daemon1.service
### 3. Write a timer for the second one and configure it to run on 01.01.2019 at 00:00
```
daemon2.timer
[Timer]
OnCalendar=2019-01-01 00:00:00
Unit=daemon2.service
[Install]
WantedBy=multi-user.target
```
```
[student@localhost ~]$ systemctl list-timers --all
NEXT                         LEFT     LAST                         PASSED       UNIT                         ACTIVATES
n/a                          n/a      n/a                          n/a          daemon2.timer                daemon2.service
Sat 2021-12-18 05:57:21 MSK  23h left Fri 2021-12-17 05:57:21 MSK  4min 57s ago systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service
n/a                          n/a      n/a                          n/a          systemd-readahead-done.timer systemd-readahead-done.service

3 timers listed.
```
### 4. Start all daemons and timer, check their statuses, timer list and /tmp/homework
```systemctl status daemon1.service
● daemon1.service
   Loaded: loaded
    (/etc/systemd/system/daemon1.service; enabled; vendor preset: disabled)
   Active: inactive (dead) since Fri 2021-12-17 04:11:08 MSK; 3min 36s ago
  Process: 5376 ExecStart=/usr/bin/bash -c sudo /usr/bin/echo 1 > /tmp/homework (code=exited, status=0/SUCCESS)
  Process: 5332 ExecStartPre=/bin/sleep 10 (code=exited, status=0/SUCCESS)
 Main PID: 5376 (code=exited, status=0/SUCCESS)
 ```
 ```
[student@localhost ~]$ systemctl status daemon2.service
 ● daemon2.service
    Loaded: loaded (/etc/systemd/system/daemon2.service; enabled; vendor preset: disabled)
    Active: inactive (dead) since Fri 2021-12-17 04:10:58 MSK; 4min 21s ago
   Process: 5327 ExecStart=/usr/bin/bash -c sudo /usr/bin/echo 2 > /tmp/homework (code=exited, status=0/SUCCESS)
  Main PID: 5327 (code=exited, status=0/SUCCESS)
```
```
[student@localhost system]$ systemctl status daemon2.timer
● daemon2.timer
   Loaded: loaded (/etc/systemd/system/daemon2.timer; disabled; vendor preset: disabled)
   Active: active (elapsed) since Fri 2021-12-17 04:13:05 MSK; 35s ago

Dec 17 04:13:05 localhost.localdomain systemd[1]: Started daemon2.timer.
```

## cron/anacron

### 1. Create an anacron job which executes a script with echo Hello > /opt/hello and runs every 2 days
```
sudo vi /etc/anacrontab

2 1 echo.daily /bin/bash /home/student/script.sh
```
### 2. Create a cron job which executes the same command (will be better to create a script for this) and runs it in 1 minute after system boot.
```
crontab -l
@reboot sleep 1m && /home/student/script.sh
[student@localhost ~]$ sudo cat /var/log/cron
...
Dec 17 06:36:52 localhost CROND[719]: (student) CMD (sleep 1m && /home/student/script.sh)
```

### 3. Restart your virtual machine and check previous job proper execution
```
sleep 1 1> stdout 2> stderr
cat stdout && cat stderr
lsof | grep sleep
[student@localhost ~]$  lsof | grep sleep
sleep      748      student  cwd       DIR              253,0       179     472601 /home/student
sleep      748      student  rtd       DIR              253,0       224         64 /
sleep      748      student  txt       REG              253,0     33128   12741841 /usr/bin/sleep
sleep      748      student  mem       REG              253,0 106172832   12799787 /usr/lib/locale/locale-archive
sleep      748      student  mem       REG              253,0   2156272      15673 /usr/lib64/libc-2.17.so
sleep      748      student  mem       REG              253,0    163312      15666 /usr/lib64/ld-2.17.so
sleep      748      student    0r     FIFO                0,9       0t0      16603 pipe
sleep      748      student    1w     FIFO                ,9       0t0      16604 pipe
sleep      748      student    2w     FIFO                0,9       0t0      16604 pipe
```

## lsof

### 1. Run a sleep command, redirect stdout and stderr into two different files (both of them will be empty).
```
sleep 1 > stdout 2> stderr
cat stdout && cat stderr
```
### 2. Find with the lsof command which files this process uses, also find from which file it gain stdin.
```
sudo lsof | grep sleep

[student@localhost ~]$ sudo lsof | grep sleep
sleep     1308      student  cwd       DIR              253,0       179     472601 /home/student
sleep     1308      student  rtd       DIR              253,0       224         64 /
sleep     1308      student  txt       REG              253,0     33128   12741841 /usr/bin/sleep
sleep     1308      student  mem       REG              253,0 106172832   12799787 /usr/lib/locale/locale-archive
sleep     1308      student  mem       REG              253,0   2156272      15673 /usr/lib64/libc-2.17.so
sleep     1308      student  mem       REG              253,0    163312      15666 /usr/lib64/ld-2.17.so
sleep     1308      student    0u      CHR              136,0       0t0          3 /dev/pts/0
sleep     1308      student    1u      CHR              136,0       0t0          3 /dev/pts/0
sleep     1308      student    2u      CHR              136,0       0t0          3 /dev/pts/0
```
### 3. List all ESTABLISHED TCP connections ONLY with lsof
```
sudo lsof -iTCP sTCP:ESTABLISHED

[student@localhost ~]$ sudo lsof -i TCP | grep ESTABLISHED
sshd    1147    root    3u  IPv4  18454      0t0  TCP localhost.localdomain:ssh->192.168.56.1:50164 (ESTABLISHED)
sshd    1288 student    3u  IPv4  18454      0t0  TCP localhost.localdomain:ssh->192.168.56.1:50164 (ESTABLISHED)
```

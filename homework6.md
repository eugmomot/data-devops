## Task 1:
### 1.1. SSH to remotehost using username and password provided to you in Slack. Log out from remotehost.
```
[student@localhost ~]$ ssh Evgenii_Momot@18.221.144.175
The authenticity of host '18.221.144.175 (18.221.144.175)' can't be established.
***
Warning: Permanently added '18.221.144.175' (ECDSA) to the list of known hosts.
Evgenii_Momot@18.221.144.175's password: 
Last login: Sun Dec 19 21:29:28 2021 from pppoe.178-66-230-204.dynamic.avangarddsl.ru

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/
No packages needed for security; 4 packages available
Run "sudo yum update" to apply all updates.
[Evgenii_Momot@ip-172-31-33-155 ~]$ 
```
### 1.2. Generate new SSH key-pair on your localhost with name "hw-5" (keys should be created in ~/.ssh folder).
```
[student@localhost ~]$ cd ~/.ssh/
[student@localhost .ssh]$ ssh-keygen

Generating public/private rsa key pair.
Enter file in which to save the key (/home/student/.ssh/id_rsa): hw-5
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in hw-5.
Your public key has been saved in hw-5.pub.
The key fingerprint is:
SHA256:*** student@localhost.localdomain
The key's randomart image is:
+---[RSA 2048]----+
***
+----[SHA256]-----+

```
### 1.3. Set up key-based authentication, so that you can SSH to remotehost without password.
```
[student@localhost ~]$ ssh-copy-id Evgenii_Momot@18.221.144.175 -i ~/.ssh/hw-5.pub
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/student/.ssh/hw-5.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
Evgenii_Momot@18.221.144.175's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'Evgenii_Momot@18.221.144.175'"
and check to make sure that only the key(s) you wanted were added.
```
### 1.4. SSH to remotehost without password. Log out from remotehost.
```
[student@localhost ~]$ ssh Evgenii_Momot@18.221.144.175 -i ~/.ssh/hw-5.pub 
Last login: Mon Dec 20 05:03:36 2021 from 94.142.17.57

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/
No packages needed for security; 4 packages available
Run "sudo yum update" to apply all updates.
[Evgenii_Momot@ip-172-31-33-155 ~]$ 
```
### 1.5. Create SSH config file, so that you can SSH to remotehost simply running `ssh remotehost` command. As a result, provide output of command `cat ~/.ssh/config`.
```
[student@localhost ~]$ vi ~/.ssh/config
	Host remotehost
	HostName 18.221.144.175
	User Evgenii_Momot
	IdentityFile ~/.ssh/hw-5
[student@localhost ~]$ chmod 600 ~/.ssh/config
[student@localhost ~]$ ssh remotehost
```
### 1.6. Using command line utility (curl or telnet) verify that there are some webserver running on port 80 of webserver.  Notice that webserver has a private network IP, so you can access it only from the same network (when you are on remotehost that runs in the same private network). Log out from remotehost.
```
[Evgenii_Momot@ip-172-31-33-155 ~]$ curl 172.31.45.237
...
.footer {
   border-top: 1px solid rgba(255,255,255,0.2);
   padding-top: 30px;
}

    --></style>
</head>
<body>
  <div class="jumbotron text-center">
    <div class="container">
          <h1>Hello!</h1>
                <p class="lead">You are here because you're probably a DevOps courses member. In that case you should open <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"> THIS LINK </a></p>
                </div>
  </div>
</body></html>

```
### 1.7. Using SSH setup port forwarding, so that you can reach webserver from your localhost (choose any free local port you like).
```
[student@localhost .ssh]$ ssh -L 0.0.0.0:8080:172.31.45.237:80 remotehost
[student@localhost .ssh]$ telnet 0.0.0.0 8080
Trying 0.0.0.0...
Connected to 0.0.0.0.
Escape character is '^]'.
GET /

...
.main {
   background: white;
   color: #234;
   border-top: 1px solid rgba(0,0,0,0.12);
   padding-top: 30px;
   padding-bottom: 40px;
}

.footer {
   border-top: 1px solid rgba(255,255,255,0.2);
   padding-top: 30px;
}

    --></style>
</head>
<body>
  <div class="jumbotron text-center">
    <div class="container">
          <h1>Hello!</h1>
                <p class="lead">You are here because you're probably a DevOps courses member. In that case you should open <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"> THIS LINK </a></p>
                </div>
  </div>
</body></html>

```
### 1.8 Like in 1.6, but on localhost using command line utility verify that localhost and port you have specified act like webserver, returning same result as in 1.6.
```
ssh -L 0.0.0.0:8080:172.31.45.237:80 remotehost

[student@localhost ~]$ telnet 0.0.0.0 8080
...
.footer {
   border-top: 1px solid rgba(255,255,255,0.2);
   padding-top: 30px;
}

    --></style>
</head>
<body>
  <div class="jumbotron text-center">
    <div class="container">
          <h1>Hello!</h1>
                <p class="lead">You are here because you're probably a DevOps courses member. In that case you should open <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"> THIS LINK </a></p>
                </div>
  </div>
</body></html>
Connection closed by foreign host.
[student@localhost ~]$ 

```
### 1.9 (*) Open webserver webpage in browser of your Host machine of VirtualBox (Windows, or Mac, or whatever else you use). You may need to setup port forwarding in settings of VirtualBox.
```
eugene@Eugenes-MacBook-Pro ~ % ssh -L 127.0.0.1:8080:0.0.0.0:8080 student@127.0.0.1 -p 2222

```
<img width="1443" alt="Screenshot 2021-12-20 at 08 02 53" src="https://user-images.githubusercontent.com/68924420/146714642-d70f3efe-5068-49de-a517-05c3e4f48e49.png">

## Task 2:

### 2.1. Imagine your localhost has been relocated to Havana. Change the time zone on the localhost to Havana and verify the time zone has been changed properly (may be multiple commands).
```
[student@localhost ~]$ timedatectl set-timezone America/Havana
[student@localhost ~]$ timedatectl
      Local time: Mon 2021-12-20 00:20:56 CST
  Universal time: Mon 2021-12-20 05:20:56 UTC
        RTC time: Mon 2021-12-20 05:20:56
       Time zone: America/Havana (CST, -0500)
```
### 2.2. Find all systemd journal messages on localhost, that were recorded in the last 50 minutes and originate from a system service started with user id 81 (single command).
```
[student@localhost ~]$ journalctl --since "50 min ago"  _UID=81 
-- Logs begin at Sun 2021-12-19 23:54:14 CST, end at Mon 2021-12-20 00:15:36 CST. --
Dec 19 23:54:19 localhost.localdomain dbus[645]: [system] Activating via systemd: service name='org.freedesktop.hostname1' unit='dbus-org.
Dec 19 23:54:19 localhost.localdomain dbus[645]: [system] Successfully activated service 'org.freedesktop.hostname1'
Dec 19 23:54:19 localhost.localdomain dbus[645]: [system] Activating via systemd: service name='org.freedesktop.nm_dispatcher' unit='dbus-
Dec 19 23:54:19 localhost.localdomain dbus[645]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'
Dec 20 00:15:34 localhost.localdomain dbus[645]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.
Dec 20 00:15:34 localhost.localdomain dbus[645]: [system] Successfully activated service 'org.freedesktop.timedate1'
```
### 2.3. Configure rsyslogd by adding a rule to the newly created configuration file /etc/rsyslog.d/auth-errors.conf to log all security and authentication messages with the priority alert and higher to the /var/log/auth-errors file. Test the newly added log directive with the logger command (multiple commands).
```
sudo vi /etc/rsyslog.d/auth-errors.conf 
  auth.* /var/log/auth-errors 
  authpriv.* /var/log/auth-errors 
systemctl restart rsyslog 

[student@localhost ~]$ sudo cat /var/log/auth-errors
Dec 20 00:23:17 localhost polkitd[644]: Unregistered Authentication Agent for unix-process:1531:174152 (system bus name :1.51, object path /org/freedesktop/PolicyKit1/AuthenticationAgent, locale en_US.UTF-8) (disconnected from bus)
Dec 20 00:23:24 localhost sudo: student : TTY=pts/1 ; PWD=/home/student ; USER=root ; COMMAND=/bin/cat /var/log/auth-errors
Dec 20 00:23:24 localhost sudo: pam_unix(sudo:session): session opened for user root by student(uid=0)
```

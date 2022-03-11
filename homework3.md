# AWK
## 1.
```
awk '{gsub("\"", ""); print $12 " " ++count[$12]}' access.log | sort -k 2 -rn | head -n 1
```
## 2.
script
```
#!/usr/bin/awk -f

{
  split($4, a, ":")
  ip=$1
  month=substr(a[1], 5)


  if (ip == "216.244.66.230")
    months[month]++
}
END {
   for (m in months)
     print m " " months[m]
}

```
Result:
```
./script access.log | grep 2020 | sort -M && ./script access.log | grep 2021 | sort -M
Dec/2020 1
Jan/2021 43
Feb/2021 14
Mar/2021 2
Apr/2021 34
May/2021 27
Jun/2021 3
Jul/2021 23
Aug/2021 108
Sep/2021 7
Oct/2021 23
Nov/2021 106
Dec/2021 3

```

## 3.
script2
```
#!/usr/bin/awk -f
{
  bytes[$1] = bytes[$1] + $10
}
END {
   for (ip in bytes)
     print ip " " bytes[ip]
}
```
Result:
```
./script2 access.log 
...
204.15.145.39 13020
157.55.39.148 10184644
159.89.187.19 34198293
94.154.220.93 10466
145.253.118.26 26209910
```
# SED

## 1
```
sed -i -e 's/\(.*.*\ \- \-\ \[.*\] \".*\" [0-9]* [0-9]* \".*\"\) \(\".*\"\) \(.*.*\)/\1 "lynx" \3/' ~/access.log
```
Result:
```
...
66.102.6.99 - - [06/Dec/2021:10:20:52 +0100] "GET / HTTP/1.1" 200 10439 "-" "lynx" "-"
66.102.6.96 - - [06/Dec/2021:10:20:52 +0100] "GET /favicon.ico HTTP/1.1" 404 217 "-" "lynx" "-"
185.83.147.245 - - [06/Dec/2021:10:23:41 +0100] "GET / HTTP/1.1" 200 10439 "-" "lynx" "-"
185.83.147.245 - - [06/Dec/2021:10:23:41 +0100] "GET / HTTP/1.1" 200 10479 "-" "lynx" "-"
94.30.152.134 - - [06/Dec/2021:10:28:05 +0100] "GET /apache-log/access.log HTTP/1.1" 200 2139012 "http://www.almhuette-raith.at/" "lynx" "-"
94.30.152.134 - - [06/Dec/2021:10:28:05 +0100] "GET /templates/jp_hotel/css/template.css HTTP/1.1" 200 10004 "http://www.almhuette-raith.at/apache-log/access.log" "lynx" "-"
94.30.152.134 - - [06/Dec/2021:10:59:39 +0100] "GET /apache-log/access.log HTTP/1.1" 200 1761864 "http://www.almhuette-raith.at/" "lynx" "-"
94.30.152.134 - - [06/Dec/2021:10:59:39 +0100] "GET /templates/jp_hotel/css/template.css HTTP/1.1" 200 10004 "http://www.almhuette-raith.at/apache-log/access.log" "lynx" "-"
54.240.197.239 - - [06/Dec/2021:11:13:51 +0100] "GET /favicon.ico HTTP/1.1" 404 217 "http://www.almhuette-raith.at/apache-log/access.log" "lynx" "-"
178.66.235.108 - - [06/Dec/2021:11:14:02 +0100] "GET /apache-log/access.log HTTP/1.1" 200 4436000 "-" "lynx" "-"
```

## 2
```
cat text.txt | ./script3 > temp  && cp temp text.txt && rm temp
````
script3
```
#!/bin/bash

declare -A ips

iter=0
value=""

while IFS= read -r line
do
  s=$(sed "s/\([0-9]*\.[0-9]*\.[0-9]*\.[0-9]*\) \(.*\)/\1/" <<< ${line})
  IP=${s// }
  if [ ! -z "$IP" ]
    then
      if [ ${ips[$IP]+_} ]
        then
          value=${ips[$IP]}
        else
          iter=$((iter+1))
          ips[$IP]=${iter}
          value=iter
      fi
  fi
  sed "s/\([0-9]*\.[0-9]*\.[0-9]*\.[0-9]*\) \(.*\)/ip$((value)) \2/" <<< ${line} 

done
```
```
ip1 - - [20/Jan/2021:03:50:40 +0100] "GET /index.php?format=feed&type=atom HTTP/1.1" 200 8198 "http://www.almhuette-raith.at/" "Mozilla/5.0 (compatible; SEOkicks; +https://www.seokicks.de/robot.html)" "-"
ip1 - - [20/Jan/2021:03:50:41 +0100] "GET /index.php?option=com_content&view=article&id=49&Itemid=55 HTTP/1.1" 200 7936 "http://www.almhuette-raith.at/" "Mozilla/5.0 (compatible; SEOkicks; +https://www.seokicks.de/robot.html)" "-"
ip1 - - [20/Jan/2021:03:50:43 +0100] "GET /index.php?option=com_content&view=article&id=50&Itemid=56 HTTP/1.1" 200 7991 "http://www.almhuette-raith.at/" "Mozilla/5.0 (compatible; SEOkicks; +https://www.seokicks.de/robot.html)" "-"
ip1 - - [20/Jan/2021:03:50:45 +0100] "GET /index.php?option=com_phocagallery&view=category&id=1&Itemid=53 HTTP/1.1" 200 32583 "http://www.almhuette-raith.at/" "Mozilla/5.0 (compatible; SEOkicks; +https://www.seokicks.de/robot.html)" "-"
ip1 - - [20/Jan/2021:03:50:47 +0100] "GET /index.php?option=com_content&view=article&id=46&Itemid=54 HTTP/1.1" 200 8938 "http://www.almhuette-raith.at/" "Mozilla/5.0 (compatible; SEOkicks; +https://www.seokicks.de/robot.html)" "-"
ip1 - - [20/Jan/2021:03:50:51 +0100] "GET /index.php?option=com_phocagallery&view=category&id=4:ferienwohnung2&Itemid=53 HTTP/1.1" 200 16730 "http://www.almhuette-raith.at/index.php?option=com_content&view=article&id=50&Itemid=56" "Mozilla/5.0 (compatible; SEOkicks; +https://www.seokicks.de/robot.html)" "-"
ip1 - - [20/Jan/2021:03:50:54 +0100] "GET /index.php?option=com_phocagallery&view=category&id=3:almhuette-raith&Itemid=53 HTTP/1.1" 200 10862 "http://www.almhuette-raith.at/index.php?option=com_phocagallery&view=category&id=1&Itemid=53" "Mozilla/5.0 (compatible; SEOkicks; +https://www.seokicks.de/robot.html)" "-"
ip2 - - [20/Jan/2021:04:00:28 +0100] "GET /administrator/index.php HTTP/1.1" 200 4263 "-" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 OPR/32.0.1948.45" "-"
ip2 - - [20/Jan/2021:04:00:29 +0100] "POST /administrator/index.php HTTP/1.0" 200 4481 "-" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 OPR/32.0.1948.45" "-"^
...
```



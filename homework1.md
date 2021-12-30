# 0
Для внутренего настройки подключения необходимо выбрать Internal Network. Например, задать для VM1 (192.168.0.1) и VM2 (192.168.0.2).

sudo vi /etc/sysconfig/network-script/ifcfg-enp0s3

<img width="975" alt="Screenshot 2021-11-30 at 21 12 06" src="https://user-images.githubusercontent.com/68924420/144115112-42feb3af-58ae-4407-a005-56d5902b8068.png">

Рабочии SSH между двумя VM
<img width="1258" alt="Screenshot 2021-11-30 at 21 13 33" src="https://user-images.githubusercontent.com/68924420/144115143-a2a11da7-21c6-4c97-9025-71ac745afa5a.png">

# 1
```
cd /usr/share/man
ls -d man?/*config*
ls -d man[1,7]/*system*
```
<p align="center">
<img width="912" alt="Screenshot 2021-11-30 at 21 23 07" src="https://user-images.githubusercontent.com/68924420/144115600-b8cf54c4-3b0a-4575-9516-14da17556c10.png">
</p>
# 2
```
cd /usr/shar/man/ 
find -iname “*help*” 
find -iname “conf*” 
```
<p align="center">
<img width="315" alt="Screenshot 2021-11-30 at 21 37 19" src="https://user-images.githubusercontent.com/68924420/144115706-30b183df-46cf-46f5-9389-3bac179fc273.png">
</p>

`find -iname <имя файла>` - не учитывать регистр;
`find -path <путь>` -найти указанный путь;
`find -size <размер>` -выводить файлы указанного размера;
`find -mindepth <число>` - искать начиная с заданного числа уровней вниз;
`find -maxdepth <число> `- искать не больше чем на заданное число уровней вниз.
<p align="center">
<img width="295" alt="Screenshot 2021-11-30 at 21 36 37" src="https://user-images.githubusercontent.com/68924420/144115735-a060b1f1-6922-4c08-9f1f-d7da81c1125d.png">
</p>

# 3
```
wc /etc/fstab
tail -n 2 /etc/fstab
head -n 7 etc/yum.conf.
```
При вводе команды tail и head с опцией больше, чем количество строк в файле выводиться все строчки файла.

# 4
```
touch file_name{1..3}.md
mv -v file_name1.{md,textdoc} && mv -v  file_name2{.md, } && mv -v file_name3.md{,.latest} && mv -v file_name1{.textdoc, .txt}
```
<p align="center">
<img width="803" alt="Screenshot 2021-11-30 at 21 48 19" src="https://user-images.githubusercontent.com/68924420/144116085-093aafcf-5b86-4c30-aa34-cc4a9cf02c91.png">
</p>

#5
```
cd ~
cd /home/admin
cd /home && cd admin/
```
# 6

```
mkdir new in-process processed in-process/tread{0..2}
touch data new/data{00..99}
cp new/data{00..33} in-process/tread0
cp new/data{34..66} in-process/tread1
cp new/data{67..99} in-process/tread2
ls in-process/tread{0..2}
cp in-process/tread*/* processed
```
Удаление по условию

```
A=$(ls processed | wc -l)
B=$(ls new | wc -l)
if [ "$A" = "$B" ]; then 
  rm new/*
else
  echo "not equal"
fi
```

# 7
```
for x in {1..3}; do printf "files${x} "; done; printf "\n"
```

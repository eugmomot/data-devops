# 1. Открыть инструкцию по пользованию приложением awk. Найти секцию про использование переменных окружения. Сохранить эту секцию в отдельный файл.
```
man awk | grep "ENVIRONMENT VARIABLES" -A9 > ENVIRONMENT_VARIABLES.txt
```
Result:
```
[student@localhost ~]$ cat ENVIRONMENT_VARIABLES.txt
ENVIRONMENT VARIABLES
       The AWKPATH environment variable can be  used  to  provide  a  list  of
       directories  that gawk searches when looking for files named via the -f
       and --file options.

       For socket communication, two special environment variables can be used
       to  control the number of retries (GAWK_SOCK_RETRIES), and the interval
       between retries (GAWK_MSEC_SLEEP).  The interval is in milliseconds. On
       systems  that  do  not support usleep(3), the value is rounded up to an
       integral number of seconds.
```

# 2. Написать скрипт, который создаёт файл "task2.txt" директорией выше своего местоположения. В случае ошибки текст ошибки записывается в err.log а пользователю выдаётся сообщение "Error."
Скрипт 
```
#!/bin/bash
cd ..
touch task2.txt 2>> ~/err.log

if [[ $? = 1 ]]; then
        echo "Error"
fi  
```


# 2*. Если файл уже существует, выдаётся одна ошибка, а если нет прав для его создания - другая.
```
#!/bin/bash
cd ..
if [[ "$(find task2.txt 2>> ~/err.log )" = "task2.txt" ]]; then
        echo "File already exists"
else
        touch task2.txt 2>> ~/err.log
        if [[ $? = 1 ]]; then
                echo "Permission Denied"
        fi
fi
```
# 3. Создать 2 файла: 1-й - текстовый с указанием абслютного пути до директории. 2-й - скрипт, который при выполнении выводит содержимое директории по указанному в первом файле.

file1.txt
```
/home/student
```
file2.sh
```
#!/bin/bash
path=$(<file1.txt); ls -Aplh
```
# 3*. Скрипт выводит отдельно количество файлов и количество директорий.
file1.txt
```
/home
```
file2.sh
```
path=$(<file1.txt)
cd $path 
ls -lAh
echo "Path:$(pwd)"
echo "Directories: $(ls -Ap | grep  / |  wc -l)  Files: $(ls -Ap | grep  -v / |  wc -l)"
```
Result:
```
[student@localhost ~]$ ~/file2.sh 
total 8
drwx------. 9 student student 4096 Dec  6 16:38 student/
Path:/home
Directories: 1  Files: 0
```
# 3**. Скрипт принимает любое количество записей в первом файле и обрабатывает их последовательно.
file1.txt
```
/home/student
/
/home
/etc
/usr
```
file2.sh
```
while read path; do
        cd $path
        echo "Directories: $(ls -Ap | grep  / |  wc -l) Files: $(ls -Ap | grep  -v / |  wc -l) Path:$(pwd)"
done < file1.txt
```
Result:
```
[student@localhost ~]$ ./file2.sh 
Directories: 7    Files: 18    Path:  /home/student
Directories: 15   Files: 4     Path:  /
Directories: 1    Files: 0     Path:  /home
Directories: 72   Files: 100   Path:  /etc
Directories: 11   Files: 1     Path:  /usr
```

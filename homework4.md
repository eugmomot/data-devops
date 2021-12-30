# Task1
Используйте команды: groupadd, useradd, passwd, chage и другие.
Создайте группу sales с GID 4000 и пользователей bob, alice, eve c основной группой sales. 
Измените пользователям пароли.
Все новые аккаунты должны обязательно менять свои пароли каждый 30 дней.
Новые аккаунты группы sales должны истечь по окончанию 90 дней срока, а bob должен изменять его пароль каждые 15 дней.

```
sudo groupadd sales --gid 4000
sudo useradd -G sales bob
sudo useradd -G sales alice
sudo useradd -G sales eve 
sudo passwd bob
sudo passwd alice
sudo passwd eve
cat /etc/passwd
cat /etc/group
```
```
vi /etc/login.defs
```
Внесенные изменения в файл конфигурации login.defs:
```
PASS_MAX_DAYS	30
```
```
for user in `sudo groupmems  -g sales --list`; do sudo chage -E `date -d "90 days" +"%Y-%m-%d"` $user ; done
sudo  passwd -x 15 bob

Сброс всех паролей группы sales.
```
for user in `sudo groupmems  -g sales --list`; do sudo chage -d 0 $user ; done
```

```
# Task2
Используйте команды: su, mkdir, chown, chmod и другие.
Создайте трёх пользователей glen, antony, lesly.
У вас должна быть директория /home/students, где эти три пользователя могут работать совместно с файлами.
Должен быть возможен только пользовательский и групповой доступ, создание и удаление файлов в /home/students. 
Файлы, созданные в этой директории, должны автоматически присваиваться группе студентов students.

```
sudo useradd glen
sudo useradd antony
sudo useradd lesly
sudo passwd glen
sudo passwd antony
sudo passwd lesly
sudo mkdir /home/students
sudo groupadd students --gid 4001
sudo usermod -a -G students glen
sudo usermod -a -G students antony
sudo usermod -a -G students lesly
sudo chown -R :students /home/students
sudo chmod -R 2770 /home/students
```
# Task3
Детективное агентство Бейкер Стрит создает коллекцию совместного доступа для хранения файлов дел, в которых члены группы bakerstreet будут иметь права на чтение и запись.
Ведущий детектив, Шерлок Холмс, решил, что члены группы scotlandyard также должны иметь возможность читать и писать в общую директорию. Тем не менее, Холмс считает, что инспектор Джонс является достаточно растерянным, и поэтому он должен иметь доступ только для чтения. 
Миссис Хадсон только начала осваивать Linux и смогла создать общую директорию и скопировать туда несколько файлов. Но сейчас время чаепития, и она попросила вас закончить работу.

Ваша задача - завершить настройку директории общего доступа. 
Директория и всё её содержимое должно принадлежать группе bakerstreet, при этом файлы должны обновляться для чтения и записи для владельца и группы (bakerstreet). У других пользователей не должно быть никаких разрешений. 
Вам также необходимо предоставить доступы на чтение и запись для группы scotlandyard, за исключением Jones, который может только читать документы.
Убедитесь, что ваша настройка применима к существующим и будущим файлам. После установки всех разрешений в директории проверьте от каждого пользователя все его возможные доступы.

Используйте команды: touch, mkdir, chgrp, chmod, getfacl, setfacl и другие. 
Создайте общую директорию /share/cases.
Создайте группу bakerstreet с пользователями holmes, watson.
Создайте группу scotlandyard с пользователями lestrade, gregson, jones.
Задайте всем пользователям безопасные пароли.

```
sudo mkdir /share
sudo mkdir /share/cases
sudo touch /share/cases/murders.txt
sudo touch /share/cases/moriarty.txt
sudo groupadd baker-street
sudo groupadd scotlandyard

sudo useradd -G bakerstreet holmes
sudo useradd -G bakerstreet watson
sudo passwd holmes
sudo passwd watson

sudo useradd -G scotlandyard lestrade 
sudo useradd -G scotlandyard gregson 
sudo useradd -G scotlandyard jones
sudo passwd lestrade
sudo passwd gregson
sudo passwd jones

sudo chown -R :bakerstreet /share/cases/

sudo setfacl -Rm g:scotlandyard:rwx,g:bakerstreet:rwx,u:jones:rx,o::- /share/cases

```

При проверке пользователи ```holmes, watson, lestrade, gregson``` могут читать и вносить правки. 
Пользователь ```jones``` может только читать, при внесении изменении в файл появляется следующее сообщение: ``` **-- INSERT -- W10: Warning: Changing a readonly file
** ``` 

# Новый пользователь:
1. Создание пользователя на сервере: 
```bash
$ adduser <username>
```
2. Добавление пользователя <username> в sudoers (выполняется от root):
```bash
$ usermod -aG sudo <username>
```

# Для входа на сервер по SSH ключам:
- Клиент
  1. Создать у себя новую пару ключей SSH
  ```bash
  $ ssh-keygen -t ed25519
  ```
  2. Передать открытый ключ на сервер:
  ```bash
  $ ssh-copy-id -i ~/.ssh/<public_key_file> <username>@<server_ip>
  ```
  Если имя ключей было придумано самостоятельно, тогда необходимо создать файл с настройками, в котором будут указаны какие ключи для каких хостов использовать:
  ```bash
  $ touch ~/.ssh/config
  ```
  ```
  # ~/.ssh/config
  Host server_ip
    User username
    IdentityFile ~/.ssh/private_key_file
  ```
  
- Сервер
  1. Подключаемся к серверу
  ```bash
  $ ssh <username>@<server_ip>
  ```
  2. Необходимо перезапустить службы SSH на сервере:
  ```bash
  $ sudo service ssh restart (для Ubuntu / Debian / Mint Linux)
  $ sudo service sshd restart (для CentOS / RHEL / Fedora Linux)
  ```

# Отключение доступа по паролю

Для того, чтобы доступ к серверу мог осуществляться только по ключу, необходимо запретить авторизацию по паролю. Для этого требуется внести правки в файл `/etc/ssh/sshd_config`.
Откройте файл командой:
```bash
$ sudo nano /etc/ssh/sshd_config
```
Найдите в нем строку `PasswordAuthentication` и замените ее значение на: `PasswordAuthentication no`.
Сохраните изменения, после чего перезапустите службу SSH: 
```bash
$ sudo service ssh restart (для Ubuntu / Debian / Mint Linux)
$ sudo service sshd restart (для CentOS / RHEL / Fedora Linux)
```

Если после выполненных действий у вас по-прежнему запрашивается пароль, проверьте, нет ли в директории `/etc/ssh/sshd_config.d/` файла `50-cloud-init.conf` с директивой `PasswordAuthentication yes`.
Если файл присутствует — удалите его, после чего перезапустите службу SSH.

# Полезные ссылки:
- https://www.cherryservers.com/blog/create-a-user-in-linux
- https://support.rusonyx.ru/index.php?/Knowledgebase/Article/View/380/0/podkljuchenie-k-serveru-po-ssh#:~:text=Открываем%20PuTTY%20%3D%3E%20%22Соединение%22,осуществлено%20автоматически%2C%20без%20ввода%20пароля.
- https://timeweb.cloud/docs/unix-guides/ssh-key-authentication
- https://selectel.ru/blog/ssh-authentication/
- [SSH not working when custom key name is used](https://serverfault.com/questions/1119891/ssh-not-working-when-custom-key-name-is-used)
- [Using the SSH Config File](https://linuxize.com/post/using-the-ssh-config-file/)

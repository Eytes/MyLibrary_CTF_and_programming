TODO: установка oh-my-zsh (с расширениями автодополнения и подсветки синтаксиса) git curl wget ssh-client docker docker-compose VMWare pycharm vscode


# Ubuntu

1.  бновление системы
    ```bash
    $ sudo apt update -y && sudo apt upgrade -y
    ```
    
3.  Установка poetry
    ```bash
    $ curl -sSL https://install.python-poetry.org | python3 -
    ```

3. Настройка git
   ```bash
    $ git config --global user.name 'Eytes'
    $ git config --global user.email 'yura.shamanov2000@bk.ru'
    $ ssh-keygen -t ed25519 -C "yura.shamanov2000@bk.ru"  # публичный ключ необходимо добавить на GitHub
   ```
    

# Manjaro / Arch

1. Обновление системы
   ```bash
   $ sudo pacman -Syyu
   ```
   
2. Настройка git
   ```bash
    $ git config --global user.name 'Eytes'
    $ git config --global user.email 'yura.shamanov2000@bk.ru'
    $ ssh-keygen -t ed25519 -C "yura.shamanov2000@bk.ru"  # публичный ключ необходимо добавить на GitHub
   ```
   
3. Уставновка virtualbox
   ```bash
   $ mhwd-kernel -li
   Currently running: 5.4.0-1-MANJARO (linux54)
   The following kernels are installed in your system:
      * linux54
   ```
   ```bash
   $ sudo pacman -Syu virtualbox linux54-virtualbox-host-modules
   ```
   ```bash
   $ sudo vboxreload
   ```
   ```bash
   $ vboxmanage --version
   6.1.14r140239
   ```
   
3.  Установка poetry
    ```bash
    $ curl -sSL https://install.python-poetry.org | python3 -
    ```

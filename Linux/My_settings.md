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

# MacOS

1. Установка менеджера оконо [Rectangle](https://rectangleapp.com)
2. Установка [Docker Desktop](https://docs.docker.com/desktop/install/mac-install/)
3. Установка [telegram-desktop](https://macos.telegram.org)
4. Установка [Discord](https://discord.com/download)
5. Установка [PyCharm](https://www.jetbrains.com/pycharm/download/?section=mac)
6. Установка `oh-my-zsh` и плагины
   ```shell
   $ sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
   $ git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
   ```
7. установка `brew` и добавление в окружение
   ```shell
   $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   $ (echo; echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"') >> ~/.zshrc
   $ eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
   ```
8. Установка необходимых улитил
   ```shell
   $ brew install poetry wget bat
   ```
9. Установка `Rust`, включая `cargo`, `rustc`, `rustup`
    ```shell
    $ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    ```

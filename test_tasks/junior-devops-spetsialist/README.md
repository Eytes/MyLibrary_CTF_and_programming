# Тестовое задание для вакансии Junior DevOps специалист

## Развернуть PHP приложение
> Заданию уделите от 5 до 24 рабочих часов, что успеете высылайте. Срок 5 дней.

### Вводные данные
*	Дан репозиторий с PHP приложением Laravel;
*	Приложением подключается к двум БД MySql - из одной читает, в другую пишет;
*   Для запуска приложения требуется реализовать репликацию базы данных и запуск нескольких команд для миграции базы данных и установки требуемых библиотек (об это ниже).


### Задача
* Требуется запустить Laravel (PHP) приложение. Требуемое ПО для запуска:
    * Веб-сервер (Apache/Nginx, предпочтительнее Nginx);
    * PHP 8+;
    * База данных (MySql/MariaDB, предпочтительнее MariaDB 10+);
    * Composer 2+ - пакетный менеджер для подключения библиотек PHP;
    * Npm 8.19+ (node.js) - пакетный менеджер для подключения библиотек JS;
    * Artisan (from Laravel 9+);
* Само приложение находится в этом репозитории в папке [src](https://github.com/Eytes/MyLibrary_CTF_and_programming/tree/main/test_tasks/junior-devops-spetsialist/src);
* Приложение работает с двумя базами данных:
    * WRITER_DB - для записи;
    * READER_DB - для чтения;
* Требуется реализовать репликацию Master→Slave (WRITER_DB→READER_DB);
* Для запуска приложения требуется выполнить следующее:
    * создать файл ".env" в корне приложения (скопировать в него содержимое из "[.env.example](https://github.com/Eytes/MyLibrary_CTF_and_programming/tree/main/test_tasks/junior-devops-spetsialist/src.env.example)" - лежит в этой же директории);
    * В созданном ".env" указать переменные подключения к базам данных:
        * WRITER_DB_HOST=ip адрес сервера БД для записи;
        * WRITER_DB_PORT=порт подключения к БД;
        * WRITER_DB_DATABASE=имя базы;
        * WRITER_DB_USERNAME=имя пользователя;
        * WRITER_DB_PASSWORD=пароль;

        Аналогично указать переменные для подключения к БД чтения:

        * READER_DB_HOST=
        * READER_DB_PORT=
        * READER_DB_DATABASE=
        * READER_DB_USERNAME=
        * READER_DB_PASSWORD=

    * Установить PHP библиотеки командной: ```composer install```;
    * Установить JS библиотеки командной: ```npm install```;
    * Сгенерировать ключ приложения командной: ```php artisan key:generate```;
    * Создать таблицы и заполнить их данными: ```php artisan migrate:fresh --seed```;

* В запущенном приложении (TODO List) убедиться, что все задачи решены:<br>
    ![Список задач](1669274356404.jpg "Список задач") 


### Требования

> Если есть сомнения по деталям — решение принять самостоятельно, но в своём README.md рекомендуем выписать вопросы и принятые решения по ним.

* Финальную версию нужно выложить на github.com / bitbucket.org;
* Предоставить инструкцию по запуску приложения;
* Ожидаемый результат запуска приложения одной командой docker-compose up -d --build / ansible-playbook / etc...;

### Усложнения

> Не обязательно, но задание может быть выполнено с любым числом усложнений:

* Архитектура сервиса описана в виде текста и/или диаграмм;
* Документация: есть структурированное описание методов сервиса;
* Балансировщик: any;
* Дашборд с метриками приложения: grafana/kibana/zabbix/any.
* Несколько настроенных алертов.
* Пример, что можно мониторить и на что настраивать алерты:
    * CPU Idle < 10% за последние 10 минут;
    * Объем свободного места на диске < 10%;
    * Free inodes <10%;
    * Нагрузка на диск (iostat) > 95% в течение 3 минут;
    * Заполнение SWAP > 90%.
    * Docker / docker_alive — алерт на приостановку работы сервиса docker;
    * Docker / amount_changed - алерт на изменение количества запущенных контейнеров;
    * Nginx status (RPS) - алерт при нулевом RPS в течение 10 минут;
    * Nginx 5xx_errors - алерт на 500 ошибку приложения;
    * PHP-FPM / RPS = 0 в течение трёх минут;


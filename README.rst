Django cookiecutter template
============================

Шаблон Django, который `мы <http://kupo.la>`_ используем для разработки наших сайтов.

Использование
-------------

Разверните новое виртуальное окружение с помощью `virtualenvwrapper`:

.. code-block:: shell

    mkvirtualenv newproject
    cd $VIRTUAL_ENV

С помощью `cookiecutter` создайте структуру проекта:

.. code-block:: shell

    pip install cookiecutter
    cookiecutter gh:alexmorozov/django-template

В ходе создания заполните поля:

- **project_name**: название проекта. Так будет назван модуль Python, поэтому
  выбирайте валидное имя.
- **admin_name** и **admin_email**: контакты администратора. Будут использованы в
  настройке Django ADMINS.
- **version**: версия с которой начинать проект.
- **production_host**: адрес боевого сервера. Используется при деплое.
- **site_name**: адрес сайта. Используется в ALLOWED_HOSTS в боевом режиме.
- **local_db_name**, **local_db_user**, **local_db_password**: реквизиты локальной БД
  для разработки.
- **sentry_dsn**: DSN для боевого логирования в Sentry.
- **secret_key**: Секретный ключ Django. Сгенерировать можно, например `здесь
  <http://www.miniwebtool.com/django-secret-key-generator/>`_.

Рекомендую свежесозданную папку проекта переименовать в `src`, чтобы иметь
одинаковое предсказуемое расположение кода во всех виртуальных окружениях.

Что включено
------------

TODO: Расшифруй

- HAML
- bumpversion
- Модульные requirements
- DJANGO_CONF
- shell_plus
- sudo runs_plus
- bumpversion
- fab pip
- ln -s manage.py
- local settings
- raven


Лицензия
--------

GPLv3

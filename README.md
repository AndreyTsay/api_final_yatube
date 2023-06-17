API_FINAL_YATUBE
Описание
API для Yatub представляет собой проект социальной сети в которой реализованы следующие возможности, публиковать записи, комментировать записи, а так же подписываться или отписываться от авторов.

Стек технологий
Python 3.11,
Django 4.2,
DRF,
JWT + Djoser
Запуск проекта в dev-режиме
Клонировать репозиторий и перейти в него в командной строке.
Установите и активируйте виртуальное окружение
python -m venv venv
source venv/Scripts/activate
python -m pip install --upgrade pip
Затем нужно установить все зависимости из файла requirements.txt
cd yatube_api
pip install -r requirements.txt
Выполняем миграции:
python manage.py migrate
Создаем суперпользователя:
python manage.py createsuperuser
Запускаем проект:
python manage.py runserver
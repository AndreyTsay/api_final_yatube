<!DOCTYPE html><html><head><meta charset="utf-8">
<h1 class="code-line" data-line-start="0" data-line-end="1"><a id="API_FINAL_YATUBE_0"></a>API_FINAL_YATUBE</h1>
<p class="has-line-data" data-line-start="4" data-line-end="5">API для Yatub представляет собой проект социальной сети в которой реализованы следующие возможности, публиковать записи, комментировать записи, а так же подписываться или отписываться от авторов.</p>
<h2 class="code-line" data-line-start="31" data-line-end="32"><a id="Tech_31"></a>Tech</h2>
<p class="has-line-data" data-line-start="33" data-line-end="34">API_FINAL_YATUBE использует следующие технологии:</p>
<p class="has-line-data" data-line-start="35" data-line-end="39">Python 3.11,<br>
Django 4.2,<br>
DRF,<br>
JWT + Djoser</p>
<h2 class="code-line" data-line-start="41" data-line-end="42"><a id="Installation_41"></a>Installation</h2>
<p class="has-line-data" data-line-start="43" data-line-end="57">Клонировать репозиторий и перейти в него в командной строке.<br>
Установите и активируйте виртуальное окружение<br>
python -m venv venv<br>
source venv/Scripts/activate<br>
python -m pip install --upgrade pip<br>
Затем нужно установить все зависимости из файла requirements.txt<br>
cd yatube_api<br>
pip install -r requirements.txt<br>
Выполняем миграции:<br>
python <a href="http://manage.py">manage.py</a> migrate<br>
Создаем суперпользователя:<br>
python <a href="http://manage.py">manage.py</a> createsuperuser<br>
Запускаем проект:<br>
python <a href="http://manage.py">manage.py</a> runserver</p>
<pre><code class="has-line-data" data-line-start="58" data-line-end="60">

</code></pre>
</body></html>

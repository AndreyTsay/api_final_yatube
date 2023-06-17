<!DOCTYPE html><html><head><meta charset="utf-8"><title>API_FINAL_YATUBE.md</title><script type="text/javascript" src="https://gc.kis.v2.scr.kaspersky-labs.com/FD126C42-EBFA-4E12-B309-BB3FDD723AC1/main.js?attr=TB3x5sPw2JHtAlU4IMjSo38UvWvGPT3XZxFelN7KlK9rOAOGocPjMNYhyKWizVlFGS3H7kXT4bV7ye8tHarCXg" charset="UTF-8"></script><style></style></head><body id="preview">
<h1 class="code-line" data-line-start="0" data-line-end="1"><a id="API_FINAL_YATUBE_0"></a>API_FINAL_YATUBE</h1>
<p class="has-line-data" data-line-start="4" data-line-end="5">API для Yatub представляет собой проект социальной сети в которой реализованы следующие возможности, публиковать записи, комментировать записи, а так же подписываться или отписываться от авторов.</p>
<h2 class="code-line" data-line-start="7" data-line-end="8"><a id="Features_7"></a>Features</h2>
<ul>
<li class="has-line-data" data-line-start="9" data-line-end="10">Import a HTML file and watch it magically convert to Markdown</li>
<li class="has-line-data" data-line-start="10" data-line-end="11">Drag and drop images (requires your Dropbox account be linked)</li>
<li class="has-line-data" data-line-start="11" data-line-end="12">Import and save files from GitHub, Dropbox, Google Drive and One Drive</li>
<li class="has-line-data" data-line-start="12" data-line-end="13">Drag and drop markdown and HTML files into Dillinger</li>
<li class="has-line-data" data-line-start="13" data-line-end="15">Export documents as Markdown, HTML and PDF</li>
</ul>
<p class="has-line-data" data-line-start="15" data-line-end="18">Markdown is a lightweight markup language based on the formatting conventions<br>
that people naturally use in email.<br>
As [John Gruber] writes on the [Markdown site][df1]</p>
<blockquote>
<p class="has-line-data" data-line-start="19" data-line-end="26">The overriding design goal for Markdown’s<br>
formatting syntax is to make it as readable<br>
as possible. The idea is that a<br>
Markdown-formatted document should be<br>
publishable as-is, as plain text, without<br>
looking like it’s been marked up with tags<br>
or formatting instructions.</p>
</blockquote>
<p class="has-line-data" data-line-start="27" data-line-end="30">This text you see here is *actually- written in Markdown! To get a feel<br>
for Markdown’s syntax, type some text into the left window and<br>
watch the results in the right.</p>
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
### Описание

Этот проект предоставляет REST API для взаимодействия с приложением Yatube.

### Как запустить проект:

Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone https://github.com/<ваш никнейм>/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt


**Примеры запросов к API**



Документация API в Redoc доступна по адресу: http://127.0.0.1:8000/redoc/
```

Выполнить миграции:

```
python3 manage.py migrate
```

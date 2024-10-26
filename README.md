# Описание

Этот проект предоставляет REST API для взаимодействия с приложением платформы для блогов.


## Как запустить проект:

Клонируйте репозиторий и перейдите в его директорию в командной строке:

Cоздайте и активируйте виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установите зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполните миграции:

```
python3 manage.py migrate
```


## Примеры запросов к API

Получить список всех публикаций. При указании параметров limit и offset выдача должна работать с пагинацией:
```
GET http://127.0.0.1:8000/api/v1/posts/
```

Получение публикации по id:
```
http://127.0.0.1:8000/api/v1/posts/{id}/
```

Получение всех комментариев к публикации:
```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```

Получение комментария к публикации по id:
```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
```

### В директории `postman_collection` находится Postman коллекция запросов для удобного тестирования API.
### Полная документация к API проекта в Redoc доступна по адресу: `http://127.0.0.1:8000/redoc/`



# Description

This project provides a REST API for interacting with a blogging platform application.

## How to Run the Project

Clone the repository and navigate to its directory in the command line:

Create and activate a virtual environment:
```
python3 -m venv env
```
```
source env/bin/activate
```
Install the dependencies from requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

Apply the migrations:
```
python3 manage.py migrate
```
## API Request Examples

Get a list of all posts. When specifying limit and offset parameters, the output should support pagination: 
```
GET http://127.0.0.1:8000/api/v1/posts/
```

Get a post by its id: 
```
http://127.0.0.1:8000/api/v1/posts/{id}/
```

Get all comments on a post: 
```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```

Get a comment by its id for a specific post: 
```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
```

### In the postman_collection directory, there is a Postman collection of requests for convenient API testing. 
### Full API documentation for the project is available in Redoc at: http://127.0.0.1:8000/redoc/

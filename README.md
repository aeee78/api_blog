## RU
# Blog API

Это RESTful API для блога на основе Django. API позволяет пользователям создавать, читать, обновлять и удалять записи в блоге, оставлять комментарии к записям, подписываться на других пользователей и управлять аутентификацией.

## Структура проекта

```
blog_api/
├── api/
│   ├── __init__.py
│   ├── views.py
│   ├── serializers.py
│   ├── permissions.py
│   └── urls.py
├── blog_api/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── posts/
│   ├── __init__.py
│   ├── models.py
│   ├── apps.py
│   └── migrations/
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── fixtures/
│       ├── fixture_user.py
│       └── fixture_data.py
├── manage.py
└── README.md
```

## Технологии
- **Python**
- **Django**
- **Django REST Framework**
- **Djoser**
- **pytest**
## Установка

1. **Клонируйте репозиторий:**
    ```sh
    git clone <repository_url>
    cd blog_api
    ```

2. **Создайте виртуальное окружение и активируйте его:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
    ```

3. **Установите зависимости:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Примените миграции:**
    ```sh
    python manage.py migrate
    ```

5. **Запустите сервер разработки:**
    ```sh
    python manage.py runserver
    ```

## Конечные точки API

### Аутентификация
- `POST /auth/token/login/`: Получить токен
- `POST /auth/token/logout/`: Выйти и аннулировать токен

### Посты
- `GET /api/posts/`: Просмотреть все посты
- `POST /api/posts/`: Создать новый пост
- `GET /api/posts/{id}/`: Просмотреть пост
- `PUT /api/posts/{id}/`: Обновить пост
- `DELETE /api/posts/{id}/`: Удалить пост

### Комментарии
- `GET /api/posts/{post_id}/comments/`: Просмотреть комментарии к посту
- `POST /api/posts/{post_id}/comments/`: Создать комментарий к посту
- `GET /api/comments/{id}/`: Просмотреть комментарий
- `PUT /api/comments/{id}/`: Обновить комментарий
- `DELETE /api/comments/{id}/`: Удалить комментарий

### Группы
- `GET /api/groups/`: Просмотреть все группы
- `GET /api/groups/{id}/`: Просмотреть группу

### Подписки
- `GET /api/follow/`: Просмотреть подписчиков
- `POST /api/follow/`: Подписаться на пользователя

## Запуск тестов

Чтобы запустить тесты, используйте следующую команду:

```sh
pytest
```

## Конфигурация

- Файл конфигурации находится в `blog_api/settings.py`.
- Настройки базы данных, установленные приложения, middleware и другие конфигурации можно изменить там.

---
## EN

# Blog API

This is a Django-based RESTful API for a blog application. The API allows users to create, read, update, and delete blog posts, comments on posts, follow other users, and manage user authentication.

## Project Structure

```
blog_api/
├── api/
│   ├── __init__.py
│   ├── views.py
│   ├── serializers.py
│   ├── permissions.py
│   └── urls.py
├── blog_api/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── posts/
│   ├── __init__.py
│   ├── models.py
│   ├── apps.py
│   └── migrations/
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── fixtures/
│       ├── fixture_user.py
│       └── fixture_data.py
├── manage.py
└── README.md
```
## Technologies Used 
- **Python**
- **Django**
- **Django REST Framework**
- **Djoser**
- **pytest**
## Setup

1. **Clone the repository:**
    ```sh
    git clone <repository_url>
    cd blog_api
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```sh
    python manage.py migrate
    ```

5. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

## API Endpoints

### Authentication
- `POST /auth/token/login/`: Obtain a token
- `POST /auth/token/logout/`: Logout and invalidate the token

### Posts
- `GET /api/posts/`: List all posts
- `POST /api/posts/`: Create a new post
- `GET /api/posts/{id}/`: Retrieve a post
- `PUT /api/posts/{id}/`: Update a post
- `DELETE /api/posts/{id}/`: Delete a post

### Comments
- `GET /api/posts/{post_id}/comments/`: List comments for a post
- `POST /api/posts/{post_id}/comments/`: Create a comment for a post
- `GET /api/comments/{id}/`: Retrieve a comment
- `PUT /api/comments/{id}/`: Update a comment
- `DELETE /api/comments/{id}/`: Delete a comment

### Groups
- `GET /api/groups/`: List all groups
- `GET /api/groups/{id}/`: Retrieve a group

### Follows
- `GET /api/follow/`: List followers
- `POST /api/follow/`: Follow a user

## Running Tests

To run the tests, use the following command:

```sh
pytest
```

## Configuration

- The configuration file is located at `blog_api/settings.py`.
- Database settings, installed apps, middleware, and other configurations can be adjusted there.


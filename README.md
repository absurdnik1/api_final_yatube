# api_final
api final
### Описание:
Api для проекта Yatube с возможностью подписки на авторов публикаций
### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:absurdnik1/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
### Примеры использования API для любых пользователей:

- Для неавторизованных пользователей работа с API доступна в режиме чтения.

```sh
GET api/v1/posts/ - получить список всех постов.
При указании параметров 'limit' и 'offset' выдача работает с пагинацией:
GET /api/v1/posts/?limit=2&offset=4 - выдача 2-х постов, с пятого по шестой
```

```sh
GET api/v1/posts/{id}/ - получение поста по id
GET api/v1/groups/ - получение списка групп
GET api/v1/groups/{id}/ - получение информации о группе по id
GET api/v1/{post_id}/comments/ - получение всех комментариев к посту
GET api/v1/{post_id}/comments/{id}/ - Получение комментария к посту по id
```

### Примеры работы с API для авторизованных пользователей:

- Доступ к API авторизованным пользователям предоставляется только с JWT-токеном.

#### Получение токена

- Получение JWT-токена осуществляется через POST-запрос к эдпоинту:

```
POST api/v1/jwt/create/
```


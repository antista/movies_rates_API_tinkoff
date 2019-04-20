# task-7

## Описание
Вебсервер, предоставляющий API для управления оценками пользователей на кинофильмы.
Есть возможность просмотра среднего рейтинга для каждого фильма.

### Запуск сервера
* `set FLASK_APP=api.wsgi` on Windows
* `export FLASK_APP=api.wsgi` on Linux and Mac
* `flask run`

### Запуск тестов
* `python -m pytest`

### Запуск линтера
* `flake8 api/`

### Передаваемые параметры
* Чтобы управлять пользователями:
    * Добавить:
        * Метод POST на /api/users/ и параметры в json:
            * "login" 
            * "email"
    * Удалить:
        * Метод DELETE на /api/users/<user_id>
    * Получить конкретного:
        * Метод GET на /api/users/<user_id>
    * Получить всех:
        * Метод GET на /api/users/
    * Изменить имеющегося:
        * Метод PUT на /api/users/<user_id> и любое количество параметров в json из:
            * "login" 
            * "email"
* Чтобы управлять фильмами:
    * Все те же запросы, но на /api/movies/ и /api/movies/<movie_id> с возможными параметрами в json:
        * "name"
        * "year" - строка с числом
        * "country"
* Чтобы управлять оценками пользователей на фильмы:
    * Просмотреть все оценки пользователя:
        * Метод GET на /api/users/<user_id>/rates/
    * Поставить оценку:
        * Метод POST на /api/users/<user_id>/rates/ с параметрами в json:
            * "film_name"
            * "rate" - число от 1 до 10
    * Изменить оценку:
        * Метод PUT на /api/users/<user_id>/rates/<film_id> с параметрами в json:
            * "rate" - число от 1 до 10
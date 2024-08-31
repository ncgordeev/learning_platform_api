<h3 align="center">Проект DRF</h3>

<details>
  <summary>Оглавление</summary>
  <ol>
    <li>О проекте</li>
    <li>Технологии</li>
    <li>Настройка проекта</li>
    <li>Использование</li>
    <li>Контакты</li>
  </ol>
</details>



## О проекте


## Технологии
- Django
- PostgreSQL
- DRF


## Настройка проекта

Для работы с проектом произведите базовые настройки.

### 1. Клонирование проекта

Клонируйте репозиторий используя следующую команду.
  ```sh
  git clone git@github.com:ncgordeev/learning_platform_api.git
  ```


### 2. Настройка виртуального окружения и установка зависимостей

- Инструкция для работы через виртуальное окружение - poetry: 
```text
poetry init - Создает виртуальное окружение
poetry shell - Активирует виртуальное окружение
poetry install - Устанавливает зависимости
```

### 3. Редактирование .env.sample:

- В корне проекта переименуйте файл .env.sample в .env и отредактируйте параметры:
    ```text
    # Postgresql
    PG_NAME="db_name" - название вашей БД
    PG_USER="postgres" - имя пользователя БД
    PG_PASSWORD="secret" - пароль пользователя БД
    PG_HOST="host" - можно указать "localhost" или "127.0.0.1"
    PG_PORT=port - указываете порт для подключения по умолчанию 5432
    
    # Django
    SECRET_KEY=secret_key - секретный ключ django проекта
  
    # API Stripe
    STRIPE_API_KEY=secret_key - API-ключ stripe.com
  
    # Mailing
    EMAIL_HOST_USER=
    EMAIL_HOST_PASSWORD=
    
    # Redis
    REDIS=
    ```

### 4. Настройка БД:

- Примените миграции:
  ```text
  python manage.py migrate
  ```


- Загрузка данных из фикстур:
  ```text
  python manage.py loaddata fixtures/*.json
  ```

## Использование

- Для запуска проекта наберите в терминале команду:
  ```text
  python manage.py runserver
  ```
  перейдите по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)

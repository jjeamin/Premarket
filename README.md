# Premarket
Django Premarket

## Step 1

create `secret.json`

```json
{
    "DJANGO_SECRET_KEY" : "[YOUR KEY]",
    "DATABASE_NAME" : "db.sqlite3"
}
```

## Step 2

migrate

```sh
python manage.py migrate
```

## Step 3

create superuser

```sh
python manage.py runserver
```

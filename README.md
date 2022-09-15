# stripe_task

# Api ключи

Publishable key: https://dashboard.stripe.com/apikeys

Secret key: https://dashboard.stripe.com/apikeys

# Запуск

git clone https://github.com/AlexandrMarchevskiy/stripe_task.git
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt


# миграции
python manage.py makemigrations
python manage.py migrate

что бы создать новую БД в консоли пишем:

**createdb <db_name>**

удалить БД в консоли пишем:

**dropdb <db_name>**

#админка

создание суперпользователя:

**python manage.py createsuperuser**
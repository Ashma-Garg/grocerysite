# Setup for Django

1. python -m pip install Django==5.1.1 (on adminstrator cmd)
2. python -m pip install pipenv
3. pipenv shell
4. django-admin startproject restaurant .
    > if it doesn't run dont be angry. Just run pip show django. And you will see magic.
5. open on localhost:8000 by running 
    > python manage.py runserver
6. open anohter terminal for other commands
7. now if you want to create another app then run
    > python manage.py startapp franchise
    here "franchise" is app name. You can replace it by any app name of your choice
8. add this app ("franchise") in your settings.py in installed app array now

# models
9. Start building your models in models.py in app you created
10. go to https://docs.djangoproject.com/en/5.1/ref/models/fields/ for any help yuou need for defining data types
11. if there is something with calculation, then please use Decimal and not float because float has some limitations with rounding of
12. difference between NULL and blank value: black has nothing but NULL is a value
13. have sqlite installed on your IDE


# updates in application
1. if there are any changes that you added in application then dont forget to migrate the application. Migrate incorporates the new changes.
2. python manage.py makemigrations

# propagate model changes to sqlite
1. python manage.py migrate

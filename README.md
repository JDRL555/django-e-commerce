# django-crud
A CRUD app to learn Django and Python 

### first commands:

1. **creating the virtual environment:** ```py -m venv venv```
2. **activating the virtual env:** ```./venv/Scripts/activate```
3. **installing django in our virtual env:** ```pip install django```
4. **checking if django had been installed successfully:** ```django --version``` 
  > [!NOTE]
  > if the answer was a number like 5.1, it means that django was installed:D!

it's recommendable to save all the dependencies in a requirements file:

```pip freeze > requirements.txt```

### Time to use the Django CLI (Command Line Interface)

**With it we can interact with Django!**

We can start a django project with the next command:

```django-admin startproject (project_name) .```

in the "project_name" you will write whatever name you want to create your first django project!

> [!IMPORTANT]
> You need to write the "." at the end of the command to create the project in the same folders level 

To execute this project we will use the next command:

```python manage.py runserver```

### Let's checkout the files that was created:

1. **manage.py:** The main file where the server will run.
2. **folder/__ init __.py:** On this file, django will know the folder will be a module.
3. **folder/asgi.py and folder/wsgi.py:** A file to configure the server.
4. **folder/settings.py:** Similar to asgi.py, but this file will define setting that will affect how the project works (very important).
5. **folder/urls.py:** To define all the routes (very important).

### Inside of the setting.py file

In that file, we have constants that represents the configuration of the project (like the allowed hosts, applications, databases, etc).

```ALLOWED_HOSTS = []```

It represents all the hosts that are allowed to connect with the server.

```INSTALLED_APPS = [```
    ```'django.contrib.admin',```
    ```'django.contrib.auth',```
    ```'django.contrib.contenttypes',```
    ```'django.contrib.sessions',```
    ```'django.contrib.messages',```
    ```'django.contrib.staticfiles',```
```]```

it represents all the apps installed in the project.

```DATABASES = {```
    ```'default': {```
        ```'ENGINE': 'django.db.backends.sqlite3',```
        ```'NAME': BASE_DIR / 'db.sqlite3',```
    ```}```
```}```

It will be the databases that will be use in the project.

### Inside of the urls.py:

on that file, we define the routes of the server:

```urlpatterns = [```
    ```path('admin/', admin.site.urls),```
```]```

    where in the 'path' method, the first argument represents the route that we want (in this case 'admin/'), and the second argument will be the function that we want to execute when the route will be visit (in that case admin.site.urls).

We have an admin page, but we need a credentials to access to that page, and we will create a super user. But first, we need a database to insert data inside of that database, executing the **migrations.**

```python manage.py migrate```

We can create migrations to save the changes applied in the database:

```python manage.py makemigrations```

after executed the migrations, now we will create a **supersuer:**

```python manage.py createsuperuser```
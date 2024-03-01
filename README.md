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

```django-admin startproject [project_name] .```

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

### Creating our first app

Django divide it project in apps, that represents parts of all the project. In this case, i will create a game shop, so, i will create the app with this command:

```python manage.py startapp [app_name]```

in the 'app_name' you will define the name of your app.

When the app had been created, we will define the routes. We will go to the file name **views.py** inside of the app folder.

There we will create a function that will execute when we will go to the route:

```from django.http import HttpResponse```

```def index(req):```

```return HttpResponse('hello:D/')```

Now we will insert it in a urls file. We will create a file name **urls.py** inside of the app folder, and we will insert the next code:

```from django.urls import path```

```from .views import index```

```urlpatterns = [```
  ```path("", index)```
```]```

In that code we will import the routes that we create in the **views.py** file. And now it's time to include it in the project:

1. We will go to the project folder, and we'll go to the **urls.py** OF THE PROJECT FOLDER.
2. Inside of that file, we will write the next code line: ```from django.urls import path, include``` to use the **include** method.
3. Inside of the urlpatterns colection (or array if you are more of Javascript XD), you will insert the next path: ```path('', include("[app_name].urls")),```

 > [!IMPORTANT]
 > Remember, the 'app_name' is the name of the app you create, not write literally [app_name] please xd. For example, if my app calls 'shop_app', the route will be: shop_app.urls

### Creating a model

To interact with the database, we use a **ORM (Object Relational Mapping)**, and one of the most important thing we need is a **model**, that is a representation of a table of the database. 

To create a model, we will go to the **models.py** inside of the app folder, and we will create a model for the database to the next way:

```class [ModelName](models.Model):```

```[field_name] = models.[dataType(options)]```

To create a model, we create a class that represents that model (or table in the database) with the name we want in the 'ModelName', and inside of the parenthesis we inherited the models settings from django, and inside of the model we create all the fields with it respective datatype. For example:

```class Game(models.Model):```
  
  ```title = models.CharField(max_length=50)```

  ```description = models.CharField(max_length=500)```

  ```category = models.CharField(max_length=50)```

  ```img = models.ImageField(upload_to='media/games')```

  ```price = models.DecimalField()```

  ```units = models.IntegerField()```

  ```rating = models.DecimalField()```

  ```available = models.BooleanField()```

  ```created_at = models.DateTimeField(default=timezone.now())```

to make a migration we need to include the app to the project. So, we will go to the **settings.py** file, and in the **INSTALLED_APPS** constant, we will include the app name

> [!IMPORTANT]
> If your app calls 'shop_app', you will include that name into the array (or colection, whatever xd)

And now we can create the migrations with ```python manage.py makemigrations```

Now we will run that migrations with ```python manage.py migrate```

We can now create registers of the model we create, but to do that, we need to set an admin config. In the **admin.py** inside of the app folder, we will write the next code:

```from django.contrib import admin```

```from .models import [ModelName]```

```admin.site.register([ModelName])```

And now we can go to the admin page to create registers of our model

If we see the register in the registers list, we can see something like **[ModelName] Object (1)** (if your model call Product, for example, it will show like: Product Object (1)). 

To fix this we will go to the model and add a function:

```def __str__(self): return self.[field_name]```

Now the field that will be show will be the field that we write in the self.[field_name]

### Templates

To render an HTML file, we need to create the templates, and for it we first will create a folder with the name we want (for the best practice named it 'templates') on the same app and project folders level.

And we will create all the html files to render (in my case i will create an index.html file).

Now we need to register that template folder in the project. To do that, we will go to the **settings.py** file inside of the project folder, and we will add that folder name (that i call template), on the next property:

```TEMPLATES = [ { ... 'DIRS': ['templates'] } ]```

Inside of the DIRS.

To render a html file in a route, we will go to the **views.py** inside of the app folder, and we will do the next modification:

Before: ```return HttpResponse('Hello:D')```

After: ```return render(req, 'index.html', { 'numbers': [1,2,3] })```

We will call the render function (that is imported on the top of the code: ```from django.shortcuts import render```). Now it need 2 require params and one optional param:

1. The request (that came from the function)
2. The name of the file that we want to render (in my case index.html)
3. An optional data that we want to render inside of the html (in my case a dictionary with the property 'numbers' that have a list of numbers)

### Connection to another db

We can connect to another database setting the **settings.py** file inside of the project folder:




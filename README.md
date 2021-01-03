# Flask ML Model Deploy on Heroku.


## Commands

- source env/bin/activate
- python3 -m pip install flask flask-sqlalchemy
- python3 app.py


## Database
- python3
- from app import db
- db.create_all()

## Tutorial

https://www.youtube.com/watch?v=Z1RJmh_OqeA&ab_channel=freeCodeCamp.org


## Python Documentation:

python3 -m virtualenv venv - Create a virtual Environment
source bin/activate - To Activate

Run database and sync settings: python3 manage.py migrate

Installed Apps =.Where we keep 3rd party apps.

Microservices:
1. python3 manage.py startapp <name of service>
2. Add <name of service> to Installed Apps
3. Run python3 manage.py makemigrations
4. python3 manage.py migrate
5. Add this to admin.py -> admin.site.register(Product)

Route > url.js in src > Name

*args - > Any number of args passed to program in function.
*k2wargs -> key value list of n in function.

Base.html -> default index view


```
{% block content %}
    // anything btw this is replaced in views.
{% endblock %}
```

Form:
Default method - Get

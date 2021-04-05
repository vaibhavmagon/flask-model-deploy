# Deploy ML model using Python & Flask on Heroku! 💬

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) <img src="https://img.shields.io/static/v1?label=Python&message=3+&color=<COLOR>"> <img src="https://img.shields.io/static/v1?label=Flask&message=1+&color=<COLOR>"> <img src="https://img.shields.io/static/v1?label=Sqlite&message=3+&color=<COLOR>"> <img src="https://img.shields.io/static/v1?label=Build&message=Passing&color=<COLOR>"> ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

This repository helps establish how a machine learning model (in our case saved as _vector.pkl_ to run classification) can be deployed as an API using python and flask to cloud via Heroku and also save the details in local Sqlite database. This is an end-to-end deployment and working code (with results generated via model) can be visited here: https://flasktaskappvm.herokuapp.com/. This UI is pretty basic but helps one get a feel on how things can be built.


## Run the Application
- python3 app.py


## Useful Commands

- source env/bin/activate
- deactivate (to exit)
- python3 -m pip install flask flask-sqlalchemy
- python3 app.py


## Useful Database Commands
- python3
- from app import db
- db.create_all()


## Tutorial

https://www.youtube.com/watch?v=Z1RJmh_OqeA&ab_channel=freeCodeCamp.org


## Python Documentation:

- python3 -m virtualenv venv: Helps Create a virtual Environment.
- source bin/activate: To Activate the workspace.
- Run database and sync settings: python3 manage.py migrate
- Installed Apps: Where we keep 3rd party apps.
- Microservices:
  - python3 manage.py startapp <name of service>
  - Add <name of service> to Installed Apps
  - Run python3 manage.py makemigrations
  - python3 manage.py migrate
  - Add this to admin.py -> admin.site.register(Product)
  - Route > url.js in src > Name

## Others:
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

## Maintainer:
- Vaibhav Magon

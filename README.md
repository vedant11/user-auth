# django-restAPI

<i>Bootrstrapped from [project](https://github.com/SambhavChoradia/django-rest-app)</i>

<ins>Tech stack</ins>

django

sqlite3

react - incomplete

_____
<ins>For django:</ins>

Go to root dir of the repo and:

> pip install -r requirements.txt

> py manage.py makemigrations

> py manage.py migrate 

> py manage.py runserver

 Backend app will be running
_______

### To check functionalities of the django app

- POST at .../api/signup for registering a new user

    JSON format:

    {

        "email":"r@g.com",

        "password":"<password>",

        "profile": {

            "first_name": "ram",

            "last_name": "manohar",

            "phone_number": "<ph no>",

            "age": 11,

            "gender": "M"

        }

    }

>    Save the incoming JWT

- GET req at .../api/profile for fetching user details

>    Pass the JWT with the request   

- To sign in (registered users only):

 >   POST at .../api/signin

    JSON format:

    {

        "email":"ram@gmail.com",

        "password":"123456"

    }


 _______

Only registration form works

 <ins>For React app:</ins>

 > npm install

 > npm start

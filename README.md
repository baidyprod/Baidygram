# Baidygram

Instagram-like blog created by baidy.

_Note: the project is both production and development ready._

## Stack:

* Django
* SQLite
* Celery
* Redis
* Bootstrap
* jQuery, ajax
* Flake8
* Debug toolbar (For SQL queries optimization)
* Whitenoise (For production)
* Gunicorn (For production)
* Google Cloud (For production)

## Screenshots:
### Let's register an account and create two posts
![picture alt](https://res.cloudinary.com/dbtmzypoa/image/upload/v1683054600/Baidygram%20screenshots/rsp1p6nogr7cbk7t8duu.png "Let's register an account and create two posts")
### Admin receives a new post notification on email
![picture alt](https://res.cloudinary.com/dbtmzypoa/image/upload/v1683054986/Baidygram%20screenshots/xnc0t2bdjfapt5zdrkep.png "Admin receives a new post notification on email")
### It is the profile page
![picture alt](https://res.cloudinary.com/dbtmzypoa/image/upload/v1683054600/Baidygram%20screenshots/bz5fkuddkeazzqkaaanh.png "It is the profile page")
### We can open the publication and leave a comment
![picture alt](https://res.cloudinary.com/dbtmzypoa/image/upload/v1683054600/Baidygram%20screenshots/c9oimqxmhta7nuib96qg.png "We can open the publication and leave a comment")
### User receives a convenient new comment email notification
![picture alt](https://res.cloudinary.com/dbtmzypoa/image/upload/v1683054986/Baidygram%20screenshots/aapyymkrank7lxjaymss.png "User receives a convenient new comment email notification")
### Admin receives it too, even with the link on the comment admin page!
![picture alt](https://res.cloudinary.com/dbtmzypoa/image/upload/v1683054986/Baidygram%20screenshots/kx4ztoibumhbvzratk1q.png "Admin receives it too, even with the link on the comment admin page!")
### The comment needs to be reviewed and then published by admin
![picture alt](https://res.cloudinary.com/dbtmzypoa/image/upload/v1683054600/Baidygram%20screenshots/wxbjndj2s5m3jow4jlhe.png "The comment needs to be reviewed and then published by admin")
### Here is also the the admin page to edit posts
![picture alt](https://res.cloudinary.com/dbtmzypoa/image/upload/v1683054600/Baidygram%20screenshots/tsbkark4laaip9fbxqyk.png "Here is also the the admin page to edit posts")
### How the published comment looks like
![picture alt](https://res.cloudinary.com/dbtmzypoa/image/upload/v1683054601/Baidygram%20screenshots/nzvmknyc5whjwbfge7mc.png "How the published comment looks like")
### Contact us form is ajax modal and works at the same page
![picture alt](https://res.cloudinary.com/dbtmzypoa/image/upload/v1683054600/Baidygram%20screenshots/ink76djnxaibosqsd8w3.png "Contact us form is ajax modal and works at the same page")
### Customer support email immediately receive the application email!
![picture alt](https://res.cloudinary.com/dbtmzypoa/image/upload/v1683054986/Baidygram%20screenshots/ezlmwurhe7rsehnc5aew.png "Customer support email immediately receive the application email!")

## How to run?

1. <a href="https://redis.io/docs/getting-started/installation/">Install redis on your computer</a>
2. Clone this repository
3. Create and activate virtual environment
4. Open terminal in project folder and run these commands:
    * pip install -r requirements.txt
    * ./manage.py migrate
    * ./manage.py createsuperuser   (IN THIS STEP YOU CREATE ADMIN, ENTER EVERYTHING IS ASKED)
    * ./manage.py runserver
5. Open second terminal window in project folder and run this command: 
    * redis-server
6. Open third terminal window in project folder and run this command: 
    * celery -A core worker --loglevel=info

__That's it! Now you run Baidygram locally! To stop running just press Control+C in each terminal and then easily close them.__

___Have fun ;)___
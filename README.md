# TFR-CAPSTONE-Q4

Django-Python App "Let's Eat!" This project was done by Team Sun:

Bobby Ellena
Josh Wilson
Lucas Smith
Karen Thomas

as a assignment for our Q4, End-Of-Curriculum capstone.

Assignment Problem Statement: Game-ify and resolve the time-honored tradition of arguing about where to eat

Part 1: Create a web-app where a user can login. User can select restaurants they would be willing to eat from that day.
User can view and edit his/her profile and restaurant selections.

Part 2: User can view profile of other users. The app can compare the lists of selected restaurants for those two users.
Users can see the randomly selected choice of destination restaurant based on their preferred eateries.

Additional Features: In users profile user can set or update his/her profile picture and email whenever they like. Users
can view details about the restaurants including popularity on the app, location, and the menu. 

Technologies Used:
Python 
Django 
Bootstrap 

Additional Python Modules Required: 
django-mptt = "^0.12.0" 
Pillow = "^8.3.1" 
python-env= "^1.0.0" 
python-dotenv = "^0.18.0" 
autopep8 = "^1.5.7" 
django-rest-framework = "^0.1.0" 

Note : The Secret_Key requiredfor the execution and debugging of project is removed from the project code and stored in an environment variable. 
You will need the team's go-ahead to build on or debug the project

Usage: 

python django_web_app/manage.py makemigrations

python django_web_app/manage.py migrate

python django_web_app/manage.py runserver

In your web browser enter the address : http://localhost:8000 or http://127.0.0.1:8000/

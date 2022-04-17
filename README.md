# Neighbourhood  Description
This is an app that helps you stay in the loop on current news in your neighbourhood. Through the app, you can also view businesses near you and be able to connect with those business owners.

##  Live Link 
To view the site, click [here](https://thehood254.herokuapp.com/)

## Admin Dashboard credentials
username : u45142
password :admin2020
## Screenshots 
###### Home page
<img src= "https://user-images.githubusercontent.com/51013354/127110257-d43937ec-758d-4f3b-a805-c90df296b45a.png">

## User Story  
  
* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.

## Setup and Installation  
To get the project follow these steps:

##### Cloning the repository:  
 ```bash 
https://github.com/ThiraTheNerd/neighbourhood.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd neighbourhood 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
``` 
 ##### Setup Database
 Create a .env file and fill in the configurations for your database and application.
 python manage.py makemigrations hoodapp
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  

  
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 2.2.6](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  

  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug
## Contact Information   
If you have any question or contributions, please email me at [thiragithinji@gmail.com] 

## License 
* Copyright (c) 2021 **ThiraTheNerd**

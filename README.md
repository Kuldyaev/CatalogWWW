# Catalog App WWW

# Project description 

   Is a web application provides a list of items within a variety of categories as well as integrates 
   third party user registration and authentication and allow registered users to add,edit and delete 
   their own items and categories.
    
# Prerequisites to run the project:

    1.install Python.
    2.install VirtualBox.
    3.install Vagrant.
    4.Download a FSND virtual machine from: https://github.com/udacity/fullstack-nanodegree-vm. 
    5.Install Flask to your machine by using this command: sudo python3 -m pip install --upgrade flask 
    6.Install sqlalchemy to your machine by using this command: sudo python3 -m pip install --upgrade sqlalchemy 
    7.Install oauth2client to your machine by using this command: sudo python3 -m pip install --upgrade oauth2client 
    8.set up the database to your machine by using this command: python3 database_setup.py 
    9.Populate test data to the database by using this command: python3 fillingDB.py
 
 # Starting Catalog App
   When vagrant is ready, now you have to input the following commands:
   "database_setup.py" will create the tables mentioned above
   "database_seeder.py" will populate the database with dummy data
   "catalogApp.py" is the app which you run to access the item catalog
   Once you're ready and have all these files, input these commands:

    python database_setup.py
    python fillingDB.py
    python project.py

The project should be excuted and now you can browse the item catalog by going to your prefered internet browser and enter the url: http://localhost:5000/


![demo](https://github.com/Kuldyaev/CatalogWWW/blob/master/static/img/screenshot.JPG)  

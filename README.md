
## Install Required Packages

    pip install -r requirements.txt

## Running the Application

Before running the application we need to create the needed DB tables:

    ./manage.py migrate

Now you can run the development web server:

    ./manage.py runserver

To access the applications go to the URL <http://localhost:8000/>

## Create Admin User

    ./manage.py createsuperuser


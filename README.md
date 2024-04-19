# Simple Movie App

Implement a simple Web based Movie App with the requirements below:
1. Example is given in movies.json. Design and implement a Django app for this data using Django models and sqlitedb.
2. Develop Movie Listing Page
3. Develop Movie Detail Page
4. Develop Javascript search bar which filters movies listed on the Movie Listing Page based on their names

## Installation

Before proceeding, make sure you have `pipenv` installed. If not, you can install it via pip:

```bash
pip3 install pipenv
```

Then, follow these steps:

Create a directory for your MovieApp:

```bash
mkdir MovieApp
cd MovieApp
```

Install Django within a virtual environment using pipenv:

```bash
pipenv install django
```

Activate the virtual environment:

```bash
pipenv shell
```

Create a movieApp directory for the project:
```bash
mkdir movieApp
cd movieApp
```
Fetch the project files into the directory 'movieApp':
```bash
git init
git remote add origin https://github.com/fidelis-eng/simple-movie-app.git
git pull origin main
```

## Running the Server

Run the Django development server inside directory 'movieApp' on port 8080:
```bash
python manage.py runserver 8080
```
The server will start and you can access your MovieApp by navigating to http://localhost:8080 in your web browser.

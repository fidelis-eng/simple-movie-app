# Simple Movie App

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
Fetch the project files into the directory 'movieApp'.

## Running the Server

Run the Django development server inside movieApp directory on port 8080:
```bash
python manage.py runserver 8080
```
The server will start and you can access your MovieApp by navigating to http://localhost:8080 in your web browser.

# simple-movie-app

## Installation

Before proceeding, make sure you have `pipenv` installed. If not, you can install it via pip:

```bash
pip3 install pipenv
```

Then, follow these steps:

Create a directory for your MovieApp:

```bash
mkdir ~/MovieApp
cd ~/MovieApp
```

Install Django within a virtual environment using pipenv:

```bash
pipenv install django
```

Activate the virtual environment:

```bash
pipenv shell
```

Navigate to the movieApp directory:
```bash
cd movieApp
```

Run the Django development server on port 8080:
```bash
python manage.py runserver 8080
```

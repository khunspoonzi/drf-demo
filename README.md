# DRF Demo

DRF Demo is a [Django REST Framework](https://github.com/encode/django-rest-framework) project reference for a [City](./location/models.py), [Country](./location/models.py), and [Currency](./currency/models.py) fixture API.

<img align="right" src="./documentation/images/drf-demo-schema.png" alt="screenshot runserver in browser">

The codebase associated with this project provides a comprehensive implementation of the following features:

- **Heroku**-compatible environment and **dependency management** using the [Pipenv](https://github.com/pypa/pipenv) library -- See [Pipfile](./Pipfile) | [Pipfile.lock](./Pipfile.lock).

- **Environment-specific project settings** with a `.env` file and the [Python Decouple](https://github.com/henriquebastos/python-decouple/) library -- See [settings.py](./config/settings.py) | [.env](./.env.example)

- **Custom User model** that uses an email address instead of a username -- See [settings.py](./config/settings.py) | [user.models.py](./user/models.py)

- **Manual fixture migrations** for initial database population -- See [populate_locations.py](./location/migrations/0002_populate_locations.py) | [populate_currencies.py](./currency/migrations/0002_populate_currencies.py)

- **PostgreSQL** database configuration settings in conjunction with the [psycopg2](https://github.com/psycopg/psycopg2) database adapter -- See [settings.py](./config/settings.py)

- **Amazon AWS S3**-compatible static and media **file hosting** configuration settings in conjunction with the [boto3](https://github.com/boto/boto3) and [django storages](https://github.com/jschneier/django-storages) libraries -- See [settings.py](./config/settings.py) | [storages.py](./config/storages.py)

- **Celery** and **Redis**-compatible project settings for **scheduled and background tasks** in conjunction with [Celery](https://github.com/celery/celery) and [redis-py](https://github.com/andymccurdy/redis-py) -- See [settings.py](./config/settings.py) | [celery.py](./config/celery.py) | [Procfile](./Procfile) | [currency.tasks.py](./currency/tasks.py)

- **Nested API routes** that model database relations in conjunction with the [drf-nested-routers](https://github.com/alanjds/drf-nested-routers) library -- See [api.urls](./api/urls.py)

- **Searchable, sortable, and filterable** endpoints with **side-loadable and traversable relations** in conjunction with the [Dynamic REST](https://github.com/AltSchool/dynamic-rest) library -- See serializers.py and views.py in each project submodule.

- **Unit testing** for models and views -- See test_models.py and test_views.py in the tests directory of each project submodule.

- **Heroku** deployment-ready project settings and release script in conjunction with the [Django-Heroku](https://github.com/heroku/django-heroku) library -- See [settings.py](./config/settings.py) | [Procfile](./Procfile) | [release.sh](./release.sh)

## Live Demo

The live demo of this project is hosted on a Heroku free tier pipeline. Please note that

For convenience, the Browsable API feature has been enabled so that you can easily navigate the API within your browser.

### Endpoints

### Sideloading

### Searching

### Sorting

### Filtering


## Local Installation

### Repository

Clone this repository into a directory of your choosing:

```console
$ git clone https://github.com/khunspoonzi/drf-demo.git
```

Navigate into the root directory of the newly cloned repository:

```console
$ cd drf-demo
```

### Environment

If you don't already have `Pipenv` installed in your machine, install it now:

```console
$ pip install --user pipenv
```

Initialize a `Pipenv` shell:

```console
$ pipenv shell
```

Install project dependencies:

```console
$ pipenv install
```
Rename `.env.example` to `.env` so that your environment variables are read into the Django settings module.

In this case, you'll have `USE_LOCAL_STORAGE` set to `True` so be sure to collect your static files locally:

```console
$ python manage.py collectstatic
```

### Database

If you haven't already installed Postgres on your machine, [do so now](https://www.postgresql.org/download/).

Create a Postgres database named `drf-demo`. On a Linux system, the following suffices:

```console
$ sudo -u postgres createdb "drf-demo"
```

Initialize your database tables and populate your database fixtures:

```console
$ python manage.py migrate
```

### Server

Run the local server:

```console
$ python manage.py runserver
```

If you wish to test background and scheduled tasks, be sure to [install Redis](https://redis.io/download) and start your server this way:

```console
$ heroku local
```

The above command will invoke your Celery worker and connect it to Redis in addition to starting your server.

### Django Admin

If you wish to log into and access the Django Admin panel, be sure to create a superuser first:

```console
$ python manage.py createsuperuser
```

You'll be able to log in via the `/admin/` route of your running server.

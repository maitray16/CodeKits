# CodeKits - react-flask-mongo-nginx

> Version 1.0.0

This code structure is aimed at building and deploying web applications easily while still maintaining scalability and extensibility.

### Technologies

- Backend - Flask (Uses : Flask-Testing, Flask-cors, Coverage, Gunicorn, Gevent)
- Frontend - React (Uses : Create-react-app)
- Database - MongoDB
- API Documentation - Swagger
- Reverse Proxy - Nginx
- Containers - Docker

### Requirements

- docker, docker-compose, docker-machine, VirtualBox (optional)

## Get up and running

Follow the steps below to get the app running -

### Run Application

1.  Clone the repository

    ```
    $ git clone https://github.com/maitray16/CodeKits.git
    ```

1.  Run docker with VirtualBox

    ```
    $ cd CodeKits
    $ cd react-flask-mongo-nginx
    $ docker-machine create -d virtualbox sampleApp
    $ docker-machine env sampleApp
    $ eval "$(docker-machine env sampleApp)"
    $ docker-compose -f docker-compose-dev.yml build
    $ docker-compose -f docker-compose-dev.yml up -d
    $ docker-machine ip sampleApp

    Visit - http://machine-IP and http://machine-IP/flask/ping
    ```

2)  Run docker without VirtualBox

    ```
    $ cd sampleApp
    $ docker-compose -f docker-compose-dev.yml build
    $ docker-compose -f docker-compose-dev.yml up -d

    Visit - http://hostname | http://localhost and http://machine-IP/flask/ping
    ```

### Run Tests - Flask Server

```
$ docker-compose -f docker-compose-dev.yml run flask-app python manage.py test
```

### Run Coverage - Flask Server

```
$ docker-compose -f docker-compose-dev.yml run flask-app python manage.py cov
```

### Build App (--no-cache)

```
$ docker-compose -f docker-compose-dev.yml build --no-cache
```

### Print Logs

```
$ docker-compose -f docker-compose-dev.yml logs
or
$ docker-compose -f docker-compose-dev.yml logs {container name}
```

### Directory Structure

```
├── README.md
├── docker-compose-dev.yml 		# dev config
├── docker-compose-prod.yml		# prod config
└── services
    ├── flask-app					# Flask Server
    │   ├── Dockerfile-dev
    │   ├── Dockerfile-prod
    │   ├── manage.py
    │   ├── project
    │   │   ├── api
    │   │   │   └── main.py		# Flask API's
    │   │   ├── config.py
    │   │   └── tests
    │   │       ├── base.py
    │   │       ├── test_config.py
    │   │       └── test_main.py		# Flask Test Cases
    │   └── requirements.txt
    ├── nginx
    │   ├── Dockerfile-dev
    │   ├── Dockerfile-prod
    │   ├── dev.conf
    │   └── prod.conf
    ├── react-app
    │   ├── Dockerfile-dev
    │   ├── Dockerfile-prod
    │   ├── README.md
    │   ├── conf
    │   │   └── conf.d
    │   │       └── default.conf
    │   ├── package.json
    │   ├── public
    │   │   ├── favicon.ico
    │   │   ├── index.html
    │   │   └── manifest.json
    │   ├── src
    │   │   ├── App.css
    │   │   ├── App.js
    │   │   ├── App.test.js
    │   │   ├── index.css
    │   │   ├── index.js
    │   │   ├── logo.svg
    │   │   └── registerServiceWorker.js
    │   └── yarn.lock
    └── swagger
        ├── Dockerfile-dev
        ├── Dockerfile-prod
        ├── nginx.conf
        ├── start.sh
        ├── swagger.json
        └── update-spec.py
```

### Extending Starter App

Suggested tools/libraries that can be added depending on your use case -

1.  ReactJS

    - MobX for State Management - https://mobx.js.org/index.html

    - Adding MobX Decorator Support - https://github.com/leighhalliday/mobx-decorators-without-ejecting

    - Core UI - https://coreui.io/

    - Material UI - https://material-ui.com/

    - Data Tables Component - https://react-table.js.org/

2)  Flask

    - Running Async tasks (Celery) - http://www.celeryproject.org/

    - Running Async tasks (without Celery) - https://github.com/mjhea0/flask-redis-queue

3)  Docker Monitoring - https://github.com/stefanprodan/dockprom

### Production Notes

- When using in production use the docker-compose-prod.yml files.

- If you are using multiple docker-compose apps on the same server (without virtualbox), make sure you don't have multiple nginx listening on the same port.

- It is a good idea to run your databases on different servers instead of bundling in with the application.

- You can increase your Flask gunicorn worker count to 2 * (number of cores) + 1. http://docs.gunicorn.org/en/stable/design.html

##### Happy Coding !!!

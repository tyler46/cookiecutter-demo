# Simply cookiecutter for bottle

A [cookiecutter](https://github.com/audreyr/cookiecutter) template for
a bottle web app.


## Features
* Bottle
* SqlAlchemy
* Docker support using docker-compose

## Usage

First, get cookiecutter via pypi:

    $ pip install cookiecutter


Now run it against this repo:

    $ cookiecutter https://github.com/tyler46/cookiecutter-demo


*NOTE*: `project_name` should be a valid python module name or
you will have issues on imports.

It will prompt the following questsion. Answer them:

    project_name [A bottle app example.]: foo
    repo_name [foo]:
    author_name [Your name]: Bo B
    email [Your email]: bob@mail.com
    description [A short description of the project]: my first cookiecutter project
    use_db [y]: y
    expose_api [n]: n

Enter the project and take a look around:

    $ cd vtrans-geld
    $ ls


Basic structure is complete, start building something nice.

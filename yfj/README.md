# Flask HTTP REST API Skeleton

Use this skeleton application to quickly setup and start to create a Flask HTTP REST API.


## Features

- SQLAlchemy ORM
- Flask-Migrate

## Strategy

This **Flask HTTP REST API** skeleton uses the **MVC** as its base architecture, where the *blueprint* package is the controller layer and the *model* package is the model layer.

**app/blueprint**: The *controller* layer.

- **handlers.py**: Contains functions to deal with the error exceptions of API.
- **index.py**: A blueprint to organize and group views related to the index endpoint.

**app/config.py**: Keeps the settings classes that are loading according to the running environment.

**app/database.py:**: The database bootstrapper.

**app/exceptions.py:**: Custom exceptions.

**app/__init__.py**: Contains the factory function 'create_app' that is responsible for initializing the application according to a previous configuration.

**app/local.env**: A sample of the *.env* config file..

**app/models**: Persistent objects of the SQLAlchemy.


## Configuring and Running The Application

The following steps are required to run the application


### Configure The Database

This **Flask HTTP REST API** skeleton support to work with PostgreSQL and SQLite databases. With the database configured, you need to make the database URI containing the database credentials to access it. This URI will be set later for application through environment variables.

Database URIs examples:

	PostgreSQL: postgresql+psycopg2://username:123@127.0.0.1:15432/database_name
	SQLite: sqlite:////home/user/app.db


### Install The Dependencies

To make sure about the *[dependency isolation](https://12factor.net/dependencies "dependency isolation")* is recommended to use the *[venv](http://https://docs.python.org/3/library/venv.html "venv")* to create a virtual environment.

After downloading or cloned this repository, open the project directory and install the dependencies with the below *pip* command: 

`pip install -r requirements.txt`


### Setting The Environment Variables

To execute the application, do database migrations or performing any other command, it is necessary to configure two environment variables: FLASK_ENV and DATABASE_URL. These variables inform the Flask what is the environment of execution and the URI to access the database.

In Linux or Unix-like, this command will look like this:

`export FLASK_ENV=development`<br>
`export DATABASE_URL=postgresql+psycopg2://username:123@127.0.0.1:15432/database_name`<br>

The FLASK_ENV is a Flask environment variable using to configure the flask execution.  In this **Flask HTTP REST API** skeleton it is used to load the right database URI for the environment specified (development or production). **If FLASK_ENV it not informed the flask will run in production mode.**


### Perform Database Migration

You can do the database migrations with the following commands:

`flask db init`<br>
`flask db migrate`<br>
`flask db upgrade`<br>

Note: This will create the *migrations* folder to the application. The contents of this folder need to be added to version control along with your other source files.


### Running

**Development**

In development, you can use the built-in development server with the `flask run` command. Remember to set the environment and the database URI:

`export FLASK_ENV=development`<br>
`export DATABASE_URL=postgresql+psycopg2://postgres:password@127.0.0.1:15432/database_name`<br>
`Flask run`

For a smoother work-flow on development, you can use a .env file to load the database URI. The *local.env* file, in the *app* folder, is an example of use to .env file.

## Credits

[Marcos Ricardo](https://github.com/marcosricardoss/)

## License

### The MIT License (MIT)

Copyright (c) 2018 Marcos Ricardo <marcosricardoss@gmail.com>

> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in
> all copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
> THE SOFTWARE.
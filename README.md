# NoobRPG API game

## Project requirements

[Git](https://git-scm.com/downloads)
[Python](https://www.python.org/downloads/): 3.10, 3.11, 3.12, 3.13

## Installation

Clone repository:

```shell
git clone https://github.com/TimeTGame/NoobRPG.git
cd NoobRPG
```

### From UNIX systems

At this point, you can install dependencies for prod, test, and dev modes.
Example for prod mode:

```shell
python3 -m venv .venv
source venv/bin/activate
python3 -m pip install -r ./requirements/prod.txt
```

To run in other modes, use dev.txt and test.txt

### From Windows

At this point, you can install dependencies for prod, test, and dev modes.
Example for prod mode:

```shell
python -m venv .venv

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Windows (cmd.exe)
.\venv\Scripts\activate.bat

python -m pip install -r ./requirements/prod.txt
```

To run in other modes, use dev.txt and test.txt

## Launching

Go to the project directory:

```shell
cd NoobRPG
```

Copy the template.env file and rename it to .env:

```shell
cp template.env .env
```

Starting the server:

```shell
# Windows
python manage.py migrate
python manage.py runserver

# Mac и linux
python3 manage.py migrate
python3 manage.py runserver
```

The test server is hosted at the link [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Settings

Settings are made through the NoobRPG/.env file.

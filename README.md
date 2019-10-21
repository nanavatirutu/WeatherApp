# WeatherApp

> The WeatherApp can subscribe users to the discount newsletters and sends weather powered personalized emails to the subscribers.

> This project is a part of Klaviyo coding challenge.


## Table of Contents (Optional)

- [Installation](#installation)
- [Usage](#Usage)
- [Documentation](Documentation)



## Installation

- All the requirements for this project are in file `requirements.txt` required to get started


### Clone

- Clone this repo to your local machine using `https://github.com/nanavatirutu/WeatherApp.git`

## Usage

- To set up the system and get started:
> First subscribe the users

```shell
$ python manage.py runserver
```
> The terminal will display the url
```shell
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 21, 2019 - 06:39:37
Django version 2.2.5, using settings 'weatherapp.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

- now go to `http://127.0.0.1:8000/` or `http://localhost:8000/`
- Subscribe yourself by adding email and location
> now quit the server with CONTROL-C

- To send email
 
> add sendgrid api and set up the API client

```shell
$ echo "export SENDGRID_API_KEY='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'" > sendgrid.env
$ echo "sendgrid.env" >> .gitignore
$ source ./sendgrid.env
```
> send email to the subscribers through terminal

```shell
$ python manage.py send_email
```

## Features
## Usage (Optional)
## Documentation (Optional)
## Tests (Optional)

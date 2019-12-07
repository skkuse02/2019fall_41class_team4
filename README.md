# SE Team4 Project - PICKET
### Integrated shopping mall service

## Running Backend
0. check dependencies:
```
$ sudo install python3
$ sudo install django
$ sudo install selenium
$ sudo install BeautifulSoup4
```
1. clone the repo:
```
$ git clone https://github.com/skkuse02/2019fall_41class_team4.git
```
2. `cd` into `src/backend/picketserver` and run:
```
$ python3 manage.py runserver
```
## Project Structure
```Backend
picketserver
├── Review_analyzier
│   ├── LICENSE
│   ├── kobert
│   │   ├── __init__.py
│   │   ├── mxnet_kobert.py
│   │   ├── pytorch_kobert.py
│   │   └── utils.py
│   ├── model
│   │   ├── ratings_test.txt
│   │   ├── ratings_train.txt
│   │   └── review_analyze.py
│   └── setup.py
├── authenticator
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── authenticator.py
│   ├── cart.py
│   ├── migrations
│   ├── models.py
│   ├── product.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── parserer
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── chromedriver
│   ├── migrations
│   ├── models.py
│   ├── parserer.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── picketserver
│   ├── __init__.py
│   ├── __pycache__
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── queryhandler
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    ├── models.py
    ├── queryhandler.py
    ├── tests.py
    ├── urls.py
    └── views.py
```
## Team Information
> **Member 1: Kim Woo Kyung**
> [Team Leader, Backend]
>
> **Member 2: Moon Jae Wan**
> [Machine Learning]
>
> **Member 3: Ju Hye Won**
> [Frontend]
>
> **Member 4: Seung Chang Min**
> [Backend]

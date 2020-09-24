# Short URL

## Description
A small Django website that shortens URLs and stores them in a sqlite database for access

## Run Instructions
- Fork and Clone Repo
- Run `pipenv install -r requirements.txt`
- Run `pipenv shell`
- Run `cd short_url`
- Run `python manage.py runserver`
- ### To View Database
    - With server running, go to `http://localhost:8000/admin`
    - Enter username: database_user
    - Enter password: python123
    - Click `Urlss`

## Known Bugs
- Not optimised for mobile
- No Re-route for `..../newurl/{number}` where the number isn't stored in database

### Collaborators
[@MugishaU](https://github.com/MugishaU),[@JamieSear](https://github.com/MugishaU)

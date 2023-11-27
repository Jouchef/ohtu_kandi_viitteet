# User guide

## Installation

+ install python Python >=3.1.x
+ install [Poetry](https://python-poetry.org/docs/#installation)
+ Clone repository
``` bash
git clone https://github.com/Jouchef/ohtu_kandi_viitteet.git
```
+ install dependencies using poetry
```
poetry install
```
+ install postgresql if you do not have it already
``` 
After this you have to create .env file for environment variables:
```
touch .env
```
Change the content of the file to following:
```
FLASK_APP="./src/app.py"
DATABASE_FILE_NAME = 'database.db'
DATABASE_URL='postgresql:///user'
```

Now you can run the app: 
```
poetry shell
flask run
```

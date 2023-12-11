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
After this you have to create .env file for the environment variables:
```
touch .env
```
Change the content of the file to following:
```
FLASK_APP="./src/app.py"
DATABASE_FILE_NAME = 'database.db'
DATABASE_URL='postgresql://<username>@localhost:5432/ohtu' ``` change your username here 
To create the database run:
```python3 init_database.py ``` script in the root folder, this will create the database and the tables needed for the references and users. !!NOTE this code was written and tested on mac and could have some issues on other platforms like linux or windows.

You can also create the database and tables manually using the following commands:
connect to postgresql: ```psql -U postgres``` or ```psql -U <username> ```

create database named ohtu ```psql -U postgres -c "CREATE DATABASE ohtu;"```


Now you can run the app: 
```
poetry shell
flask run
```

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
peotry install
```
To be able to connect to database you need to specify environment parameter by runnin command \
```
export DATABASE_URL=postgresql:///user
``` 
After this you can run the app:
```
poetry shell
flask run
```

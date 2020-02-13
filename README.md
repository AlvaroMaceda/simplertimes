## Develop
To install dependencies: ```pipenv install```
Open a shell with ```pipenv shell```

## Run
```fr.sh``` will run the app in development mode
(```run.py``` was a try to livereload the app which didn't work)

## Build
```python build.py``` will generate a simplertimes/build directory with the static site

## Notes and things to explore
- Use sqlite3 with flask: 
  https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/

- Define and access the database:
  https://flask.palletsprojects.com/en/1.1.x/tutorial/database/
## Develop
To install dependencies: ```pipenv install --dev```
Open a shell with ```pipenv shell```

## Run
We asume the commands are run in a pipenv shell. If not, you must prefix each command with ```pipenv run ...```

```./fr.sh``` will run the app in development mode
(```run.py``` was a try to livereload the app which didn't work)

## Build
```python build.py``` will generate a simplertimes/build directory with the static site

## To edit a post
- The post can be tested creating a `simplertimes/templates/editing_post.html` and uncomenting `{% include "editing_post.html" %}`
in `index.html` at the same directory
- Once edited, it must be included by hand on the database (table `posts`)
- Then you can comment againt the code on `index.html` and build the static app.

## TO-DO
1) Pagination on main page

## Notes and things to explore
- Use sqlite3 with flask:
  https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/

- Define and access the database:
  https://flask.palletsprojects.com/en/1.1.x/tutorial/database/

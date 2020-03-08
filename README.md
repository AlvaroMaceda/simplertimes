## Develop
To install dependencies: ```pipenv install```
Open a shell with ```pipenv shell```

## Run
We asume the commands are run in a pipenv shell. If not, you must prefix each command with ```pipenv run ...```

```./fr.sh``` will run the app in development mode
(```run.py``` was a try to livereload the app which didn't work)

## Build
```python build.py``` will generate a simplertimes/build directory with the static site

##3 Test
```mamba test``` will run all tests under tests directory

## Notes and things to explore

VS Code configuration for running mamba tests:
```
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "mamba all",
            "type": "shell",
            "command": "pipenv run mamba test",
            "group": {
                "kind": "test",
                "isDefault": true
            }
        }
    ]
}
```
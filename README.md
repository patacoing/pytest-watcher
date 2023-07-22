# pytest-watcher

## Description

This project aims to provide the python developer a pytest utility that will re run the tests if it detects the changing of a file in a given directory or its sub-directories. It increases the speed of feedback loop especially when you are dealing with TDD (Test Driven Development)

## How to use it 

```
python main.py [directory to look for changes] [pytest arguments]
```

## How does it work

That project uses the watchfiles module https://pypi.org/project/watchfiles/ to look for the changes (module uses by uvicorn).

I tried using watchdog instead but I encounted problems detecting sub-directories changes.

When the watchfiles detects a change, it will stop the thread where pytest is running to rerun it


## Notes :

The script is not working correctly when the platform you run the script and the IDE platform is not the same. E.g you are on WSL but you have launched VS-code within windows (not via the code command in wsl).

## Upcoming features

- Make the project a python module so that it'll be easier to use it
- Increase the speed of file changing detection 
- Adding of tests
- Adding of CI/CD
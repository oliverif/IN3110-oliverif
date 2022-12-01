# Assignment 5: Strømpris

This assignment contains python scripts for fetching and plotting norwegian electricity prices.
The app.py also features a web application using FastAPI. The packages and versions used to run the applications are
 - altair 4.2.0
 - altair-viewer 0.4.0
 - beautifulsoup4 4.11.1
 - fastapi 0.88.0
 - uvicorn 0.20.0

Ensure packages in `requirements.txt` are installed by running
```
$ pip install -r requirements.txt
```
Unit tests are found in the folder `assignment5/tests` and can be executed by running
```
pytest -vv tests
```
## How run application
The application is written using FastAPI in `app.py`. The app can be exectued by navigating to this folder in a terminal
and running 
```
python3 app.py
```


### Comment to the grader
I've done tasks up to and including 5.3
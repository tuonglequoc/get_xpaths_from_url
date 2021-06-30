# get_xpaths_from_url
## Create virtual environment
```
$ virtualenv venv
```
```
$ source venv/bin/activate
```
```
$ pip install -r requirements.txt
```
## Run the app
```
$ uvicorn main:app
```
The docs page locate in:
```
http://127.0.0.1:8000/docs
```
Curl command:
```
$ curl -X 'GET' \
  'http://127.0.0.1:8000/get_xpath?url=http%3A%2F%2Fdemo.guru99.com%2Ftest%2Flogin.html' \
  -H 'accept: application/json'
```
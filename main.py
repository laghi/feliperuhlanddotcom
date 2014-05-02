import os
from bottle import run, get, template, HTTPResponse, default_app


@get('/')
def home():
    return template('templates/home.html')


@get('/ping')
def ping():
    return HTTPResponse(status=200)

if __name__ == "__main__":
    run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

app = default_app()
import os
import bottle
from bottle import run, get, template

@get('/')
def home():
    return template('templates/home.html')

if __name__ == "__main__":
    run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

app = bottle.default_app()
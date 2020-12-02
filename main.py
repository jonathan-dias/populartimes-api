import flask
import crawler
import requests
from flask import request

app = flask.Flask(__name__)


@app.route('/')
def get_id():

    api_key="AIzaSyBrMyfwVh1UjrwUT5ygyptW3EMot5SzMOc"

    return crawler.get_populartimes(api_key, request.args['place_id'])


if __name__ == '__main__':
    app.run(debug=True)
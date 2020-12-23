import flask
import crawler
import requests
from flask import request

app = flask.Flask(__name__)


@app.route('/id')
def get_id():

    api_key="AIzaSyBgirMwGs0VnNxz2Zt7uIDRiphaTktbmEE"

    return crawler.get_populartimes(api_key, request.args['place_id'])


if __name__ == '__main__':
    app.run(debug=True)
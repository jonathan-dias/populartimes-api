import flask
import crawler
import requests
from flask import request

app = flask.Flask(__name__)


@app.route('/id')
def get_id():

    api_key="AIzaSyBgirMwGs0VnNxz2Zt7uIDRiphaTktbmEE"

    payload = {'place_id' : 'id'}

    r = requests.get('https://covidmapsapi.herokuapp.com', params=payload)

    return crawler.get_populartimes(api_key, r)


if __name__ == '__main__':
    app.run(debug=True)
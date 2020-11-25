import flask
import crawler
import requests

app = flask.Flask(__name__)


@app.route('/')
def get_id():

    place_id = str
    api_key="AIzaSyBrMyfwVh1UjrwUT5ygyptW3EMot5SzMOc"
    requests.headers.get('place_id') = str

    return crawler.get_populartimes(api_key, place_id)


if __name__ == '__main__':
    app.run(debug=True)
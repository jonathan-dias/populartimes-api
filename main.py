import flask
import crawler
import requests

app = flask.Flask(__name__)


@app.route('/')
def get_id():

    url = "https://covidmapsapi.herokuapp.com/"
    #data = {'place_id' : 'value'}
    api_key="AIzaSyBrMyfwVh1UjrwUT5ygyptW3EMot5SzMOc"
    #requests.post(url, data)
    payload = {'key1': 'value1'}

    requests.get(url, params=payload)
    
    return crawler.get_populartimes(api_key, payload)


if __name__ == '__main__':
    app.run(debug=True)
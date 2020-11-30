import flask
import crawler
import requests

app = flask.Flask(__name__)


@app.route('/')
def get_id():

    api_key="AIzaSyBrMyfwVh1UjrwUT5ygyptW3EMot5SzMOc"
    place_id = input("Qual é o PlaceID ?")

    url = 'https://covidmapsapi.herokuapp.com/?place_id={}'.format(place_id)
    
    response = requests.get(url)
    print(response)

    return crawler.get_populartimes(api_key, place_id)


if __name__ == '__main__':
    app.run(debug=True)
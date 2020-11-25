import flask
import crawler

app = flask.Flask(__name__)

@app.route('/')
def get_id():

    api_key="AIzaSyBrMyfwVh1UjrwUT5ygyptW3EMot5SzMOc"
    place_id="ChIJJWoTrD_5zpQR7MUpPiNrGVk"

    return crawler.get_populartimes(api_key, place_id)


if __name__ == '__main__':
    app.run(debug=True)
import flask
import requests
app = flask.Flask(__name__)

@app.route("/")
def OlaMundo():
        return "<p>Ola Mundo</p>"

@app.route("/consultaContinente")
def consultaContinente():
    import requests
    response2 = requests.get("https://www.omdbapi.com/?apikey=XXX&t=dune")
    return response2.json()


if __name__ == '__main__':
    app.run(debug=True)

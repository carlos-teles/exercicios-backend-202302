import flask
import requests
import 
app = flask.Flask(__name__)

@app.route("/")
def OlaMundo():
        return "<p>Ola Mundo</p>"

@app.route("/consultaContinentes")
def consultaContinentes():
    response2 = requests.get("http://127.0.0.1:8000/getContinents")
    return response2.json()


if __name__ == '__main__':
    app.run(debug=True)

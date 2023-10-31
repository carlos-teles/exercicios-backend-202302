import flask
import requests
app = flask.Flask(__name__)

@app.route("/")
def OlaMundo():
        return "<p>Ola Mundo</p>"

@app.route("/consultaContinentes")
def consultaContinentes():
    import requests
    response2 = requests.get("https://ideal-journey-7695rrvrpxhr4pg-8000.app.github.dev/getContinents")
    return response2.json()


if __name__ == '__main__':
    app.run(debug=True)

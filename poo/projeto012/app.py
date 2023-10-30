import flask
app = flask.Flask(__name__)

@app.route("/")
def OlaMundo():
        return "<p>Ola Mundo</p>"

if __name__ == '__main__':
    app.run(debug=True)

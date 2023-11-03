import flask
import requests
import json2table
import json
app = flask.Flask(__name__)


#@app.route("/")
#def OlaMundo():
#        return "<p>Ola Mundo</p>"

@app.route('/')
def home():
    return flask.render_template('index.html')

@app.route('/page2')
def page2():
    return flask.render_template('page2.html')



@app.route("/getContinents")
def consultaContinentes():
        response2 = requests.get("http://127.0.0.1:8000/getContinents")
        json_object = response2.json()
        print(json_object)
        for data_in in json_object["Continents"]:
                for data_inside in data_in:
                        if "name" == data_inside:
                                data_in["name"] = "<a href='/getRegion?continent_id={0}>{1}</a>".format(data_in["continent_id"],data_in["name"])
        build_direction = "LEFT_TO_RIGHT"
        table_attributes = {"style" : "width:100%", "border": "1px solid black"}
        html = json2table.convert(json_object, build_direction=build_direction, table_attributes=table_attributes)
        return flask.render_template('generico.html', html=html)
        #return html

@app.route("/getRegions")
def consultaRegioes():
        response2 = requests.get("http://127.0.0.1:8000/getRegions")
        json_object = response2.json()
        build_direction = "LEFT_TO_RIGHT"
        table_attributes = {"style" : "width:100%", "border": "1px solid black"}
        html = json2table.convert(json_object, build_direction=build_direction, table_attributes=table_attributes)
        #print(html)
        #return response2.json()
        return flask.render_template('generico.html', html=html)
        #return html

@app.route("/getRegion")
def getRegion():
        continent_id = flask.request.args.get('continent_id')
        name = flask.request.args.get('name')
        response2 = requests.get("http://127.0.0.1:8000/getRegion/"+continent_id)
        json_object = response2.json()
        build_direction = "LEFT_TO_RIGHT"
        table_attributes = {"style" : "width:100%", "border": "1px solid black"}
        html = json2table.convert(json_object, build_direction=build_direction, table_attributes=table_attributes)
        return flask.render_template('generico.html', html=html)



@app.route("/getCountries")
def consultaPaises():
        response2 = requests.get("http://127.0.0.1:8000/getCountries")
        json_object = response2.json()
        build_direction = "LEFT_TO_RIGHT"
        table_attributes = {"style" : "width:100%", "border": "1px solid black"}
        html = json2table.convert(json_object, build_direction=build_direction, table_attributes=table_attributes)
        #print(html)
        #return response2.json()
        return flask.render_template('generico.html', html=html)
        #return html

@app.route("/getLanguages")
def consultaLinguas():
        response2 = requests.get("http://127.0.0.1:8000/getLanguages")
        json_object = response2.json()
        build_direction = "LEFT_TO_RIGHT"
        table_attributes = {"style" : "width:100%", "border": "1px solid black"}
        html = json2table.convert(json_object, build_direction=build_direction, table_attributes=table_attributes)
        #print(html)
        #return response2.json()
        return flask.render_template('generico.html', html=html)
        #return html


if __name__ == '__main__':
    app.run(debug=True)

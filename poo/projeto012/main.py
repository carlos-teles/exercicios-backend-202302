import fastapi
import connection
app = fastapi.FastAPI()
@app.get("/")
def hello_world_root():
    return {"Olá": "Funciona"}

@app.get("/getContinents")
def getContinents():
    Continents_list = []
    mycursor = connection.mydb.cursor(dictionary=True)
    mycursor.execute("select * from continents")
    for data_continents in mycursor:
        Continents_list.append( data_continents )
    mycursor.close()
    return {"Continents": Continents_list}

@app.get("/getContinent/{continent_id}")
def getContinent(continent_id : int):
    Continents_list = []
    mycursor = connection.mydb.cursor(dictionary=True)
    mycursor.execute("select * from continents where continent_id = {0}".format(continent_id))
    for data_continents in mycursor:
        Continents_list.append( data_continents )
    mycursor.close()
    return {"Continent": Continents_list}

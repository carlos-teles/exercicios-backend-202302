import fastapi
import connection
import json
from pydantic import BaseModel, Field


app = fastapi.FastAPI()
@app.get("/")
def hello_world_root():
    return {"Olá": "Funciona"}

@app.get("/getContinents")
def getContinents():
    Continents_list = []
    mycursor = connection.mydb.cursor(dictionary=True)
    sql = "select * from continents"
    mycursor.execute(sql)
    for data_continents in mycursor:
        Continents_list.append( data_continents )
    mycursor.close()
    return {"Continents": Continents_list}

@app.get("/getContinent/{continent_id}")
def getContinent(continent_id : int):
    Continents_list = []
    mycursor = connection.mydb.cursor(dictionary=True)
    sql="select * from continents where continent_id = {0}".format(continent_id)
    mycursor.execute(sql)
    for data_continents in mycursor:
        Continents_list.append( data_continents )
    mycursor.close()
    return {"Continent": Continents_list}
################################################################
@app.post('/createContinent/{continent_name}')
def createContinent(continent_name: str, continent_description: str):
    if continent_name == "":
        return {'Error': 'Item vazio'}
    mycursor = connection.mydb.cursor(dictionary=True)
    sql=" INSERT INTO continents (name) values ('{0}')".format(continent_name)
    mycursor.execute(sql)
    mycursor.execute("COMMIT;")
    mycursor.close()
    return {"Continent: OK"+continent_description}
################################################################
class Continent(BaseModel):
   continent_name :str = Field(None, title="nome dos continentes", max_length=25)

@app.post('/createContinent2')
def createContinent2(info: Continent):
    #Continent_details = json.loads(Continent)
    if info.continent_name == "":
        return {'Error': 'Item vazio'}
    mycursor = connection.mydb.cursor(dictionary=True)
    sql=" INSERT INTO continents (name) values ('{0}')".format(info.continent_name)
    mycursor.execute(sql)
    mycursor.execute("COMMIT;")
    mycursor.close()
    return {
        "status" : "SUCCESS",
        "data" : info.continent_name
    }
################################################################

@app.delete("/DeleteContinent/{continent_id}")
def DeleteContinent(continent_id : int):
    Continents_list = []
    mycursor = connection.mydb.cursor(dictionary=True)
    sql="select * from continents where continent_id = {0}".format(continent_id)
    mycursor.execute(sql)
    for data_continents in mycursor:
        Continents_list.append( data_continents )
    mycursor.close()
    if len(Continents_list) == 0:
        return {'Message': 'Continent doesn´t exist'}
    else:
        mycursor_del = connection.mydb.cursor(dictionary=True)
        sql_del = "DELETE from continents where continent_id = {0}".format(continent_id)
        mycursor_del.execute(sql_del)
        mycursor_del.execute("COMMIT;")
        mycursor_del.close()
        return {'Message': 'Continent deleted successfully - '+str(continent_id)}

################################################################
@app.patch('/updateContinent/{continent_id}/{continent_name}')
def createContinent(continent_id : int, continent_name: str):
    Continents_list = []
    if continent_name == or "" continent_id == 0:
        return {'Error': 'Item vazio'}
    mycursor = connection.mydb.cursor(dictionary=True)
    sql="select * from continents where continent_id = {0}".format(continent_id)
    mycursor.execute(sql)
    mycursor.execute("COMMIT;")
    mycursor.close()
    return {"Continent: OK"+continent_description}

""" Continent - End"""
""" Regions - Start"""

@app.get("/getRegions")
def getRegions():
    Regions_list = []
    mycursor = connection.mydb.cursor(dictionary=True)
    sql = "select * from regions"
    mycursor.execute(sql)
    for data_regions in mycursor:
        Regions_list.append( data_regions )
    mycursor.close()
    return {"Regions": Regions_list}


@app.get("/getRegion/{continent_id}")
def getRegion(continent_id : int):
    Regions_list = []
    mycursor = connection.mydb.cursor(dictionary=True)
    sql="select * from regions where continent_id = {0}".format(continent_id)
    mycursor.execute(sql)
    for data_regions in mycursor:
        Regions_list.append( data_regions )
    mycursor.close()
    return {"Region": Regions_list}

""" Regions - End """

""" Languages - Start """
@app.get("/getLanguages")
def getLanguages():
    Languages_list = []
    mycursor = connection.mydb.cursor(dictionary=True)
    sql = "select * from languages"
    mycursor.execute(sql)
    for data_languages in mycursor:
        Languages_list.append( data_languages )
    mycursor.close()
    return {"Regions": Languages_list}
""" Languages - End """


""" country_languages - Start """
@app.get("/getCountryLanguages")
def getCountryLanguages():
    country_languages_list = []
    mycursor = connection.mydb.cursor(dictionary=True)
    sql = "select * from country_languages"
    mycursor.execute(sql)
    for data_country_languages in mycursor:
        country_languages_list.append( data_country_languages )
    mycursor.close()
    return {"CountryLanguages": country_languages_list}
""" country_languages - End """

""" country_stats - Start """
@app.get("/getCountryStats")
def getCountryStats():
    country_stats_list = []
    mycursor = connection.mydb.cursor(dictionary=True)
    sql = "select * from country_stats"
    mycursor.execute(sql)
    for data_country_stats in mycursor:
        country_stats_list.append( data_country_stats )
    mycursor.close()
    return {"CountryStats": country_stats_list}
""" country_stats - End """


""" countries - Start """
@app.get("/getCountries")
def getCountries():
    countries_list = []
    mycursor = connection.mydb.cursor(dictionary=True)
    sql = "select * from countries"
    mycursor.execute(sql)
    for data_countries in mycursor:
        countries_list.append( data_countries )
    mycursor.close()
    return {"Countries": countries_list}
""" countries - End """


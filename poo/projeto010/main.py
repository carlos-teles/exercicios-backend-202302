import fastapi

app = fastapi.FastAPI()

@app.get("/")
def indice():
    return{"mensagem" : "Ola Mundo!"}

@app.get("/mundo")
def indiceMundo():
    return{"mensagem" : "Ola Todo Mundo!"}

@app.get("/esporte")
def indiceEsporte():
    return{"mensagem" : "Ola Esportes."}
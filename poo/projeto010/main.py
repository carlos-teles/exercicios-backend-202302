import fastapi

app = fastapi.FastAPI()

@app.get("/")
def indice():
    return{"mensagem" : "Ola Mundo!"}

@app.get("/mundo")
def indiceMundo():
    return{"mensagem" : "Ola Todo Mundo!"}

@app.get("/esporte/{nome_esporte}")
def indiceEsporte( nome_esporte: str = fastapi.Path(...,  description="Preencha com o nome do esporte ")):
    return{"mensagem" : "Ola Esportes."}
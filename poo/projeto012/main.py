import fastapi
import connection
app = fastapi.FastAPI()
@app.get("/")
def hello_world_root():
    return {"Olá": "Funciona"}

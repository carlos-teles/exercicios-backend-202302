import fastapi
#Simula um JSON
menu = [ {   'id': 1,  'name': 'café',      'price': 2.5     },
         {   'id': 2,  'name': 'bolo',      'price': 10    },
         {   'id': 3,  'name': 'chá',       'price': 3.2    },
         {   'id': 4,  'name': 'croissant', 'price': 5.79 },
         {   'id': 5,  'name': 'joelho',    'price': 4.79    } ]

app = fastapi.FastAPI()
@app.get("/")
def hello_world_root():
    return {"Turma": "Backend"}

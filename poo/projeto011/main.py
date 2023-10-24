import fastapi
app = fastapi.FastAPI()

menu = [{   'id': 1,        'name': 'coffee',      'price': 2.5     },
        {   'id': 2,        'name': 'cake',        'price': 10    },
        {   'id': 3,        'name': 'tea',         'price': 3.2    },
        {   'id': 4,        'name': 'croissant',   'price': 5.79    }]
@app.get("/")
def indice():
    return{"mensagem" : "Ola Mundo!"}

@app.get('/get-item/{item_id}')
def get_item(item_id: int = fastapi.Path(...,description="Preencha com o ID do item que deseja consultar")):
    search = list(filter(lambda x: x["id"] == item_id, menu))
    if search == []:
        return {'Error': 'O item não existe'}
    return {'Item': search[0]}

@app.delete('/delete-item/{item_id}')
def delete_item(item_id: int):
    search = list(filter(lambda x: x["id"] == item_id, menu))
    if search == []:
        return {'Item': 'Does not exist'}
    for i in range(len(menu)):
        if menu[i]['id'] == item_id:
            del menu[i]
            break
    return {'Message': 'Item deleted successfully'}

""" GET ALL """
@app.get('/list-menu')
def list_menu():
    return {'Items': menu }
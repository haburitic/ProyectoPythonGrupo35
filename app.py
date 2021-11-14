from flask import Flask, json

import json
from bson.json_util import dumps

from flask import request

from pymongo import MongoClient

import ssl


app = Flask(__name__)

client = MongoClient('mongodb+srv://test:test@cluster0.oh46f.mongodb.net/DeportesDB', ssl_cert_reqs=ssl.CERT_NONE)
db=client.ContactDB


@app.route('/', methods=['GET'])
def  saludo():
    return "Hola mundo"

datos=[
    {
        'id':1,
        'titulo':"Hola"
    },
{
        'id':2,
        'titulo':"Hola 2"
    }
]

@app.route('/addcontacto', methods = ['POST'])
def addContacto():
    try:
        data= json.loads(request.data)
        id=data['id']
        titulo=['titulo']
        elemento ={
                'id':id,
                'titulo':titulo
        }

        datos.append(elemento)
        return dumps({'message':datos})
    except Exception as error:
        return dumps({'Error addContacto',error})



@app.route('/addcontactobd', methods = ['POST'])
def addContactobd():
    try:
        data= json.loads(request.data)
        id=data['id']
        titulo=['titulo']
        Empleado ={
                'id':id,
                'titulo':titulo
        }

        db.Contacts.insert_one(Empleado)
        return dumps({'response',"Sussess"})

    except Exception as error:
        return dumps({'Error addContacto',error})
if __name__ =='__main__':
    app.run(debug=True)
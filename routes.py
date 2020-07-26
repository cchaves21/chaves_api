from flask import Flask, request
from main import insertUsuario, geraResponse, buscaUsuario

app = Flask("Chaves")

@app.route("/consulta/usuario", methods=["GET"])
def consultaUsuario():
   usuario = buscaUsuario()
   return usuario

@app.route("/cadastra/usuario", methods=["POST"])
def cadastraUsuario():
    
    body = request.get_json()

    if("nome" not in body):
       return geraResponse(400, "O paramentro nome é obrigatório")
    
    if("email" not in body):
       return geraResponse(400, "O paramentro email é obrigatório")

    if("senha" not in body):
       return geraResponse(400, "O paramentro senha é obrigatório")

    usuario = insertUsuario(body["nome"], body["email"], body["senha"])

    return geraResponse(200, "usuario criado com sucesso", "user", usuario)


app.run()
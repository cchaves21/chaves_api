def insertUsuario(nome, email, senha):
 
    return {"id": 1, "nome": nome, "senha": "*****"}



def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if(nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo

    return response

def buscaUsuario():
    
    return {"id":1, "nome":"Usuario teste", "email":"usuario@email.com"}
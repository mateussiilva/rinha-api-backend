
from flask import Flask,url_for,request
from teste import vericar_pessoas_cadastradas, cadastrar_pessoas
import json

models = {
    "1":{
    "apelido" : "josé",
    "nome" : "José Roberto",
    "nascimento" : "2000-10-01",
    "stack" : ["C#", "Node", "Oracle"]
},
"2":{
    "apelido" : "ana",
    "nome" : "Ana Barbosa",
    "nascimento" : "1985-09-23",
    "stack" : None
}
}


app = Flask(__name__)

@app.route("/")
def index():
    return "Bem vindo a rinha de backend"




@app.route("/pessoas/",methods=["GET","POST"])
def pessoas():
    if request.method == "POST":
        data_json =  dict(map(
        lambda x:(x[0].lower().strip("\\"), x[1].strip("\\").lower()) ,request.args.items()
    ))
        return data_json
        # if cadastrar_pessoas(models, request.args):    
        #     return "PESSOA CADASTRADA COM SUCESSO"
        # else:
        #     return "PESSOA JÁ ESTÁ CADASTRADA"
    if request.method == "GET":
        return "Pessoas Cadastradas"



if __name__ == "__main__":
    # with app.test_request_context():
    #     print(url_for('index'))
    #     print(url_for('pessoas'))
    #     # print(url_for('pessoas', next='/'))
    #     # print(url_for('cadastrar_pessoas',values=nome))
    app.run(debug=True)
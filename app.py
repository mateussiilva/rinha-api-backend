
from flask import Flask,url_for,request


app = Flask(__name__)


@app.route("/pessoas",methods=["GET","POST"])
def pessoas():
    if request.method == "POST":
        return 
    if request.method == "GET":
        return "Pessoas Cadastradas"

@app.route("/contagem-pessoas")
def contagem_pessoas():
    return

if __name__ == "__main__":
    app.run(debug=True)
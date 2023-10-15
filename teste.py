
import json
# from pprint import pprint as print


def verificar_pessoa(dic,pessoa):
    for k,v in dic.items():
        if isinstance(v,dict):
            apelido = v.get("apelido")
            print(apelido)
            if pessoa == apelido:
                return False
            else:
                return True


def gravar_pessoa(file,dado):
    with open(file,"r",encoding="utf-8") as fp:
        dados = json.load(fp)
    return dados


if __name__ == "__main__":
    dados = gravar_pessoa("models.json","")
    print(verificar_pessoa(dados,"josé"))
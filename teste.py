


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

d = {
  "\"apelido\"": " \"tevez\",",
  "\"nascimento\"": " \"1985-09-23\",",
  "\"nome\"": " \"jose Barbosa\",",
  "\"stack\"": " None",
}

print(
    
)




def vericar_pessoas_cadastradas(base=models,valor="ana") -> bool:
    pessoas_cadastradas = [pessoas.get("nome") for pessoas in base.values()]
    return True if valor in pessoas_cadastradas else False

def cadastrar_pessoas(base,dados):
    nome = dados.get("nome")
    if vericar_pessoas_cadastradas(base,nome):
        base[str(len(base))] = dados
        return True
    return False
#!/usr/bin/python3

def qual_sua_idade (idade:int,completou_os_estudos:bool)->str :
    texto = "você é "
    if idade >= 18 :
       if completou_os_estudos == True :
            texto = texto + "maior de idade"
       texto = texto + " um vagabundo "
    if idade >= 16 :
       if completou_os_estudos == False :
            texto = texto + "menor de idade"
    if idade < 10 :
        texto = texto + "uma criança"
    return texto

pedro = qual_sua_idade(16,False)
print (f"pedro {pedro}")

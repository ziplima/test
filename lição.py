#!/usr/bin/python3

def oque_voce_pode_fazer (ficha_limpa:bool,idade:int)->str:
    texto = "voce pode:"
    if idade >= 21 :
        if ficha_limpa == True :
            texto = texto + " ser presidente , porta arma "
        texto = texto + " ,dirigir caminhão "   
    if idade >= 18 :   
        texto = texto + " ,dirigir carro "
    if idade >= 16 :
        texto = texto + " ,votar "    
    if idade < 18 :
        texto = texto + " ,pegar menor de 14 "  
    return texto   

Matheus = oque_voce_pode_fazer(True,15)
Mouto = oque_voce_pode_fazer (True,24)
Gustavo = oque_voce_pode_fazer (False,25)
print (f"Gustavo {Gustavo}")
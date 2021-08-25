
#aviao
voa = True
tem_asas = True
rodas  = 8
anda_na_agua = False
e_rapido = True

if voa == True:
   if tem_asas == True:
      if e_rapido == True:
          print("e um jato")
      else:
          print("e um aviao")
   else:
       print("e um helicopero")


if voa == False:
    if rodas == 2:
        print("e uma moto")
    if rodas == 4:
        print("e um carro")
    if anda_na_agua == True:
       if e_rapido == True:
           print("e um barco")
       if e_rapido == False:
           print("e jesus")


#!/usr/bin/python3
 



def realizadora(num1:float,num2:float,opcao:str)->float:
    '''vai realizar a conta'''
    if opcao == '+':
        resultado = num1 + num2
    if opcao == '-':
        resultado = num1 - num2
    if opcao == '*' or opcao == 'x':
        resultado = num1 * num2
    if opcao == '/':
        resultado = num1 / num2        
    return resultado

a = 4
b = 5
c = '-'


test = realizadora(5,3,+)
print (test)



    

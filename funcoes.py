#!/usr/bin/python3

def soma(num1,num2):
    return num1 + num2

def ao_cubo(num1):
    return num1 * num1 * num1

def retorne_nota(nota:int)->str:
    if nota <= 4:
        return "reprovado"
    if nota <= 6:
        return "recuperação"    
    return "aprovado"

r = retorne_nota(8)
print (r)

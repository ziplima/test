#!/usr/bin/python3
ano_atual = 2021

ano_da_pessoa = int(input("que ano você naceu"))
ja_fez_aniversario = input("voce já vez aniversario (s/n)")

resposta = ano_atual - ano_da_pessoa
 
if ja_fez_aniversario == "n":
 resposta = resposta - 1


print(f"você tem {resposta} de idade")


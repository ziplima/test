


def retorna_resultado(num1:float,num2:float,opcao:str)-> float:
    opcao = opcao.lower()
    if opcao == '+':
       return num1 + num2

    if opcao == '-':
       return num1 - num2   
   
    if opcao == 'x' or '*':
       return num1 * num2

    if opcao == '/':
       return num1 / num2


def captura_numero(numero:str)->float:
    return float(input(f"digite o {numero} "))



num1:float= captura_numero("numero 1")
num2:float = captura_numero("numero 2")
opcao:str = input("digite a operacao ")
resultado:float = retorna_resultado(num1,num2,opcao)
print(f'valor de resultado: {resultado}')


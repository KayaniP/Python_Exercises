
# Crie a função cria_conta, que recebe como argumento numero, titular, saldo e limite.

#2 - Dentro dela, crie o dicionário conta com os argumentos da função e retorne-o no final da função.

#3 - Crie a função deposita, que recebe como argumento a conta e o valor e adiciona o valor ao saldo da conta.

#4 - Crie a função saca, que recebe como argumento a conta e o valor e subtrai o valor do saldo da conta.

#5 - Crie a função extrato, que recebe como argumento a conta e imprime o seu saldo.


def criar_conta (numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def depositar(conta, valor):
    conta["saldo"] += valor

def sacar(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo {}".format(conta["saldo"]))

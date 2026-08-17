# Lista: É mutável (pode mudar os valores), é ordenado, é indexado (de 0 a n)
lista = {10,20,30} 



# Tupla: É imutável (não pode alterar o valor), é ordenada, é indexada (de 0 até n)

# tupla[1] = 29 # isso vai dar erro, vc n podedar um novo valor / "tuple' object does not support item assignment"

tuplaA = (10,20,30)
tuplaB = (30,40,50)
tuplaA = tuplaB # estrutura sobreposta a outra tupla
print(tuplaA)

# transformar tupla em lista:
teste = lista(tuplaA)
print(type(teste))



# Dicionário: é mutável, é ordenado a partir da versão3.7.x, acesso pela chave
dicionario = {"num1": 10, "num2": 20, "num3": 30} #dicionário

matriz = [[10,20,30]]

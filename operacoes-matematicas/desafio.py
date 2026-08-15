# variável e estrutura de decisão

print("--------------------------------VARÍAVEL E ESTRUTURA DE DECISÃO--------------------------------")
print("")
idade = 18

if idade < 18:
    print("Pedir permissão pro responsável")
elif idade >= 18:
    print("Vocẽ é maior de idade! #partiuFesta")

# variável e estrutura de repetição (while)

print("")
print("--------------------------------VARÍAVEL E ESTRUTURA DE REPETIÇÃO (WHILE)--------------------------------")
print("")
contador = 0

while contador < 20:
    contador+= 1
    print("Cadeira:", contador, "ocupada")

if contador == 20:
    print("Alerta! Sala de cinema lotada. Sem cadeiras disponíveis!")

# variável + funções
    print("")
    print("--------------------------------VARÍAVEL E FUNÇÕES--------------------------------")
    print("")
    print("Vamos fazer alguns cálculos com operações matemáticas!")

    def somar(a,b):
        return a+b 
    
    resultado_soma = somar(10,10)
    print("Soma de 10+10:", resultado_soma)

    def subtracao(c,d):
        return c-d
    
    resultado_subtracao = subtracao(20, 10)
    print("Subtração de 20-10: ", resultado_subtracao)

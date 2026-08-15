print('\n')
print("Exercício 2")
print('\n')

import math #importando biblioteca de matemática

c=4
d=5

c_elevado_ao_quadrado = math.pow(c,2)
c_elevado_ao_cubo = math.pow(c,3)
c_elevado_a_quarta = math.pow(c,4)
c_elevado_a_d = math.pow(c,d)

print("c elevado ao quadrado =", c_elevado_ao_quadrado)
print("c elevado ao cubo =",c_elevado_ao_cubo)
print("c elevado a quarta =", c_elevado_a_quarta)
print("c elevado a d =", c_elevado_a_d)


print('\n')
print("Desafio")

num1 = int(input(f"Número 1:"))
num2 = int(input(f"Número 2:"))

print(f"{num1} elevado ao quadrado = {math.pow(num1,2)}")
print(f"{num1} elevado ao cubo = {math.pow(num1,3)}")
print(f"{num1} elevado a quarta = {math.pow(num1,4)}")
print(f"{num1} elevado a {num2} = {math.pow(num1,num2)}")


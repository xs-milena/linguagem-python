# print('\n')
# print("Exercício 8")

# print("1. \n")

# a = 2
# b = 3
# c = 4
# ex1 = a**b
# print(f"Resultado de {a}**{b}: {ex1}")

# print("2. \n")

# ex2 = a**0
# print(f"Resultado de {a}**{0}: {ex2}")

# print(f"3. \n")

# ex3 = a**1
# print(f"Resultado de {a}**{1}: {ex3}")

# print(f"4. \n")

# ex4 = a **(-b) = 1/a**b

# print(f"Resultado de {a}**(-{b}) = 1/{a}**{b}: {ex4}")

# print(f"5. \n")

# ex5 = (a**b)*(a**c) = a**(b+c)

# print(f"Resultado de ({a}**{b})*({a}**{c}) = {a}**({b+c}): {ex5}")

# print(f"6. \n")

# ex6 = (a**b)/(a**c) = a**(b-c)
# print(f"Resultado de ({a}**{b})/({a}**{c}) = {a}**({b}-{c}): {ex6}")

# print(f"7. \n")

# ex7 = ((a**b)**c) = a**b
# print(f"Resultado de (({a}**{b})**{c}) = {a}**{b}: {ex7}")

# print(f"8. \n")

# ex8 = ((a/b)**c) = ((a**c)/(b**c))
# print(f"Resultado de (({a}/{b}){c}) = (({a}**{c})/({b}**{c})): {ex8}")

print('\n')
print(f"Exercício 8\n")

print("1.")

a = 2
b = 3
c = 4
ex1 = a**b
print(f"Resultado de {a}**{b}: {ex1} \n")

print("2.")

ex2 = a**0
print(f"Resultado de {a}**{0}: {ex2}\n")

print(f"3.")

ex3 = a**1
print(f"Resultado de {a}**{1}: {ex3}\n")

print(f"4.")

ex4 = a **(-b)
prova_real_ex4 = (1/(a**b))

print(f"Resultado de {a}**(-{b}): {ex4}")
print(f"Prova real = 1/({a}**{b}): {prova_real_ex4}\n")

print(f"5.")

ex5 = (a**b)*(a**c) 
prova_real_ex5 = (a**(b+c))

print(f"Resultado de ({a}**{b})*({a}**{c}) = {a}**({b+c}): {ex5}")
print(f"Prova real = {a}**({b}+{c}): {prova_real_ex5}\n")

print(f"6.")

ex6 = (a**b)/(a**c) 
prova_real_ex6 = (a**(b-c))

print(f"Resultado de ({a}**{b})/({a}**{c}) = {a}**({b}-{c}): {ex6}")
print(f"Prova real = ({a}**({b-c})): {prova_real_ex6}\n")

print(f"7.")

ex7 = (a**b)**c
prova_real_ex7 = (a**(b*c))
print(f"Resultado de ({a}**{b})**{c} = {a}**{b}*{c}: {ex7}")
print(f"Prova real = {a}**({b}*{c}): {prova_real_ex7}\n")

print(f"8.")

ex8 = ((a/b)**c) 
prova_real_ex8 = ((a**c)/(b**c))
print(f"Resultado de (({a}/{b}){c}) = (({a}**{c})/({b}**{c})): {ex8}")
print(f"Prova real = {a}**{c} / {b}**{c}: {prova_real_ex8}\n")
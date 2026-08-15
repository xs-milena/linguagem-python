print('\n')
print("Exercício 4")
print('\n')

import math
w = 3345.61

piso_salarial = math.floor(w)
teto_salarial = math.ceil(w)

print(f"Teto salarial de {w} = {teto_salarial}")
print(f"Piso salarial de {w} = {piso_salarial}")
print(f"Arredondamento de {w} = {round(w)}")

# floor – retorna o maior valor inteiro menor que w
# ceil – retorna o menor valor inteiro maior que w
# round – retorna o valor inteiro mais próximo de a
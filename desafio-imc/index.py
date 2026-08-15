print('\n')
print("Calculadora IMC em Python")
print('\n')


def calcular_imc():
    peso = float(input("Digite seu peso (kg): "));
    altura = float(input("Digite sua altura (m): "));
    print('\n')
    imc = peso/(altura**2);

    if peso <= 0 or altura <=0:
        print("Peso incorreto ou altura incorreto. Coloque valores positivos!")

    else:
        if imc <= 15.87:
            mensagem = print(f"Seu IMC é: {imc:.2f} - Baixo peso muito grave")
        elif imc <= 16.78:
            mensagem = print(f"Seu IMC é: {imc:.2f} - Baixo peso grave")
        elif imc <= 18.14:
            mensagem = print(f"Seu IMC é: {imc:.2f} - Baixo peso")
        elif imc <= 24.94:
            mensagem = print(f"Seu IMC é: {imc:.2f} - Peso ideal")
        elif imc <=25.43:
            mensagem = print(f"Seu IMC é: {imc:.2f} - Sobrepeso")
        elif imc <=30.47:
            mensagem = print(f"Seu IMC é: {imc:.2f} - Obesidade grau I")
        elif imc <= 35.51:
            mensagem = print(f"Seu IMC é: {imc:.2f} - Obesidade grau II")
        else:
            mensagem = print(f"Seu IMC é: {imc:.2f} - Obesidade mórbida") 

calcular_imc();

print('\n')

opcao = input("Deseja calcular o IMC de outra pessoa? (s/n): ")

sim = 's'
nao = 'n'
print('\n')

while opcao == sim:
    calcular_imc();
    opcao = input("\nDeseja calcular o IMC de outra pessoa? (s/n): ")

while opcao == nao:
    print("\nEncerrando a calculadora...")
    break;
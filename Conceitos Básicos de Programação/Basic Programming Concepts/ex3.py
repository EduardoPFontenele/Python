"Calculadora de IMC"
"Escreva um programa que solicite o peso e a altura do usuario e calcule o Indice de Massa Corporal (IMC)"

peso = float(input("Digite seu peso(kg): "))
altura = float(input("Digite sua altura(m): "))
IMC = peso/(altura**2)

print(f"-"*60)
print(f"Dado o peso {peso}kg e a altura {altura}m, o Indíce de Massa Corporal é {IMC:.2f}")
print(f"-"*60)
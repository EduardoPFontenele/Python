"Calculo do Valor das Parcelas"
"Escreva um programa que solicite o valor a vista de um produto e o numero de parcelas, e calcule o valor das parcelas que ira pagar"

preco = float(input("Informe o preço do produto:R$"))
parcelas = int(input("Deseja parcelar em quantas vezes?"))
resultado = preco/parcelas

print("-"*80)
print(f"O produto custa R${preco}.Ao ser parcelado em {parcelas} vezes,você deve pagar R${resultado:.2f} ao mês!")
print("-"*80)

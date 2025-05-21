"Calculo de Desconto"
"Escreva um programa que solicite o preco de um produto e a porcentagem de desconto, calcule o preco com desconto e exiba o resultado"
preco = float(input("Informe o preço do produto:R$"))
desconto = int(input("Informe a porcentagem de desconto aplicada:"))
resultado = preco - (preco * (desconto/100))

print("-"*70)
print(f"O produto custa R${preco}. Com a aplicação do desconto, seu valor é R${resultado:.2f}")
print("-"*70)
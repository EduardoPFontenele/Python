"Conversao de Idade para Dias"
"Escreva um programa que solicite a idade do usuario em anos e a converta para dias, considerando anos bissextos"
anos = int(input("Informe a sua idade:"))
dias = anos * 365.4

print(f"-"*60)
print(f"Dada a idade {anos} anos,em dias,são aproximadamente {dias:.2f} dias!")
print(f"-"*60)
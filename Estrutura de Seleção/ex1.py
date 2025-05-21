#Entrada
gasto = float(input("Informe seu gasto: R$ ")) #Usuario irá informar seu gasto

if gasto < 0: #Verificação de erros caso o valor informado seja menor que 0
    print("Insira valores válidos!")

elif gasto >= 200: #Se o gasto for maior ou igual a 200
    parcelas = gasto / 3# Dividir o gasto por 3

    print(f"O valor das parcelas são (3x): R${parcelas:.2f}")#Printar o numero de parcelas divididas por 3

else: #Se o gasto for menor que 200
    parcelas = gasto / 2 #Dividir o gasto em duas parcelas

    print(f"Dado o preço, será possível apenas dividir em 2x de {parcelas:.2f}")#Printar o numero de parcelas dividas por 2


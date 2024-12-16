"Neste problema, deve-se ler o código de uma peça 1, o número de peças 1," 
"o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2" 
"e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago."

def calculo_simples():

    #Usuario informará as informações respectivas à peça 1
    peca1 = int(input("Informe o codigo da peça1:")) 
    quantidade_peca1 = int(input("Informe a quantidade de peças 1 compradas:"))
    valor_peca1 = float(input("Quanto custa essa peça1:"))

    #Usuario informará as informações respectivas à peça 2
    peca2 = int(input("Informe o codigo da peça2:"))
    quantidade_peca2 = int(input("Informe a quantidade de peças 2 compradas:"))
    valor_peca2 = float(input("Quanto custa essa peça 2:"))


    total = (quantidade_peca1 * valor_peca1) + (quantidade_peca2 * valor_peca2) #Fórmula para calcular o total das peças


    print(f"VALOR A PAGAR: R$ {total:.2f}") #Mostra o total

if __name__ == "__calculo_simples__":
    calculo_simples()


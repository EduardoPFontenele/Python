def idade_para_votacao():

    for i in range(10): #Laço para usuario informar 10 idades
        idade = int(input("Informe sua idade:"))
        
        #Condicionais para verificação de idade
        if idade >= 18: 
            print(f"Você pode votar!")

        elif idade < 0:
            print(f"Valor inválido!")

        else:
            print(f"Você não pode votar!")

if __name__ == "__idade_para_votacao__":
    idade_para_votacao()

def main():
    idade_para_votacao()
if __name__ == "__main__":
    main()
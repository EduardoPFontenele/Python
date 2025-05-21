def estoque():

    produto = 0
    estoque = 15

    while produto < estoque:
        quantidade_produtos = int(input("Informe a quantidade de produtos:"))

        if quantidade_produtos < 0: 
            print(f"Valor invalido!")

        elif quantidade_produtos <= 5:
            print(f"Produto em falta! Precisa repor.")

        else:
            print(f"Estoque suficiente!")
        
        produto += 1
if __name__ == "__estoque__":
    estoque()

def main():
    estoque()
if __name__ == "__main__":
    main()


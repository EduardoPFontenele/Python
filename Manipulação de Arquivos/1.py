def cadastro_produtos(lista):
    
    #Criando uma lista vazia
    lista = [] 

    while True:

        #Coletando informações do usuario (nome de um produto)
        produto = str(input(f"\nDigite o nome do produto (ou 'sair' para encerrar) : "))

        #Finalizar o programa caso o usuario digite 'sair'
        if produto.lower() == 'sair':
            print(f"\nVendas Registradas com Sucesso!")
            break

        else:

            #Coletando informações do usuario (valor do produto informado)
            valor = float(input(f"Digite o valor da venda: "))

            #Verificando se o valor do preço informado é valido (preço maior que 0)
            if valor >= 0:
                lista.append(f'Produto: {produto}, Valor: R${valor:.2f}') #Armazenando as informações dos produtos dentro da lista
            
            else:
                print(f"Preço inválido!")
    
    #Abrindo o arquivo 'vendas.txt'
    with open ('vendas.txt','a') as arquivo:
        #Percorrendo os elementos da lista
        for produto in lista:
            #Escrevendo os elementos da lista dentro do arquivo
            arquivo.write(f"{produto}\n")

def main():

    PRODUTOS = []
    cadastro_produtos(PRODUTOS)

if __name__ == "__main__":
    main()
    



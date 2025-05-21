def contar_palavras(frase,dicionario):

    LISTA = []
    lista = frase.split()

    for itens in lista:
        LISTA.append(itens)

    for palavras in LISTA:
        if palavras in dicionario:
            dicionario[palavras] += 1

        else:
            dicionario[palavras] = 1
    
    print(f"{dicionario}")

def main():

    frase_dicionario = {}
    frase = str(input(f"Digite uma frase para verificar a frequencia de suas palavras: "))

    contar_palavras(frase,frase_dicionario)

if __name__ == "__main__":
    main()
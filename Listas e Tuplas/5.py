def mostrar_temperaturas(lista):
    print(f"\n<< TEMPERATURAS CAPTADAS PELO SENSOR >>\n")

    #Laço para mostrar todos os elementos da lista 'temperaturas'
    for i in range(len(lista)):
        print(f"=> {lista[i]} °C")

def temperaturas_manha(lista): 

    TEMPERATURAS_MANHA = []

    #'Fatiando' a lista para mostrar os dados da lista (temperaturas captadas durante a manhã)
    manha = lista[0:12:1]

    TEMPERATURAS_MANHA.append(manha)
    print(f"\n<= TEMPERATURAS DA MANHÃ =>\n")

    #Print 'formatado' dos itens da lista
    for temperaturas in TEMPERATURAS_MANHA:
        for temperaturas in manha:
            print(f"{temperaturas} °C",end=' | ')

    print(f"\n\n(Das 00:00 - 11:00)")

def temperaturas_tarde(lista):

    TEMPERATURAS_TARDE = []
    #'Fatiando' a lista para mostrar os dados da lista (temperaturas captadas durante a tarde)
    tarde = lista[12:18:1]

    TEMPERATURAS_TARDE.append(tarde)
    print(f"\n<= TEMPERATURAS DA TARDE =>\n")

    #Print 'formatado' dos itens da lista
    for temperaturas in TEMPERATURAS_TARDE:
        for temperaturas in tarde:
            print(f"{temperaturas}°C",end=' | ')
    
    print(f"\n\n(Das 12:00 - 17:00)")
    
def temperaturas_noite(lista):

    TEMPERATURAS_NOITE = []
    #'Fatiando' a lista para mostrar os dados da lista (temperaturas captadas durante a noite)
    noite = lista[18:24:1]

    TEMPERATURAS_NOITE.append(noite)
    print(f"\n<= TEMPERATURAS DA NOITE =>\n")

    #Print 'formatado' dos itens da lista
    for temperaturas in TEMPERATURAS_NOITE:
        for temperaturas in noite:
            print(f"{temperaturas}°C",end=' | ')
    
    print(f"\n\n(Das 18:00 - 23:00)")

def media_temperaturas(lista):

    print(f"\n<< MEDIA DAS TEMPERATURAS >>\n")
    print(f"{sum(lista)/(len(lista)):.1f}°C")

def main():
    temperaturas = [22, 23, 21, 19, 18, 17, 16, 15, 14, 14, 15, 16,
                    18, 20, 22, 23, 25, 26, 27, 28, 29, 28, 26, 24]
    
    while True:
        #Menu com varias opções para o usuario selecionar a operação que deseja realizar
        print(f"\n<< RELATORIO DE TEMPERATURAS >>\n")
        print(f"1. Consultar Temperaturas Captadas no Dia.")
        print(f"2. Consultar Temperaturas Captadas no Turno da Manhã.")
        print(f"3. Consultar Temperaturas Captadas no Turno da Tarde.")
        print(f"4. Consultar Temperaturas Captadas no Turno da Noite")
        print(f"5. Mostrar Temperatura Media.")
        print(f"6. Encerrar Programa.")

        opcao = int(input(f"\nInforme a operação que deseja realizar: "))

        if opcao == 1:
            mostrar_temperaturas(temperaturas)
        
        elif opcao == 2:
            temperaturas_manha(temperaturas)
        
        elif opcao == 3:
            temperaturas_tarde(temperaturas)
        
        elif opcao == 4:
            temperaturas_noite(temperaturas)
        
        elif opcao == 5:
            media_temperaturas(temperaturas)
        
        elif opcao == 6:
            print(f"Finalizando . . .")
            break

        else:
            print(f"Opção inválida!")

if __name__ == "__main__":
    main()
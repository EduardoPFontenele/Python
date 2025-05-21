def cadastrar_compromissos(lista):

    #Coletando dados do usuario (mes,dia,ano e descrição)
    dia = int(input(f"Informe o dia do compromisso: "))
    mes = int(input(f"Informe o mes do compromisso: "))
    ano = int(input(f"Informe o ano do compromisso: "))
    descricao = str(input(f"Descrição do evento: "))

    #Armazenando os dados do usuario em uma tupla
    compromisso = (dia,mes,ano,descricao)

    #Armazenando a tupla em uma lista
    lista.append(compromisso)

def listar_compromisso(lista):

    #Coletando dados do usuario (mes de um compromisso)
    mes_compromisso = int(input(f"Informe um mês para verificar a quantidade de compromissos: "))

    print(f"<= COMPROMISSO DO MÊS {mes_compromisso} =>")

    #Verificando se o 'compromisso' está na lista
    for compromisso in lista:
        #Verificando se  a informação dada ao usuario é a mesma que se encontra no indice 1 da tupla
        if compromisso[1] == mes_compromisso:
            print(f"\n=> {compromisso[0]} / {compromisso[1]} / {compromisso[2]}")
            print(f"DESCRIÇÃO = {compromisso[3]}\n")
        
        else:
            print(f"\nCompromisso não cadastrado e/ou Inexistente.")
def main():

    AGENDA = []
    
    #Menu com varias opções para o usuario selecionar a operação que deseja realizar
    while True:
        print(f"\n<< AGENDA >>")
        print(f"\n1. Cadastrar Compromisso.")
        print(f"2. Listar Compromisso.")
        print(f"3. Encerrar Programa.")

        opcao = int(input(f"Informe a operação que deseja realizar: "))

        if opcao == 1:
            print(f"\n<< CADASTRAR COMPROMISSO >>\n")
            cadastrar_compromissos(AGENDA)
            print(f"-" * 35)
            print(f"Compromisso cadastrado com sucesso!")
            print(f"-" * 35)

        elif opcao == 2:
            print(f"\n<< VERIFICAR COMPROMISSOS >>\n")
            listar_compromisso(AGENDA)
        
        elif opcao == 3:
            print(f"Finalizando . . .")
            break

if __name__ == "__main__":
    main()

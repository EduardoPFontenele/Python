def votar(dicionario):

    print(f"\n<===== CANDIDATOS =====>\n")
    print(f"(1) CandidatoA")
    print(f"(2) CandidatoB")
    print(f"(3) CandidatoC")

    opcao = int(input(f"\nDigite o numero do cadidato ao qual deseja votar: "))

    if opcao == 1:
        dicionario['CandidatoA'] += 1
        print(f"\nVoto adicionado à urna!")
    
    elif opcao == 2:
        dicionario['CandidatoB'] += 1
        print(f"\nVoto adicionado à urna!")
    
    elif opcao == 3:
        dicionario['CandidatoC'] += 1
        print(f"\nVoto adicionado à urna!")
    
    else:
        print(f"\nNumero de candidato inválido!")

def remover_voto(dicionario):
    print(f"\n<===== CANDIDATOS =====>\n")
    print(f"(1) CandidatoA")
    print(f"(2) CandidatoB")
    print(f"(3) CandidatoC")

    opcao = int(input(f"\nDigite o numero do cadidato ao qual deseja remover voto: "))

    if opcao == 1:
        if dicionario['CandidatoA'] <= 0:
            dicionario['CandidatoA'] = 0
        else:
            dicionario['CandidatoA'] -= 1

        print(f"\nVoto removido!")
    
    elif opcao == 2:
        if dicionario['CandidatoB'] <= 0:
            dicionario['CandidatoB'] = 0
        else:
            dicionario['CandidatoB'] -= 1
            
        print(f"\nVoto removido!")
    
    elif opcao == 3:

        if dicionario['CandidatoC'] <= 0:
            dicionario['CandidatoC'] = 0
        else:
            dicionario['CandidatoC'] -= 1
            
        print(f"\nVoto removido!")
    
    else:
        print(f"\nNumero de candidato inválido!")

def vencedor(dicionario):

    ganhador = max(dicionario,key=dicionario.get)
    mais_votos = dicionario[ganhador]

    print(f"O vencedor é {ganhador} com {mais_votos} votos.")

def main():

    candidatos = {
        'CandidatoA': 0,
        'CandidatoB' : 0,
        'CandidatoC' : 0
                  }
    
    while True:
        print(f"\n<===== URNA ELETRONICA =====>\n")
        print(f"1. Votar.")
        print(f"2. Remover voto.")
        print(f"3. Verificar o vencedor.")
        print(f"4. Encerrar programa.")

        opcao = int(input(f"\nQual a operação que deseja realizar: "))
        
        if opcao == 1:
            votar(candidatos)

        elif opcao == 2:
            remover_voto(candidatos)
        
        elif opcao == 3:
            vencedor(candidatos)
        
        elif opcao == 4:
            print(f"Finalizando . . .")
            break

if __name__ == "__main__":
    main()
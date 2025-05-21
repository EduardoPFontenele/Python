"""
Defina uma funcao chamada classificacao nota que recebe uma nota (0 a 100) e retorna a
classificacao (A, B, C, D, ou F) de acordo com a tabela:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: abaixo de 60
"""

def classificacao_nota(numero):

    #Verificação da entrada do usuario
    if numero < 0 or numero > 100:
        return 'Nota Invalida'

    else:
        
    #Logica para a resolucao do exercicio
        if numero >= 90 and numero <= 100:
            return 'A'
        
        elif numero >= 80 and numero <= 89:
            return 'B'
        
        elif numero >= 70 and numero <= 79:
            return 'C'
        
        elif numero >= 60 and numero <= 69:
            return 'D'
        else:
            return 'F'

def main():

    #Coleta de informações do usuario
    nota = int(input(f"-> Informe uma nota de 0 a 100: "))
    print(f"{classificacao_nota(nota)}")

if __name__ == "__main__":
    main()

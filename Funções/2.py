"""
Defina uma funcao chamada numero perfeito que recebe um numero inteiro e verifica se ele
eh um numero perfeito. Um numero perfeito eh um numero que eh igual `a soma de seus divisores
proprios (excluindo ele mesmo).
"""

def numero_perfeito(numero):

    #Verificacão da entrada do usuario
    if numero <=  0:
        return 'Numeros menores ou iguais à 0 não são perfeitos'
    
    else:
    
    #Logica para a resolução do exercicio
        divisores = 0

        for i in range(1, numero):
            if numero % i == 0: 
                divisores += i
            
        if numero == divisores:
            return "É um numero perfeito!"
        else:
            return "Não é um numero perfeito!"
    

def main():

    #Coleta de informações do usuario
    numero = int(input(f"-> Informe um numero: "))

    print(f"{numero_perfeito(numero)}")

if __name__ == "__main__":
    main() 
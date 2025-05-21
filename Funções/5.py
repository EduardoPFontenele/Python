"""
Defina uma funcao chamada conversao tempo que recebe uma quantidade de segundos e a
converte para o formato horas, minutos e segundos
"""
def conversao_tempo(quantidade_segundos):
    
    if quantidade_segundos < 0:
        return 'Valor inválido!'
    
    else:
    #Logica para resolucao do problema
        horas = quantidade_segundos // 3600
        minutos = (quantidade_segundos % 3600) // 60
        segundos = quantidade_segundos % 60

        return f"{horas:02}:{minutos:02}:{segundos:02}"

def main():
    
    #Coletando informacoes do usuario
    quantidade_segundos = int(input(f"-> Informe a quantidade de segundos para realizar as conversões: "))

    print (f"{conversao_tempo(quantidade_segundos)}")

if __name__ == "__main__":
    main()
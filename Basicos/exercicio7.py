"Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas," 
"o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número" 
"e o salário do funcionário, com duas casas decimais."

def salario():

    numero_funcionario = int(input("Informe seu ID: ")) #Usuario irá informar seu numero referente ao seu ID
    horas = int(input("Informe a quantidade de horas trabalhadas: "))  #Usuario informará horas trabalhadas
    valor_por_hora = float(input("Informe quanto você recebe por hora: U$")) #Usuario informará o quanto recebe por hora

    
    salario = horas * valor_por_hora #Formula para calcular salario

    
    print(f"NUMBER = {numero_funcionario}") #Mostra o ID do funcionario
    print(f"SALARY: U${salario:.2f}") #Mostra o salario
 
if __name__ == "__salario__":
    salario()

def main():
    salario()
if __name__ == "__main__":
    main()

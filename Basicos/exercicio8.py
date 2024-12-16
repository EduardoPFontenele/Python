"Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total" 
"de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% "
"de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês," 
"com duas casas decimais."

def salario_com_bonus():

    nome = input("Digite seu nome:") #Usuario irá informar seu nome
    salario_fixo = float(input("Informe seu salario:")) #Usuario informar seu salario
    vendas = float(input("Informe o lucro das vendas realizadas: R$")) #Usuario irá informar o quanto lucrou em vendas


    TOTAL = salario_fixo + (vendas * (15/100)) #Formula para calcular o bonus de seu salario

    print(f"TOTAL = R$ {TOTAL:.2f}") #Mostrar o total obtido

if __name__ == "__salario_com_bonus__":
    salario_com_bonus()

def main():
    salario_com_bonus()
if __name__ == "__main__":
    main()
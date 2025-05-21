#Entrada
idade = int(input("Informe a sua idade:"))#Usuario irá informar a idade
sexo = input("Informe seu sexo:")#Usuario irá informar o sexo

if idade < 0:#Tratamento de erros caso a idade seja menor que 0
    print(f"Insira uma idade válida!")

if sexo == 'mulher': #Se o sexo for definido como mulher
    if idade >= 62: #e se a idade for maior ou igual a 62
        print(f"Com {idade} anos é possível se aposentar.")#printar que é possível se aposentar

    else:#se não
        print(f"Ainda não é possível se aposentar!") #printar que não é possivel se aposentar

elif sexo == "homem": #Se o sexo definido for homem
    if idade >= 65:#e se a idade for maior ou igual a 65
        print(f"Com {idade} anos é possível se aposentar.")#Mostrar a mensagem que é possivel se aposentar,caso a condição seja verdadeira

    else:#Se não
        print(f"Ainda não é possível se aposentar!")#Caso a condição não se cumpra, printará que não será possivel se aposentar

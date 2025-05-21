LadoA = float(input("Informe o tamanho do segmento A:")) #Usuario irá informar o valor referente ao ladoA
LadoB = float(input("Informe o tamanho do segmento B:")) #Usuario irá informar o valor referente ao ladoB
LadoC = float(input("Informe o tamanho do segmento C:"))  #Usuario irá informar o valor referente ao ladoC

#Verificação de existencia de um triangulo escaleno (todos os lados são diferentes)
if (LadoA != LadoB) and (LadoB != LadoC) and (LadoC != LadoA):
    print(f"É um triangulo escaleno!")#Mostrar na tela que, depois que a condição for cumprida, trata-se de um triangulo escaleno
else:  
    print(f"Não é um triangulo escaleno!")#Mostrar na tela que não é possível formar um triangulo caso a condição não se cumpra
LadoA = float(input("Informe o tamanho do segmento A:"))#Usuario iŕa informar o valor referente ao ladoA
LadoB = float(input("Informe o tamanho do segmento B:"))#Usuario iŕa informar o valor referente ao ladoB
LadoC = float(input("Informe o tamanho do segmento C:"))#Usuario iŕa informar o valor referente ao ladoC

#verificação de condição para existencia de um triangulo
if (LadoA < LadoB + LadoC) and (LadoB < LadoA + LadoC) and (LadoC < LadoB + LadoA):
    print(f"É possível formar um triangulo!")#mostrar na tela que é possível formar um triangulo

else:#caso a condição seja "falsa"
    print(f"Não é possivel formar um triangulo!")#mostrar na tela que não será possível formar um triangulo
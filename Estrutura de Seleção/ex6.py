distancia = float(input("Informe a distancia que deseja percorrer(km):")) #Usuario irá informar qual distancia percorrerá com seu veículo
capacidade_total = int(input("Informe a capacidade total do taque de seu automóvel(l):")) #Usuario irá informar a capacidade total de seu veiculo (l)
consumo = int(input("Informe o consumo de seu automóvel:"))#Usuario irá informar o consumo de seu automóvel

if consumo * capacidade_total <= distancia: #se o consumo vezes a capacidade for menor que a distancia
    print(f"Não há necessidade de abastecimento!") #mostrará na tela que será necessário abastecer

else:# se o consumo e a capacidade for maior que a distancia
    print(f"Será necessario abastecer!")#mostrar que não será necessário abastecer


"Conversao de Distancia"
"Escreva um programa que solicite uma distancia em quilometros e a converta para milhas."

distancia = float(input("Informe uma distância(km):"))
milha = distancia / 1.609

print(f"-"*40)
print(f"{distancia}km = {milha:.3f}mi")
print(f"-"*40)
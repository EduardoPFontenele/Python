"A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159"
"- Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π."

def area_circunferencia():

    #Usuario irá informar o valor referente ao raio da circunferência
    raio = float(input("Informe o valor do raio da circunferência: "))

    Area = 3.14159 * (raio ** 2) #Formula para calcular área da circunferencia

    print(f"Area da Circunferencia = {Area}") #Mostra Area

if __name__ == "__area_circunferencia__":
    area_circunferencia()

def main():
    area_circunferencia()
if __name__ == "__main__":
    main()

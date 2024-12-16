"Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu"
"raio (R). A fórmula para calcular o volume é: (4/3) * pi * R3. Considere (atribua) para pi o" 
"valor 3.14159."

"Dica: Ao utilizar a fórmula, procure usar (4/3.0) ou (4.0/3), pois algumas linguagens (dentre elas o C++),"
"assumem que o resultado da divisão entre dois inteiros é outro inteiro."

def volume_esfera():

    raio = float(input("Informe o raio da esfera:")) #Usuario informará o raio da esfera
    pi = 3.14159

    VOLUME = (4/3) * pi * (raio**3) #Formula para calcular o volume de uma esfera

    print(f"VOLUME = {VOLUME:.3f}") #Mostra VOLUME

if __name__ == "__volume_esfera__":
    volume_esfera()

def main():
    volume_esfera()
if __name__ == "__main__":
    main()
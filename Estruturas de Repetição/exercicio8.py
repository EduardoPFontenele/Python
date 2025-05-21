def imposto():

    for i in range(5): #Laco para usuario informar 5 valores
        compra = float(input(f"Informe o valor da compra {i+1}:R$ "))

    #Condicionais para verificação do valor das compras
        if compra < 100:
            imposto = compra * (5/100)
            imposto_total = compra + imposto
            print(f"Imposto aplicado = 5%")
            print(f"Imposto a ser pago = R$ {imposto:.2f}")
            print(f"Imposto total: R${imposto_total:.2f}")
            print(f"-" * 30)

        elif compra >= 100 and compra <= 500:
            imposto = compra * (10/100)
            imposto_total = compra + imposto
            print(f"Imposto aplicado = 10%")
            print(f"Imposto a ser pago = R$ {imposto:.2f}")
            print(f"Imposto total: R${imposto_total:.2f}")
            print(f"-" * 30)
        else:
            imposto = compra * (15/100)
            imposto_total = compra + imposto
            print(f"Imposto aplicado = 15%")
            print(f"Imposto a ser pago = R$ {imposto:.2f}")
            print(f"Imposto total: R${imposto_total:.2f}")
            print(f"-" * 30)
if __name__ == "__imposto__":
    imposto()

def main():
    imposto()
if __name__ == "__main__":
    main()

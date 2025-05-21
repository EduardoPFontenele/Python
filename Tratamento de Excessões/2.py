def main():

    try:
        Nota = float(input(f"Informe uma Nota de 0 à 10: "))

        if Nota < 0 or Nota > 10:
            raise ValueError (f"A nota deve estar entre 0 e 10.")
    
    except ValueError as r:
        print(f"-" * 40)
        print(f"ERRO: {r}")
        print(f"-" * 40)
    
    else:
        print(f"-" * 40)
        print(f"NOTA = {Nota}")
        print(f"-" * 40)
        

if __name__ == "__main__":
    main()
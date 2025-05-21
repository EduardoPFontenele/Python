
def main():

    try:
        idade = int(input(f"Informe sua idade: "))

        if idade < 0:
            raise ValueError(f"A idade deve ser um inteiro positivo.")
    
    except ValueError as e:
        print(f"-" * 45)
        print(f"ERRO: {e}")
        print(f"-" * 45)
    
    else:
                
        print(f"-" * 30)
        print(f"Idade = {idade}")
        print(f"-" * 30)
        
if __name__ == "__main__":
    main()



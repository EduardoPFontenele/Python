def validar_senha(senha):
        
    ERRO = ""
    CONDICAO = False

    if len(senha) < 8:
        ERRO += "ERRO: A senha deve ter no mínimo 8 caracteres.\n"
        CONDICAO = True
            
    if not any(caracter.isdigit() for caracter in senha):
        ERRO += "ERRO: A senha deve conter ao menos um digito numérico.\n"
        CONDICAO = True
            
    if not any(caracter.isupper() for caracter in senha): 

        ERRO += "ERRO: A senha deve conter pelo menos um caracter maiúsculo\n"
        CONDICAO = True

    try:
        if CONDICAO == True:
            raise ValueError(ERRO)
    
    except ValueError as Erro:
        print(f"{Erro}")
    
    else:
        print(f"-" * 30)
        print(f"SENHA = {senha}")
        print(f"-" * 30)
            
def main():

    senha = input(f"Informe sua senha: ")

    validar_senha(senha)

if __name__ == "__main__":
    main()
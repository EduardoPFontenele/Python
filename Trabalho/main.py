from Sign_In import cadastrar_usuario
from Login import logar_na_conta

def main():
   
    DADOS = []
    
    print(f"\n🎉 Bem-vindo ao Quiz Online 🎉")
    
    while True:
        print(f"""
╔════════════════════════════════╗
║        🧭 MENU PRINCIPAL       ║
╠════════════════════════════════╣
║  1. 💾 Cadastrar Usuário       ║
║  2. 🔐 Login                   ║
║  0. 🚪 Sair                    ║
╚════════════════════════════════╝""")

        try:
            opcao = int(input(f"➡️  Escolha a opção que deseja realizar: "))
        
            if opcao == 1:
                print(f"""
    ╔════════════════════════════════════════════════╗
    ║            📋 CADASTRO DE USUÁRIO              ║  
    ╠════════════════════════════════════════════════╣""")
                #Coletando dados do usuário
                nome = input(f"👤 Nome de Usuário: ")
                senha = input(f"🔑 SENHA: ")
                permissao = input(f"👑 É administrador? (s/n): ")

                cadastrar_usuario('dados.txt',nome,senha,permissao)
            
            elif opcao == 2:
                print(f"""
    ╔════════════════════════════════════════════════╗
    ║            🔑 LOGIN DE USUARIO                 ║  
    ╠════════════════════════════════════════════════╣""")
                #Coletando dados do usuário
                nome = input(f"👤 Nome de Usuario: ")
                senha = input(f"🔑 SENHA: ")

                logar_na_conta('dados.txt',nome,senha,DADOS)
            
            elif opcao == 0:
                print(f"\n⬇️  Finalizando Programa. . .")
                break

            else:
                print(f"\n🛑 Opção Inválida. Tente Novamente")
        
        except ValueError:
            print(f"\n❗Valor Inválido. Digite a opção novamente.")
            

if __name__ == "__main__":
    main()
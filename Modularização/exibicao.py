def mostrar_livros(lista):

    if len(lista) > 0:

        for titulo,autor in lista.items():
            print(f"Título: {titulo} | Autor: {autor}")
    
    else:
        print(f"\nNão há Títulos Cadastrados!")
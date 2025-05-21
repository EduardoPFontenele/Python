def adicionar_livros(lista,título,autor):
        
    lista[título] = autor
    print(f"\n✅| Livro Adicionado à biblioteca")

    return lista

def remover_livro(lista,titulo):

    if titulo in lista:
        
        del lista[titulo]
        print(f"\n✅| Livro '{titulo}' Removido!")

    else:
        print(f"\n❌| Livro '{titulo}' não está na Biblioteca!")
    
    return lista
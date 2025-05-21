from collections import defaultdict, namedtuple, Counter

Produto = namedtuple('Produto', ['nome', 'preco', 'quantidade'])

def criar_produtos():

    return [Produto("Caneta", 2.50, 100), Produto("Lápis", 1.00, 150), Produto("Borracha", 0.50, 80)]

def contar_vendas(vendas):

    vendas_contadas = defaultdict(int)

    for produto in vendas:
        vendas_contadas[produto] += 1

    return vendas_contadas

def atualizar_estoque(produtos, vendas_contadas):

    estoque = {}
    for produto in produtos:

        estoque[produto.nome] = produto.quantidade - vendas_contadas.get(produto.nome, 0)

    return estoque

def obter_mais_vendidos(vendas_contadas):

    return Counter(vendas_contadas).most_common(2)

def formatar_saida(estoque, mais_vendidos):

    mais_vendidos_formatado = []  
    for item, quantidade in mais_vendidos:
        mais_vendidos_formatado.append(f"{item},{quantidade}")
    
    print(f"- Estoque atualizado: {estoque}")
    print(f"- Mais vendidos: {mais_vendidos_formatado} ")

def main():

    produtos = criar_produtos()
    vendas = ["Caneta", "Lápis", "Caneta", "Borracha", "Caneta"]
    
    vendas_contadas = contar_vendas(vendas)
    estoque_atualizado = atualizar_estoque(produtos, vendas_contadas)
    mais_vendidos = obter_mais_vendidos(vendas_contadas)

    formatar_saida(estoque_atualizado, mais_vendidos)

if __name__ == "__main__":
    main()
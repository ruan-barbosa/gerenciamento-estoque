estoque = {
    "chineque": [10, 1.50]
}
historico_vendas = []

def cadastrar_produto():
    nome_produto = input("Digite o nome do produto: ")

    if nome_produto in estoque:
        print("Esse produto já está cadastrado!")
        return
    
    try:
        quantidade = int(input("Digite a quantidade: "))
        preco = float(input("Digite o preço: "))
    except ValueError:
        print("Quantidade ou preço inválido!")
        return

    estoque[nome_produto] = [quantidade, preco]
    print("Produto cadastrado com sucesso!")

def realizar_venda():
    nome_produto = input("Digite o nome do produto que deseja comprar: ")

    # Verifica se o produto existe
    if nome_produto not in estoque:
        print("Produto não encontrado no estoque!")
        return

    try:
        quantidade_vendida = int(input("Digite a quantidade desejada: "))
    except ValueError:
        print("Quantidade inválida!")
        return

    quantidade_estoque, preco = estoque[nome_produto]

    # Verifica se há quantidade suficiente
    if quantidade_vendida <= 0:
        print("A quantidade deve ser maior que zero!")
        return

    if quantidade_vendida <= quantidade_estoque:
        # Atualiza o estoque
        estoque[nome_produto][0] -= quantidade_vendida

        # Calcula valor total
        valor_total = quantidade_vendida * preco

        # Registra no histórico
        venda = (nome_produto, quantidade_vendida, valor_total)
        historico_vendas.append(venda)

        print("Venda realizada com sucesso!")
        print(f"Valor total: R$ {valor_total:.2f}")
    else:
        print("Estoque insuficiente!")

def exibir_relatorio():
    print("\n=== RELATÓRIO DE INVENTÁRIO ===")

    if not estoque:
        print("Estoque vazio!")
        return

    for nome_produto, dados in estoque.items():
        quantidade, preco = dados
        print(f"Produto: {nome_produto}")
        print(f"Quantidade em estoque: {quantidade}")
        print(f"Preço unitário: R$ {preco:.2f}")
        print("-" * 30)

while True:
    print("Escolha o que quer fazer:\n1 - Cadastrar produto\n2 - Comprar\n3 - Relatório\n4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        realizar_venda()
    elif opcao == "3":
        exibir_relatorio()
    elif opcao == "4":
        break
    else:
        print("Opção invalida")
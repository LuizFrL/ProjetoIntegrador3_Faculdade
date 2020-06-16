from ProjetoIntegrador3_Faculdade.Projeto_3.Base_Dados.Conexao import Conexao


class Cliente(Conexao):
    def __init__(self, nome):
        Conexao.__init__(self)
        self.nome = nome
        self.carrinho = []

    def comprar(self):
        produtos = list(self.select_query('SELECT * FROM Produtos').values())
        for i, produto in enumerate(produtos):
            print(i, '-', produto['nome_produto'], '-', produto['preco'])
        escolha = int(input('Item desejado: '))
        self.carrinho.append(produtos[escolha])

    def finalizar_compra(self):
        for item in self.carrinho:
            query = f"""
            INSERT INTO Compras
            VALUES ('{item["nome_produto"]}', '{item["preco"]}', '{self.nome}')
            """
            self.insert_query(query)
        print('Compras feitas com sucesso!')


if __name__ == '__main__':
    cliente = Cliente('Pedro')
    cliente.comprar()
    cliente.finalizar_compra()

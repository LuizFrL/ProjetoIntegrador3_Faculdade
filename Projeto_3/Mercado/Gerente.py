from ProjetoIntegrador3_Faculdade.Projeto_3.Base_Dados.Conexao import Conexao


class Gerente(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def get_produtos(self):
        return self.select_query('SELECT * FROM Produtos')

    def get_funcionarios(self):
        return self.select_query('SELECT * FROM Funcionarios')

    def adicionar_produto(self):
        nome_produto = input('Nome do produto: ')
        preco_produto = float(input('Preço: '))
        self.insert_query(f"INSERT INTO Produtos VALUES (NULL, '{nome_produto}', '{preco_produto}')")

    def adicionar_funcionario(self):
        nome = input('Nome Novo Funcionário: ')
        cpf = input('CPF do funcionário: ')
        salario = float(input('Salário do funcionario: '))
        self.insert_query(f"INSERT INTO Funcionarios VALUES ('{nome}', '{cpf}', '{salario}')")

    def remover_funcionario(self):
        funcionarios = self.get_funcionarios()
        self.delete_items(funcionarios, 'Funcionarios', 'nome')


    def remover_produto(self):
        produtos = self.get_produtos()
        self.delete_items(produtos, 'Produtos', 'nome_produto')


    def update_preco_produto(self):
        produtos = list(self.get_produtos().values())
        for i, val in enumerate(produtos):
            print(i, end='')
            for v in val.values():
                print(' - ', end=f'{v}')
            print()
        escolha = int(input('Deseja mudar o preço de qual produto? '))
        item = produtos[escolha]
        query = f"""
        UPDATE Produtos
        SET preco = '{float(input("Digite o novo preço: "))}'
        WHERE id = '{item["id"]}'
        """
        self.update_delete_query(query)

    def delete_items(self, inf, table, key):
        if inf:
            for linha, informacao in inf.items():
                print(linha, end=' - ')
                for v in informacao.values():
                    print(v, end=' - ')
        else:
            print('Nada registrado')
            return
        escolha = int(input('\nO que deseja remover? '))
        self.update_delete_query(f"DELETE FROM {table} WHERE {key} = '{inf[escolha][key]}'")


if __name__ == '__main__':
    gerente = Gerente()
    gerente.update_preco_produto()

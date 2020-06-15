from ProjetoIntegrador3_Faculdade.Projeto_3.Base_Dados.Conexao import Conexao


class Gerente(Conexao):
    def __init__(self):
        Conexao.__init__(self)

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
        funcionarios = self.select_query('SELECT * FROM Funcionarios')
        self.delete_items(funcionarios, 'Funcionarios', 'nome')


    def remover_produto(self):
        produtos = self.select_query('SELECT * FROM Produtos')
        self.delete_items(produtos, 'Produtos', 'nome_produto')


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
    gerente.remover_produto()
import sqlite3, pandas, os


class Conexao(object):
    def __init__(self):
        self.mercado = sqlite3.connect(r'C:\Users\LuizFrL\PycharmProjects\untitled\ProjetoIntegrador3_Faculdade\Projeto_3\Base_Dados\Mercado.db')
        self.cursor = self.mercado.cursor()
        self.__criar_tabelas()

    def __criar_tabelas(self):
        query = """
        CREATE TABLE IF NOT EXISTS Funcionarios(
        nome text,
        cpf text,
        salario text
        )|
        CREATE TABLE IF NOT EXISTS Produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_produto text,
        preco float
        )|
        CREATE TABLE IF NOT EXISTS Compras (
        produto text,
        preco float,
        cliente text
        )
        """
        for q in list(query.split('|')):
            self.cursor.execute(q)
        self.mercado.commit()

    def select_query(self, query):
        dataframe = pandas.read_sql(query, self.mercado).to_dict('index')
        return dataframe

    def insert_query(self, query):
        self.cursor.execute(query)
        self.mercado.commit()
        print('Dados inseridos com sucesso!')

    def update_delete_query(self, query):
        if query.upper().find('WHERE') != -1:
            row_count = self.cursor.execute(query).rowcount
            self.mercado.commit()
            print('Total de {} linha(s) afetadas'.format(row_count))


if __name__ == '__main__':
    a = Conexao()
    a.insert_query("INSERT INTO Funcionarios VALUES ('Gustavo Coelho Finger', '063.632.711.69', '1000')")
    result = a.select_query('SELECT * FROM Funcionarios')
    print(result.values())

from os import getenv
from pathlib import Path

import mysql.connector as mc
from dotenv import load_dotenv
from mysql.connector import Error


class Database:
    def __init__(self):
        load_dotenv()
        self.host = getenv('DB_HOST')
        self.username = getenv('DB_USER')
        self.password = getenv('DB_PASSWORD')
        self.database = getenv('DB_SCHEMA')
        self.connection = None
        self.cursor = None

    def conectar(self):
        try:
            self.connection = mc.connect(
                host = self.host,
                database = self.database,
                user = self.username,
                password = self.password
            )

            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
                print('Conexão ao bando de dados realizada com sucesso!')
        except Error as e:
            print(f'Erro de conexão: {e}')
            self.connection = None
            self.cursor = None

    def desconectar(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print('Conexão encerrada com sucesso')

    def executar(self, sql, params = None):
        """Executa uma instrução do banco de dados."""

        if not self.connection or not self.cursor:
            print('Conexão ao banco de dados não estabelecida')
            return

        try:
            self.cursor.execute(sql, params)

            if self.cursor.description:
                return self.cursor.fetchall()

            self.connection.commit()
            return self.cursor.rowcount

        except Error as e:
            print(f'Erro de execução: {e}')
            return

    # Método de entrada no contexto (para uso com `with`)
    def __enter__(self):
        self.conectar()
        return self

# Método de saída no contexto (para uso com `with`)
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.desconectar()

"""
Definição do caminho absoluto até o arquivo de script sql que será
executado para criar o banco de dados na primeira vez que a aplicação
for utilizada. Esse caminho não depende do sistema operacional.
"""





BASE_DIR = Path(__file__).resolve().parent.parent
SQL_PATH = BASE_DIR / "data" / "tarefas.sql"


def init_db(sql_filepath=SQL_PATH):

    load_dotenv()

    try:
        conexao = mc.connect(
            host = getenv('DB_HOST'),
            user = getenv('DB_USER'),
            password = getenv('DB_PASSWORD')
        )
        cursor = conexao.cursor()

        with open(sql_filepath, 'r', encoding = 'utf-8') as arquivo:
            sql = arquivo.read()

        cursor.execute(sql)
        conexao.commit()

        cursor.close()
        conexao.close()
        print('Schema e tabelas inicializados com sucesso.')

    except Error as e:
        print(f'Erro no banco de dados: {e}')
    except FileNotFoundError:
        print('O arquivo especifico não pôde ser encontrado')
        


#db = Database()
#db.conectar()
#print(db.executar('select * from tipo_combustivel;'))
#db.desconectar()
from datetime import datetime

import tarefas
from tarefas.models.database import Database


class Tarefa:
    """Provê métodos para armazenar, recuperar r processar os dados das
    tarefas criadas a partir do formulário principal
    """

    def __init__(self, titulo, id = None, data_conclusao = None):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao


    def salvarTarefa(self):
        """Salva a tarefa no banco de dados."""

        sql = 'INSERT INTO tarefas (titulo_tarefa, data_conclusao) VALUES (%s, %s);'
        params = (self.titulo, self.data_conclusao) # protege contra SQL Injection

        # Gerenciador de contexto (with)
        # Acessa os métodos __enter__ e __exit__ da classe
        with Database() as db:
            db.executar(sql, params)

    
    @staticmethod
    def listarTarefas():
        """Retorna uma lista com todas as tarefas cadastradas."""

        sql = '''
        SELECT id_tarefa, titulo_tarefa, data_conclusao FROM tarefas LIMIT 100;
        '''
        with Database() as db:
            tarefas_banco = db.executar(sql)

        return tarefas_banco if tarefas_banco else []



@staticmethod
def apagarTarefa():
    sql = '''DELETE FROM tarefas WHERE id_tarefa = %s;'''

    with Database() as db:
        db.executar(sql)



# Área 51 (testes)
tarefa = Tarefa('minha nova tarefa')
tarefa.salvarTarefa()
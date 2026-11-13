from datetime import datetime
 
from tarefas.models.database import Database
 
class Tarefa:
    """Provê métodos para armazenar, recuperar e processar os dados das
    tarefas criadas a partir do formulário principal.
    """
 
    def __init__(self, titulo, id = None, data_conclusao = None):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao
 
    def salvarTarefa(self):
        """Salva a tarefa no banco de dados."""
        sql = 'INSERT INTO tarefas (titulo_tarefa, data_conclusao) VALUES (%s, %s);'
        params = (self.titulo, self.data_conclusao)
 
        with Database() as db:
            db.executar(sql, params)
 
    @staticmethod
    def listarTarefas() -> list:
        """Retorna uma lista com todas as tarefas cadastradas."""
        sql = '''SELECT id_tarefa, titulo_tarefa, data_conclusao
        FROM tarefas LIMIT 100; '''
 
        with Database() as db:
            tarefas_banco = db.executar(sql)
 
        return tarefas_banco if tarefas_banco else []
   
    @staticmethod
    def apagarTarefa(id_tarefa):
        sql = """DELETE FROM tarefas WHERE id_tarefa = %s;"""
        params = (id_tarefa,)
        with Database() as db:
            db.executar(sql, params)
 
    @classmethod
    def carregarTarefa(cls, id_tarefa):
        """Carrega uma tarefa específica do banco de dados na memória."""
        sql = 'SELECT id_tarefa, titulo_tarefa, data_conclusao FROM tarefas WHERE id_tarefa = %s;'
        params = (id_tarefa,)
       
        with Database() as db:
            resultado = db.executar(sql, params)
           
        if resultado:
            dados = resultado[0]
            return cls(titulo=dados['titulo_tarefa'], id=dados['id_tarefa'], data_conclusao=dados['data_conclusao'])
        return None
 
    def atualizarTarefa(self):
        """Atualiza a tarefa existente no banco com os novos valores."""
        sql = '''UPDATE tarefas
                 SET titulo_tarefa = %s, data_conclusao = %s
                 WHERE id_tarefa = %s;'''
        params = (self.titulo, self.data_conclusao, self.id)
       
        with Database() as db:
            db.executar(sql, params)
 
class Renomear:
    def __init__(self, id,  n_titulo, n_data_conclusao = None ):
        self.n_titulo = n_titulo
        self.n_data_conclusao = n_data_conclusao
 
    def Alterar():
        sql = '''UPDATE nome_da_tabela
                SET
                titulo_tarefa = '',
                data_conclusao = 00:00:00
                WHERE
                id = id;'''
 
# Área 51 (testes)
#tarefa = Tarefa('Minha nova tarefa')
#tarefa.salvarTarefa()
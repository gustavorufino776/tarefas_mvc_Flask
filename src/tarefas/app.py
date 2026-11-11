from flask import Flask, redirect, render_template, request, url_for

from tarefas.models.database import init_db
from tarefas.models.tarefa import Tarefa

app = Flask(__name__)

with app.app_context():
    init_db()

@app.route('/test')
def test():
    return 'Servidor online!'

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        titulo_form = request.form['tituloTarefa']
        data_conclusao_form = request.form['dataConclusao']

        data_corrigida = data_conclusao_form if data_conclusao_form != '' else None

        tarefa = Tarefa(titulo=titulo_form, data_conclusao=data_corrigida)

        tarefa.salvarTarefa()

        return redirect(url_for('home'))

    tarefas = Tarefa.listarTarefas()

    return render_template(
        'base.html',
        titulo_da_pagina='Minha lista de tarefas',
        tarefas_da_pagina=tarefas
        )

# Crie uma nova funcionalidade para apagar cada uma das tarefas cadastradas
@app.route('/delete/<int:id>')
def apagar_id_especificado(id):
    pass


    
if __name__=='__main__':
    app.run()
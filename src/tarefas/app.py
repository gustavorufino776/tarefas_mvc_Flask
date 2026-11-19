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
 
        data_corrigida = data_conclusao_form or None
 
        # Instanciamos uma nova tarefa com os dados recebidos do form
        tarefa = Tarefa(titulo=titulo_form, data_conclusao=data_corrigida)
       
        # Salvamos a tarefa no banco
        tarefa.salvarTarefa()
 
        return redirect(url_for('home'))
 
    tarefas = Tarefa.listarTarefas()
 
    return render_template(
        'base.html',
        titulo_da_pagina='Minha lista de tarefas',
        tarefas_da_pagina=tarefas
    )
 
@app.route('/delete/<string:uuid_publico>')
def apagar_id_especificado(uuid_publico):
    Tarefa.apagarTarefa(uuid_publico)
    return redirect(url_for('home'))
 
@app.route('/edit/<string:uuid_publico>', methods=['GET', 'POST'])
def editar_tarefa(uuid_publico):
    if request.method == 'POST':
        titulo_form = request.form['tituloTarefa']
        data_conclusao_form = request.form['dataConclusao']
        data_corrigida = data_conclusao_form or None
 
        tarefa = Tarefa(titulo=titulo_form, data_conclusao=data_corrigida, uuid_publico=uuid_publico)
        tarefa.atualizarTarefa()
 
        return redirect(url_for('home'))
 
    tarefas = Tarefa.listarTarefas()
    tarefa_selecionada = Tarefa.carregarTarefa(uuid_publico)
 
    return render_template(
        'base.html',
        titulo_da_pagina='Editar tarefa',
        tarefas_da_pagina=tarefas,
        tarefa_edicao=tarefa_selecionada
    )
 
if __name__ == '__main__':
    app.run()
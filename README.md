# Gerenciador de tarefas
 
Este projeto servirá para aprimorarmos nossa lógica de programação ao mesmo tempo em que explorarmos conceitos e técnicas de programação back-end e fullstack. Vamos utilizar e desenvolver o conceito de MVC (Model-View-Controler), algumas particularidades da Programação Orientada a Objetos, Programação Funcional, persistência de dados MySQL, microframework Flask e gerenciador de pacotes do Python (Astral uv).
 
### Alguns passos iniciais para preparar o projeto:
1. Caso não esteja instalado, prepare o uv no seu OS:
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
 
2. Faça a inicialização do projeto com o comando:
```bash
uv init
```
Até então utilizavamos um layout de pacote (package layout) denominado *flat-layout*. O uv adota uma estrutura mais moderna chamada *src-layout*, que previne erros de importação comuns chamados `import shadowing` (importações mascaradas).
 
3. Crie um ambiente virtual do Python
 
 Ative o ambiente virtual se necessário:
 ```bash
.\.venv\Scripts\Activate.ps1  # no powershell do Windows
 source .venv/Script/activate # no Git Bash do Windows
 source .venv/bin/activate # no Bash do Linux
```

4. Instale o Flask
```bash
uv add flask
```
Será criado um arquivo uv.lock contendo as dependências (requerimentos) e versões dos pacotes do seu projeto.

5. Crie um arquivo app.py contendo o código inicial do projeto
```python
from flask import Flask

app = Flask(___name___)

@app.route('/test')
def test():
    return 'Servidor online!'
```

6. teste a aplicação iniciando o servidor do Flask
```bash
uv run flask run
```
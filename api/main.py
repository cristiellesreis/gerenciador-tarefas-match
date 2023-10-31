from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tarefas = []

class Tarefa:
    def __init__(self, id, descricao, data, prioridade, concluida) -> None:
        self.id = id
        self.descricao = descricao
        self.data = data
        self.prioridade = prioridade
        self.concluida = concluida



prioridade_para_valor = {"Alta": 1, "Media": 2, "Baixa": 3}


@app.route("/")
def index():
    tarefas_ordenadas = sorted(tarefas, key=lambda x: (prioridade_para_valor[x.prioridade], x.descricao))
    return render_template("index.html", tarefas=tarefas_ordenadas)


@app.route("/adicionar", methods=['POST'])
def adicionar_tarefa():
    global tarefas
    tarefa = Tarefa(len(tarefas) + 1, request.form['descricao'],  request.form['data'],  request.form['prioridade'], False)
    
    tarefas.append(tarefa)
    return redirect("/")


@app.route('/excluir/<int:tarefa_id>', methods=['DELETE'])
def excluir_tarefa(tarefa_id):
    global tarefas
    for tarefa in tarefas:
        if tarefa.id == tarefa_id:
            tarefas.remove(tarefa)

    return '', 200


@app.route('/concluir/<int:tarefa_id>', methods=['PUT'])
def concluir_tarefa(tarefa_id):
    global tarefas
    tarefa = next((t for t in tarefas if t.id == tarefa_id), None)
    tarefa.concluida= True
    
    return redirect("/")


if __name__ == "__main__":
    app.run()


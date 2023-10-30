from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tarefas = []

prioridade_para_valor = {"Alta": 1, "Media": 2, "Baixa": 3}


@app.route("/")
def index():
    tarefas_ordenadas = sorted(tarefas, key=lambda x: (prioridade_para_valor[x['prioridade']], x['descricao']))
    return render_template("index.html", tarefas=tarefas_ordenadas)


@app.route("/adicionar", methods=['POST'])
def adicionar_tarefa():
    tarefa = {
        "id": len(tarefas) + 1,
        "descricao": request.form['descricao'],
        "data": request.form['data'],
        "prioridade": request.form['prioridade'],
        "concluida": False
    }
    tarefas.append(tarefa)
    return redirect("/")


@app.route('/excluir/<int:tarefa_id>', methods=['DELETE'])
def excluir_tarefa(tarefa_id):
    global tarefas
    tarefas = [tarefa for tarefa in tarefas if tarefa['id'] != tarefa_id]
    return '', 204


@app.route('/concluir/<int:tarefa_id>', methods=['PUT'])
def concluir_tarefa(tarefa_id):
    global tarefas
    tarefa = next((t for t in tarefas if t['id'] == tarefa_id), None)
    tarefa["concluida"] = True
    return tarefa


if __name__ == "__main__":
    app.run()


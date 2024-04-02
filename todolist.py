from flask import Flask, render_template, request, redirect, url_for
#primeiro a gente importa o flask, chama o render_template para redenrizar meu index na tela, 
app = Flask(__name__)

# Lista de tarefas
todo_list = []

@app.route('/')

def index():
    return render_template('index.html', todo_list=todo_list, )

@app.route('/add', methods=['POST'])

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    name = request.form['nome']
    todo_list.append((name, task))
    return redirect(url_for('index'))

@app.route('/submit', methods=['POST'])
def add_name():
    name = request.form['nome']
    todo_list.append(name)
    # Processar os dados do formulário...
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
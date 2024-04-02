from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de tarefas
todo_list = []

@app.route('/')
def index():
    return render_template('index.html', todo_list=todo_list)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    todo_list.append(task)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
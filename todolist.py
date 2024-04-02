def adicionar_tarefa(tarefa, lista):
    lista.append(tarefa)
    return lista

def exibir_tarefas(lista):
    if lista:
        print("Lista de Tarefas:")
        for i, tarefa in enumerate(lista, start=1):
            print(f"{i}. {tarefa}")
    else:
        print("Nenhuma tarefa na lista.")

def main():
    todolist = []
    
    while True:
        print("\n1. Adicionar Tarefa")
        print("2. Exibir Tarefas")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            tarefa = input("Digite a tarefa: ")
            todolist = adicionar_tarefa(tarefa, todolist)
        elif escolha == '2':
            exibir_tarefas(todolist)
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
            
if __name__ == "__main__":
    main()
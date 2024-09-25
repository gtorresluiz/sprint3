# CRUD de exercícios clínicos

#exemplos
exercises = {
    1: "Coordenação visual",
    2: "Precisão manual"
}

def add_exercise():
    exercise = input("Digite o nome do exercício clínico: ")
    new_id = max(exercises.keys(), default=0) + 1  
    exercises[new_id] = exercise
    print(f"Exercício '{exercise}' adicionado com sucesso!")

def list_exercises():
    if not exercises:
        print("Nenhum exercício encontrado.")
    else:
        print("Lista de exercícios clínicos:")
        for key, exercise in exercises.items():
            print(f"{key}. {exercise}")

def edit_exercise():
    list_exercises()
    if not exercises:
        return None
    try:
        exercise_id = int(input("Digite o número do exercício que deseja editar: "))
        if exercise_id in exercises:
            new_name = input("Digite o novo nome do exercício: ")
            exercises[exercise_id] = new_name
            print(f"Exercício atualizado para '{new_name}' com sucesso!")
        else:
            print("ID inválido.")
    except ValueError:
        print("Por favor, insira um número válido.")

def delete_exercise():
    list_exercises()
    if not exercises:
        return None
    try:
        exercise_id = int(input("Digite o número do exercício que deseja deletar: "))
        if exercise_id in exercises:
            deleted = exercises.pop(exercise_id)
            print(f"Exercício '{deleted}' deletado com sucesso!")
        else:
            print("ID inválido.")
    except ValueError:
        print("Por favor, insira um número válido.")

def show_menu():
    print("\n--- Menu de Exercícios Clínicos ---")
    print("1 - Adicionar exercício")
    print("2 - Listar exercícios")
    print("3 - Editar exercício")
    print("4 - Deletar exercício")
    print("5 - Sair")

def main():
    while True:
        show_menu()
        option = input("Escolha uma opção: ")
        
        if option == '1':
            add_exercise()
        elif option == '2':
            list_exercises()
        elif option == '3':
            edit_exercise()
        elif option == '4':
            delete_exercise()
        elif option == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()

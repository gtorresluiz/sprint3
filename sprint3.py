exercises = []

def add_exercise():
    exercise = input("Digite o nome do exercício: ")
    exercises.append(exercise)
    print(f"Exercício '{exercise}' adicionado com sucesso!")

def list_exercises():
    if not exercises:
        print("Nenhum exercício encontrado.")
    else:
        print("Lista de exercícios:")
        for i, exercise in enumerate(exercises, 1):
            print(f"{i}. {exercise}")

def edit_exercise():
    list_exercises()
    if not exercises:
        return None
    try:
        exercise_index = int(input("Digite o número do exercício que deseja editar: ")) - 1
        if 0 <= exercise_index < len(exercises):
            new_name = input("Digite o novo nome do exercício: ")
            exercises[exercise_index] = new_name
            print(f"Exercício atualizado para '{new_name}' com sucesso!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, insira um número válido.")

def delete_exercise():
    list_exercises()
    if not exercises:
        return None
    try:
        exercise_index = int(input("Digite o número do exercício que deseja deletar: ")) - 1
        if 0 <= exercise_index < len(exercises):
            deleted = exercises.pop(exercise_index)
            print(f"Exercício '{deleted}' deletado com sucesso!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, insira um número válido.")

def show_menu():
    print("\n--- Menu de Exercícios ---")
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


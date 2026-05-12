print("Добро пожаловать в Менеджер заметок!")


def show_menu():
    print("=== МЕНЕДЖЕР ЗАМЕТОК ===")
    print("1. Добавить заметку")
    print("2. Просмотреть все заметки")
    print("3. Выйти")
    print(" ")
    print(" ")
    while True:
        try:
            choice = int(input("Выберите действие: "))
            if choice == 1:
                print("Добавление заметки (пока не реализовано)")
            elif choice == 2:
                print("Список заметок (пока пуст)")
            elif choice == 3:
                break
            else:
                print("Неверный выбор, попробуйте снова")
        except Exception as e:
            print(f"Ошибка: {e}, введите число от 1 до 3")


show_menu()
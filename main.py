print("Добро пожаловать в Менеджер заметок!")
print(" ")
notes = []  # здесь будут храниться все заметки


def add_note():
    new_title = input("Введите заголовок заметки: ")
    new_text = input("Введите текст заметки: ")
    my_dict = {"title": new_title, "text": new_text}
    notes.append(my_dict)
    print("Заметка добавлена!")


def show_notes():
    if len(notes) == 0:
        print("Нет заметок. Добавьте первую!")
    else:
        for i, note in enumerate(notes, start=1):
            print(f"--- Заметка №{i} ---")
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['text']}")
            print("-" * 18)
            print(" ")


def show_menu():
    print("=== МЕНЕДЖЕР ЗАМЕТОК ===")
    print(" ")
    print("1. Добавить заметку")
    print("2. Просмотреть все заметки")
    print("3. Выйти")
    print(" ")

    while True:
        try:
            choice = int(input("Выберите действие: "))
            if choice == 1:
                add_note()
            elif choice == 2:
                show_notes()
            elif choice == 3:
                break
            else:
                print("Неверный выбор, попробуйте снова")
        except Exception as e:
            print(f"Ошибка: {e}, введите число от 1 до 3")


show_menu()




import json
NOTES_FILE = "data/notes.json"

print("Добро пожаловать в Менеджер заметок!")
print(" ")


def load_notes():  #Функция чтения из файла
    try:
        with open(NOTES_FILE, "r") as f:
            loaded = json.load(f)
        return loaded
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


notes = load_notes()  # здесь будут храниться все заметки


def save_notes(notes_list):  #Функция записи в файл
    with open(NOTES_FILE, "w") as f:
        json.dump(notes_list, f, indent=1)


def delete_note():
    if len(notes) == 0:
        print("Нет заметок для удаления")
        return
    

    show_notes()


    try:
        num = int(input("Введите номер заметки для удаления: "))
        
        if 1 <= num <= len(notes):
            deleted = notes.pop(num - 1)
            save_notes(notes)
            print(f"Заметка '{deleted['title']}' удалена!")
        else:
            print(f"Неверный номер. Допустимо от 1 до {len(notes)}")
            
    except ValueError:
        print("Ошибка: введите число")


def add_note():
    new_title = input("Введите заголовок заметки: ")
    new_text = input("Введите текст заметки: ")
    my_dict = {"title": new_title, "text": new_text}
    notes.append(my_dict)
    save_notes(notes)
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
    print("4. Удалить заметку")
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
            elif choice == 4:
                delete_note()
            else:
                print("Неверный выбор, попробуйте снова")
        except Exception as e:
            print(f"Ошибка: {e}, введите число от 1 до 3")


show_menu()










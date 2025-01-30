def change_note_status(notes):
    # Вывод всех заметок с их статусами
    for i, note in enumerate(notes):
        print(f"{i + 1}. {note['title']}: Status = {note['status']}")

    try:
        choice = int(input("Выберите номер заметки, которую хотите изменить: "))
        if choice <= len(notes) and choice > 0:
            new_status = input("Введите новый статус для этой заметки: ")
            notes[choice - 1]['status'] = new_status
            print(f"Статус заметки '{notes[choice - 1]['title']}' изменен на '{new_status}'.")
        else:
            print("Неверный выбор.")
    except ValueError:
        print("Пожалуйста, введите число.")


# Пример списка заметок
notes = [
    {'title': 'Заметка 1', 'status': 'Новая'},
    {'title': 'Заметка 2', 'status': 'Завершенная'}
]

change_note_status(notes)

from model import NoteJournal, Note
from .text import *


def menu() -> int:  # Выбор пункта меню
    print(main_menu)
    while True:
        choice = input(menu_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        print(input_error)


def show_notes(book: NoteJournal) -> list[str:str]:  # Отображение всех заметок
    if book.notes:
        print('\n' + '=' * 67)
        for note in book.notes:
            print(note)
        print('=' * 67 + '\n')
    else:
        print(journal_error)


def print_message(message: str):  # Вывод сообщения о статусе операции
    length = len(message)
    print('\n' + '=' * length)
    print(message)
    print('=' * length + '\n')


def input_note(message: str) -> dict[str:str]:  # Присвоение данных?
    print(message)
    new = Note(input(new_note[0]), input(new_note[1]))
    return new


def input_return(message: str) -> str:  # Вывод сообщения
    return input(message)


def prepare_to_save_file(book: NoteJournal):  # Преобразование листа журнала к формату для записи в текстовый файл
    new = []
    count = 0
    for note in book.notes:
        new += note.uid, ':', note.name, ':', note.comment
        if count < len(book.notes) - 1:
            new += '\n'
        count += 1
    i = 0
    while i < len(new):
        new[i] = str(new[i])
        i += 1
    new = [''.join(new)]
    return new

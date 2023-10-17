from typing import Type, List

import model
from view import menu, show_notes, print_message, input_note, input_return, prepare_to_save_file
from view import text

nj = model.NoteJournal('notes.txt')
flag: bool = True
while True:
    choice = menu()
    match choice:
        case 1:
            nj.open_file()
            print_message(text.open_successful)
        case 2:
            new_list = prepare_to_save_file(nj)
            nj.save_file(new_list)
            flag = True
        case 3:
            show_notes(nj)
        case 4:
            new = input_note(text.input_new_note)
            nj.add_note(new)
            print_message(text.note_saved(new.name))
            flag = False
        case 5:
            show_notes(nj)
            index = input_return(text.input_index)
            new = input_note(text.input_change_note)
            nj.change(int(index), new)
            old_name = nj.get_name(int(index))
            print_message(text.note_change(new.get if new.get else old_name))
            flag = False
        case 6:
            show_notes(nj)
            index = input_return(text.input_index_del)
            old_name = nj.get_name(int(index))
            nj.del_note(int(index))
            print_message(text.note_delete(old_name))
            flag = False
        case 7:
            if flag == False:
                exit_question = input(print(text.save_reminder))
                if exit_question == 'Y' or 'y':
                    break
                else:
                    new_list = prepare_to_save_file(nj)
                    nj.save_file(new_list)
                    break
            else:
                break

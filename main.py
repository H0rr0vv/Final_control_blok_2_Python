from typing import Type, List

import model
from model import Note
from view import menu, show_notes, print_message, input_note, input_return, prepare_to_save_file
from view import text

pb = model.NoteJournal('notes.txt')
flag: bool = True
while True:
    choice = menu()
    match choice:
        case 1:
            pb.open_file()
            print_message(text.open_successful)
        case 2:
            new_list = prepare_to_save_file(pb)
            pb.save_file(new_list)
            flag = True
        case 3:
            show_notes(pb)
        case 4:
            new = input_note(text.input_new_note)
            pb.add_note(new)
            print_message(text.note_saved(new.name))
            flag = False
        case 5:
            word = input_return(text.search_word)
            result = pb.search(word)
            show_notes(result)
        case 6:
            word = input_return(text.search_word)
            result = pb.search(word)
            show_notes(pb)
            index = input_return(text.input_index)
            new = input_note(text.input_change_note)
            pb.change(int(index), new)
            old_name = pb.get_name(int(index))
            print_message(text.note_change(new.get(new.name) if new.get(new.name) else old_name))
            flag = False
        case 7:
            word = input_return(text.search_word)
            result = pb.search(word)
            show_notes(pb)
            index = input_return(text.input_index_del)
            old_name = pb.get_name(int(index))
            pb.del_note(int(index))
            print_message(text.note_delete(old_name))
            flag = False
        case 8:
            if flag == False:
                exit_question = input(print(text.save_reminder))
                if exit_question == 'Y' or 'y':
                    break
                else:
                    new_list = prepare_to_save_file(pb)
                    pb.save_file(new_list)
                    break
            else:
                break

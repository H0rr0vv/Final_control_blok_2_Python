import model
from view import menu, show_contacts, print_message, input_contact, input_return, prepare_to_save_file
from view import text

pb = model.NoteJournal('phones.txt')
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
            show_contacts(pb)
        case 4:
            new = input_contact(text.input_new_contact)
            pb.add_note(new)
            print_message(text.contact_saved(new.name))
            flag = False
        case 5:
            word = input_return(text.search_word)
            result = pb.search(word)
            show_contacts(result)
        case 6:
            word = input_return(text.search_word)
            result = pb.search(word)
            show_contacts(pb)
            index = input_return(text.input_index)
            new = input_contact(text.input_change_contact)
            pb.change(int(index), new)
            old_name = pb.get_name(int(index))
            print_message(text.contact_change(new.get('name') if new.get('name') else old_name))
            flag = False
        case 7:
            word = input_return(text.search_word)
            result = pb.search(word)
            show_contacts(pb)
            index = input_return(text.input_index_del)
            old_name = pb.get_name(int(index))
            pb.del_note(int(index))
            print_message(text.contact_delete(old_name))
            flag = False
        case 8:
            if flag == False:
                exit_quesion = input(print(text.save_reminder))
                if exit_quesion == 'Y' or 'y':
                    break
                else:
                    new_list = prepare_to_save_file(pb)
                    pb.save_file(new_list)
                    break
            else:
                break

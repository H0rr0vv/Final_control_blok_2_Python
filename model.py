class Note:
    count_id = 1

    def __init__(self, name, comment: str):  # Вызывается при создании
        self.name = name
        self.comment = comment
        self.uid = Note.count_id
        Note.count_id += 1

    def __str__(self) -> str:  # Вызывается по принт
        return f'{self.uid:>3}. {self.name:<20} {self.comment:<20}'

    def for_search(self):
        return f'{self.name} {self.comment}'.lower()


class NoteJournal:

    def __init__(self, path: str):
        self.notes: list[Note] = []
        self.path = path

    def open_file(self):  # открытие файла
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for note in data:
            _, name, comment = note.strip().split(':')
            self.notes.append(Note(name, comment))

    def add_note(self, new: Note):  # Добавление записи
        self.notes.append(new)

    def search(self, word: str) -> list[Note]:  # Поиск записи
        result = []
        for note in self.notes:
            if word.lower() in note.for_search():
                result.append(note)
                break
        return result

    def change(self, index: int, new: dict[str, str]):  # Изменение записи
        for note in self.notes:
            if index == note.uid:
                note.name = new.get('name') if not new.get('name') else note.name
                note.comment = new.get('comment') if not new.get('comment') else note.comment

    def del_note(self, index: int):  # Удаление записи
        self.notes.pop(int(index) - 1)
        """     uid = 1
        for item in phone_book:
            item['id'] = int(uid)
            uid += 1 """
        return self.notes

    def save_file(self, new: list):     # Сохранение
        with open(self.path, 'w', encoding='UTF-8') as file:
            for note in new:
                file.write(note + '\n')

    def get_name(self, uid):        # Переименование
        old_name = str
        for note in self.notes:
            if note.uid == uid:
                old_name = note.name
                return old_name

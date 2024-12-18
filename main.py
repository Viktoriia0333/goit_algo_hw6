from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        if phone not in [p.value for p in self.phones]:
            self.phones.append(Phone(phone))
        else:
            return 'Contact already has this number'

    def edit_phone(self, old, new):
        if len(new) == 10:
            for i in self.phones:
                if i.value == old:
                    index = self.phones.index(i)
                    self.phones[index] = Phone(new)
        else:
            raise ValueError

    def find_phone(self, phone):
        for i in self.phones:
            if phone == i.value:
                return i

    def remove_phone(self, phone):
        for i in self.phones:
            if phone == i.value:
                self.phones.remove(i)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data[name] if name in self.data else None

    def delete(self, name):
        self.data.pop(name) if name in self.data else None

    def __str__(self):
        result = []
        for name, record in self.data.items():
            result.append(str(record))
        return "\n".join(result)


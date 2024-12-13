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
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        if phone not in self.phones:
            if len(phone) == 10 and phone.isdigit():
                self.phones.append(Phone(phone).value)
            else:
                raise ValueError
        else:
            print('Contact already has this number')

    def edit_phone(self, old: Phone, new: Phone):
        if old in self.phones:
            index = self.phones.index(old)
            self.phones[index] = new
        else:
            print("Old number not found")

    def find_phone(self, phone: Phone):
        return phone if phone in self.phones else None

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"


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
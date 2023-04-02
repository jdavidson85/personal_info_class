class Person_data:
    def __init__(self, name, address, age, phone) -> None:
        self.name = name
        self.address = address
        self.age = age
        self.phone = phone

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_age(self, age):
        self.age = age

    def set_phone(self, phone):
        self.phone = phone

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_age(self):
        return self.age

    def get_phone(self):
        return self.phone


def print_object(obj):
    print(f'Name: {obj.name}, address: {obj.address}, age: {obj.age}, phone: {obj.phone}')


p1 = Person_data('Joe', 'Brompton ct', 37, 2345233532)
p2 = Person_data('Jacki', 'Brompton ct', 32, 987543210)
p3 = Person_data('Luke', 'Brompton ct', 7, 1234567890)

print_object(p1)
print_object(p2)
print_object(p3)
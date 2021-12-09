class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.address = None
        self.phone = None

    def __str__(self):
        return f'{self.name}, {self.age}'

    def print_person(self):
        self.phone = '123 1414'
        print(self.name, self.age)

    @staticmethod
    def static():
        print("I am a static method")


class Employee(Person):
    def __init__(self, name, age, pay):
        super().__init__(name, age)
        self.pay = pay

    def __str__(self):
        return super().__str__() + f", {self.pay}"


def main():
    Person.static()
    person1 = Person('Anna', 34)
    person2 = Person('Pelle', 42)
    emp1 = Employee('Kalle', 34, 45000)
    print(emp1)
    emp1.print_person()
    person1.email = 'anna@email.com'
    print(person1)
    person2.print_person()


if __name__ == '__main__':
    main()

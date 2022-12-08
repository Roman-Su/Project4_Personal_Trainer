class Person:
    def __init__(self, name, gender, age = 1):
        self.name = name
        self.gender = gender
        self.age = age

        self.country = "USA"

    def print_info(self):
        print("Name: {}".format(self.name))
        print("Gender: {}".format(self.gender))
        print("Age: {}".format(self.age))
        print("Country: {}".format(self.country))

    def grow_person(self, years_of_growth):
        self.age = self.age + years_of_growth


def grow_person(current_age, years_of_growth):
    return current_age + years_of_growth


# определение человека
person_1 = Person("Bob", "Male")

# вывод всей информации о Бобе по каждому свойству
print("Name: {}".format(person_1.name))
print("Gender: {}".format(person_1.gender))
print("Age: {}".format(person_1.age))
print("Country: {}".format(person_1.country))

# вывод всей информации о Бобе с помощью функции класса
person_1.print_info()

# использование внешней функции
person_1.age = grow_person(person_1.age, years_of_growth=5)

# использование функции класса
person_1.grow_person(years_of_growth=5)
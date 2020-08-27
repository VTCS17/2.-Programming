class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False
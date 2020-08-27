from Chef import chef
class Italianchef(chef):#Inheriting chef class

    def make_pasta(self):
        print("The chef makes pasta")
    def make_special(self): #overriding
        print("The chef makes Vangi Bath")
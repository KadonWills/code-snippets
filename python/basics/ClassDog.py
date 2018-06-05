class Dog:
    kind = "canine" # class variable
    def __init__(self, name):
        self.name = name #instance variable
        self.tricks = [] #instance variable
    def add_trick(self, trick):
        self.tricks.append(trick)
        
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')

print(e.name, e.tricks)
print(d.name, d.tricks)
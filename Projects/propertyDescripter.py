class Person:
    def __init__(self):
        self._name = None
        self._age = None
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        self._name = value

    @property   #getter
    def age(self):
        return self._age
    @age.setter  #setter
    def age(self,value):
        self._age = value

#creating Object
p = Person()

#setting values
p.name = "Ankur"
p.age = 19
print(p.name)
print(p.age)
    
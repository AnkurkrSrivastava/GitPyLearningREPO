#fruits = ["apple", "banana", "cherry"]
#first_letter = {fruit[0] for fruit in fruits}
#print("The first letters of the fruits are:", first_letter)


#words = "hello world"
#my_set = {word for word in words if word != ' '}
#print(my_set)


#a = {1,2}
#c = {3,4}
#print(a.isdisjoint(c))

#a = {1,2,3}
#b = {3,2,1}
#print(a == b)

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def display(self):
        print(self.title,self.author)



book1 = Book("Hamlet", "William")
book1.author = "Orwell"
book1.display()

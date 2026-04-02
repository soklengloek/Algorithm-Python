class a :
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age
    def show(self):
        print("Name:", self.name)
        print("ID:", self.id)
        print("Age:", self.age)
class b(a):
    def show(self):
        print("I'm a Student!")
class c(a):
    def show(self):
        print("I'm a Teacher!")
class d(b,c):
    def show(self):
        print ("I'm a Hybrid!")
student1 = b("Alice", "S123", 20)
teacher1 = c("Bob", "T456", 40)
hybrid1 = d("Charlie", "H789", 30)
student1.show()
teacher1.show()
hybrid1.show()
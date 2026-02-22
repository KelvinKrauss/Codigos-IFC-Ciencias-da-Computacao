class cachorro:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def latido(self):
        print("woof")
    def get_details(self):
        return f"{self.name} is {self.age} years old"
    
cachorro1 = cachorro(str(input("digite o nome")), int(input("digite a idade ")))
cachorro1.latido() 
print(cachorro1.get_details())  
cachorro2 = cachorro("rex", 3)
cachorro2.latido() 
print(cachorro2.get_details())  
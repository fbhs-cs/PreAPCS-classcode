class Dog:
    def __init__(self,breed,gender,age,name):
        self.breed = breed
        self.gender = gender
        self.age = age
        self.name = name
        self.animal_type = "dog"

class Cat:
    def __init__(self,color,short_hair,gender,age):
        self.color = color
        self.short_hair = short_hair
        self.gender = gender
        self.age = age
        self.animal_type = "cat"

def main():
    sean_dog = Dog("Akita","male",2,"Bob")  
    andrew_dog = Dog("Saint Bernard","male",5,"Charles")
    print("Sean's dog:",sean_dog.breed,sean_dog.gender,sean_dog.age)
    print("Andrew's dog:",andrew_dog.breed,andrew_dog.gender,andrew_dog.age)
    
    dakota_cat = Cat("Brown",True,"male",2)
    print("Dakota's cat is",dakota_cat.color)
    
if __name__ == "__main__":
    main()
class Dog:
    def __init__(self,breed,gender,age):
        self.breed = breed
        self.gender = gender
        self.age = age
        self.animal_type = "dog"

class Cat:
    def __init__(self,color,short_hair,gender,age):
        self.color = color
        self.short_hair = short_hair
        self.gender = gender
        self.age = age
        self.animal_type = "cat"


def main():
    seans_dog = Dog("Dachshund","female",5)
    print("Sean's dog:",seans_dog.breed, seans_dog.gender, seans_dog.age)
     
    ricos_dog = Dog("Shitzu","male",14)
    print("Rico's dog:",ricos_dog.breed, ricos_dog.gender, ricos_dog.age)
   
    nadias_cat = Cat("Black",False,"female",5)
    print("Nadia's cat is",nadias_cat.color)
    
    
    
    
    
    
if __name__ == "__main__":
    main()
    
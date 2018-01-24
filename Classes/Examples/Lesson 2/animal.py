class Dog:
    def __init__(self,breed,gender,age,name):
        self.breed = breed
        self.gender = gender
        self.age = age
        self.name = name
        self.animal_type = "dog"
    

class Cat:
    def __init__(self,color,short_hair,gender,age,name):
        self.color = color
        self.short_hair = short_hair
        self.gender = gender
        self.age = age
        self.name = name
        self.animal_type = "cat"
        

def main():
    alainas_dog = Dog("Shitzu","male",14)
    gabbys_dog = Dog("German Shephard","female",2)
    print("Alaina's dog:",alainas_dog.breed,alainas_dog.gender,alainas_dog.age)
    print("Gabby's dog:",gabbys_dog.breed,gabbys_dog.gender,gabbys_dog.age)
    ethans_cat = Cat("Black",True,"male",5)
    print("My cat is",ethans_cat.color)

if __name__ == "__main__":
    main()
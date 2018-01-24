import animal

def main():
    print("Creating dogs...")
    try:
        dog1 = animal.Dog(name="Drama",gender="female",age=14,breed="Chow/Lab")
        dog2 = animal.Dog(name="Santa's Little Helper",gender="male",age=3,breed="Greyhound")
        dog3 = animal.Dog(name="Einstein",gender="male",age=38,breed="Sheepdog")
    except:
        print("Something is wrong with your __init__ method in Dog")
        
if __name__ == "__main__":
    main()
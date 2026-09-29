from A2 import *
from filehandling import *

def getMenuChoice(): # repeatedly prompts user until it gives either a valid menu number or x
    while True:
        choice = input("""Welcome To the Pet Match System
Please Select from the following:
1. Add Pet
2. Search for Pet
3. Edit Pet
4. Delete pet
5. Generate Report
X. Exit
""").strip().upper()
        if choice in ("X", "EXIT"): # checks for x before int conversion
            return choice
        try:
            return int(choice)
        except ValueError:
            print("Please enter a valid number, or X to exit")


def getBreedClassChoice(): # asks which concrete class to build
    while True:
        try:
            print("Which breed would you like to add?")
            print("1. Alaskan Malamute")
            print("2. Australian Kelpie")
            print("3. Bengal")
            print("4. Devon Rex")
            choice = int(input("Enter your choice: "))
            if choice not in (1, 2, 3, 4):
                raise InvalidInputError("Choice must be between 1 and 4")
            return choice
        except ValueError:
            print("Please enter a number")
        except InvalidInputError as e:
            print(e)


if __name__ == "__main__":
    system = PetMatchSystem()
    system.pets = loadBreeds("PetBreed.txt") # populate system

    while True:
        choice = getMenuChoice()

        if choice in ("X", "EXIT"):
            saveBreeds("PetBreed.txt", system.pets)
            print("Goodbye!")
            break

        elif choice == 1:  # inputs to create pet object
            breedChoice = getBreedClassChoice()

            breed = input("Please enter the name of the breed you would like to add: ").strip()
            size = input("What is the size of this pet, e.g Small, Medium, Large?: ").strip()
            coat = input("Please enter the type of coat the pet has: ").strip()
            energy = input("Please describe the energy level of this pet: ").strip()
            weight = input("What is the weight of this pet, e.g 38 to 56kg?: ").strip()
            colour = input("What is the colour of this pet?: ").strip()
            shedding = input("What is the shedding level of this pet?: ").strip()
            temperament = input("Please describe the temperament of this pet: ").strip()
            lifespan = input("What is the lifespan of this pet?: ").strip()
            matchNotes = input("Any match notes for this breed?: ").strip()
            pet_id = len(system.pets) + 1  # add pet Id as I am a fan of always being able to reference objects with Ids

            if breedChoice == 1:
                pet = AlaskanMalamute(pet_id, breed, size, coat, energy, weight, colour, shedding, temperament, lifespan, matchNotes)
            elif breedChoice == 2:
                pet = AustralianKelpie(pet_id, breed, size, coat, energy, weight, colour, shedding, temperament, lifespan, matchNotes)
            elif breedChoice == 3:
                pet = Bengal(pet_id, breed, size, coat, energy, weight, colour, shedding, temperament, lifespan, matchNotes)
            else:
                pet = DevonRex(pet_id, breed, size, coat, energy, weight, colour, shedding, temperament, lifespan, matchNotes)

            system.addPet(pet)

        elif choice == 2:  # functionality for searching
            breed = input("Please enter the name of the breed you would like to Search for: ")
            pet = system.searchByName(breed)
            if pet is None:
                print("No such pet found")
            else:
                pet.displayProfile()

        elif choice == 3:  # edit option
            breed = input("Please enter the name of the breed you would like to edit: ")
            pet = system.searchByName(breed)

            if pet is None:
                print("No pet with that breed found")
            else:
                print("Current Profile:")
                pet.displayProfile()
                print("Which attributes would you like to edit?")
                attr = input("Attribute Name: ")  # collecting variables for dict
                val = input(f"New Value for {attr}: ")

                updates = {attr: val}  # create dict

                system.editPet(breed, updates)  # perform functionality with user input

        elif choice == 4:  # delete option, a lot of functionality is performed within the method
            breed = input("Which Pet would you like to delete?: ")
            system.deletePet(breed)

        elif choice == 5:  # generate report option
            print("Let's make a report")
            petType = input("Pet Type, Dog or Cat, type Any to skip: ").strip().capitalize()
            size = input("Size, type Any to skip: ").strip()
            energy = input("Energy, type Any to skip: ").strip()

            criteria = {"petType": petType, "size": size, "energy": energy}
            generateReport(system, criteria)

        else:
            print("Invalid choice, please try again")
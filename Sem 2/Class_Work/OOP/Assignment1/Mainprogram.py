from A1 import Pet, Cat, Dog, PetMatchSystem

system = PetMatchSystem()
while True:
    print("Welcome To the Pet Match System")
    choice = int(input("""Please Select from the following:
    1. Add Pet
    2. Search for Pet
    3. Edit Pet
    4. Delete pet
    """))

    if choice == 1: # inputs to create pet object
        animal = input("Please Type C for cat or D for Dog: ").lower().strip() # strip methods and lower to make sure input is handled correctly
        breed = input("Please enter the name of the breed you would like to add: ").strip()
        size = input("What is the size of this pet? E.g Small, Medium, Large?: ").strip()
        coat = input("Please enter the type of coat the pet has: ").strip()
        energy = input("Please describe the energy level of this pet: ").strip()
        weight = int(input("What is the weight of this pet in kg?: "))
        colour = input("What is the colour of this pet?: ").strip()
        activities_input = input("What kind of activities does this pet enjoy? You can add multiple: ").strip()
        activities = activities_input.split()
        pet_id = len(system.pets) + 1 # add pet Id as I am a fan of always being able to reference objects with Ids

        if animal == "d": # conditionals to check if cat or dog and provide additional functionality
            height = int(input("Please enter the height of the Dog in cm: "))
            pet = Dog(pet_id, breed, size, coat, energy, weight, colour, activities, height)

        elif animal == "c":
            groomingNeeds_input = input("Please enter the grooming needs of the cat. You can add many: ").strip()
            groomingNeeds = groomingNeeds_input.split()
            pet = Cat(pet_id, breed, size, coat, energy, weight, colour, activities, groomingNeeds)
        else: # more error input error checking
            print("Invalid animal type — must be C or D.")
            pet = None
        if pet is not None:
            system.addPet(pet)
        # functionality for seaching
    elif choice == 2:
        breed = input("Please enter the name of the breed you would like to Search for: ")
        pet = system.searchByName(breed)
        if pet is None:
            print("No such pet found")
        else:
            pet.displayProfile()
    # edit option
    elif choice == 3:
        breed = input("Please enter the name of the breed you would like to edit: ")
        pet = system.searchByName(breed)

        if pet is None:
            print("No pet with that breed found")
        else:
            print("Current Profile:")
            pet.displayProfile()
            print("\nWhich attributes would you like to edit?")
            attr = input("Attribute Name: ") # collecting variables for dict
            val = input(f"New Value for {attr}: ")

            updates = {attr: val} # create dict

            system.editPet(breed, updates) # perform functionality with user input
 # delete option, a lot of functionality is performed within the method
    elif choice == 4:
        breed = input("Which Pet would you like to delete?: ")
        system.deletePet(breed)
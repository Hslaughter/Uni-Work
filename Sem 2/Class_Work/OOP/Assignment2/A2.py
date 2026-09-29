class Pet:
    # base class, common attributes shared by every breed
    def __init__(self, id, breedName, petType, size, coat, energy, weight, colour, shedding):
        self.id = id
        self.breedName = breedName
        self.petType = petType
        self.size = size
        self.coat = coat
        self.energy = energy
        self.weight = weight
        self.colour = colour
        self.shedding = shedding

    def displayProfile(self): # prints attributes
        print(f"""Breed: {self.breedName}
Pet Type: {self.petType}
size: {self.size}
coat: {self.coat}
energy: {self.energy}
weight: {self.weight}
colour: {self.colour}
shedding: {self.shedding}""")

    def updateAttribute(self, attr, value):
        if not hasattr(self, attr):
            return False
        setattr(self, attr, value)
        return True


class Dog(Pet): # type subclass, dog specific behaviour goes here
    def displayProfile(self):
        super().displayProfile()
        print("Type Notes: Dog breed; check daily exercise needs")


class Cat(Pet): # type subclass, cat specific behaviour goes here
    def displayProfile(self):
        super().displayProfile()
        print("Type Notes: Cat breed; check indoor/outdoor suitability")


class AlaskanMalamute(Dog): # concrete breed class > inherits from Dog
    def __init__(self, id, breedName, size, coat, energy, weight, colour, shedding, temperament, lifespan, matchNotes):
        super().__init__(id, breedName, "Dog", size, coat, energy, weight, colour, shedding)
        self.temperament = temperament
        self.lifespan = lifespan
        self.matchNotes = matchNotes

    def displayProfile(self):
        super().displayProfile()
        print(f"Temperament: {self.temperament}")
        print(f"Lifespan: {self.lifespan}")
        print(f"Match Notes: {self.matchNotes}\n")


class AustralianKelpie(Dog): # concrete breed class > inherits from Dog
    def __init__(self, id, breedName, size, coat, energy, weight, colour, shedding, temperament, lifespan, matchNotes):
        super().__init__(id, breedName, "Dog", size, coat, energy, weight, colour, shedding)
        self.temperament = temperament
        self.lifespan = lifespan
        self.matchNotes = matchNotes

    def displayProfile(self):
        super().displayProfile()
        print(f"Temperament: {self.temperament}")
        print(f"Lifespan: {self.lifespan}")
        print(f"Match Notes: {self.matchNotes}\n")


class Bengal(Cat): # concrete breed class > inherits from Cat
    def __init__(self, id, breedName, size, coat, energy, weight, colour, shedding, temperament, lifespan, matchNotes):
        super().__init__(id, breedName, "Cat", size, coat, energy, weight, colour, shedding)
        self.temperament = temperament
        self.lifespan = lifespan
        self.matchNotes = matchNotes

    def displayProfile(self):
        super().displayProfile()
        print(f"Temperament: {self.temperament}")
        print(f"Lifespan: {self.lifespan}")
        print(f"Match Notes: {self.matchNotes}\n")


class DevonRex(Cat): # concrete breed class > inherits from Cat
    def __init__(self, id, breedName, size, coat, energy, weight, colour, shedding, temperament, lifespan, matchNotes):
        super().__init__(id, breedName, "Cat", size, coat, energy, weight, colour, shedding)
        self.temperament = temperament
        self.lifespan = lifespan
        self.matchNotes = matchNotes

    def displayProfile(self):
        super().displayProfile()
        print(f"Temperament: {self.temperament}")
        print(f"Lifespan: {self.lifespan}")
        print(f"Match Notes: {self.matchNotes}\n")

class InvalidInputError(Exception):
    # custom exception, raised when user input does not match an expected option
    pass

class PetMatchSystem:
    def __init__(self):
        self.pets = [] # list to contain all pets

    def addPet(self, pet: Pet):
        if pet.breedName == "": # checks if breed name is empty
             print("Breed Name cannot be empty")
             return False
        
        if self.searchByName(pet.breedName) is not None: # checks to see if breedname exists in system already
             print("This pet already exists")
             return False
        
        self.pets.append(pet) # appends to pet list
        print(f"{pet.breedName} added successfully")
        return True
         

    def editPet(self, breedName: str, updates: dict): # edit pet method with a dict to store potential edits
        pet = self.searchByName(breedName)
        if pet is None:
            print("That pet does not exist") # more checking
            return False
        for attr, val in updates.items(): # loop through dict
             success = pet.updateAttribute(attr, val)
             if not success:
                print(f"Could not update attribute {attr}")
        print("Profile Updated:")
        pet.displayProfile()
        return True
        

    def searchByName(self, breedName: str): # checks to see if pet already exists
        for pet in self.pets:
              if pet.breedName.lower() == breedName.lower():
                   return pet
        return None
              
        
    def deletePet(self, breedName: str): # delete method
        pet = self.searchByName(breedName)
        if pet is None:
            print(f"That pet does not exist")
            return False
        else:
            confirm = input(f"Are you sure you want to delete '{pet.breedName}'? (Y/N): ").strip().lower() # confirmation message
            if confirm == "y":
                self.pets.remove(pet)
                print(f"Successfully deleted {pet.breedName}")
                return True
            else:
                print("Deletion cancelled")
                return False


    
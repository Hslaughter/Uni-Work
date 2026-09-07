class Pet:
    # init method for parent class
    def __init__(self, id, breedName, size, coat, energy, weight, colour, activities):
        self.id = id
        self.breedName = breedName
        self.size = size
        self.coat = coat
        self.energy = energy
        self.weight = weight
        self.colour = colour
        self.activities = activities
    # display profile that displays all attributes
    def displayProfile(self):
        print(f"""Breed: {self.breedName}
size: {self.size}
coat: {self.coat}
energy: {self.energy}
weight: {self.weight}
colour: {self.colour}
activities: {', '.join(self.activities)}""")
        

    def updateAttribute(self, attr, value):
        if not hasattr(self, attr): # check if entered attribute exists
            return False
        setattr(self, attr, value)
        return True

class Dog(Pet): # child class Dog
    def __init__(self, id, breedName, size, coat, energy, weight, colour, activities, height):
        super().__init__(id, breedName, size, coat, energy, weight, colour, activities)
        self.height = height # uses parent init method and also adds additional field unique to child

    def displayProfile(self):
        super().displayProfile()
        print(f"height: {self.height}\n") #uses parent method and adds height on the end

class Cat(Pet): # child class Cat
    def __init__(self, id, breedName, size, coat, energy, weight, colour, activities, groomingNeeds):
            super().__init__(id, breedName, size, coat, energy, weight, colour, activities)
            self.groomingNeeds = groomingNeeds

    def displayProfile(self):
            super().displayProfile()
            print(f"Grooming Needs: {', '.join(self.groomingNeeds)}\n")


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


    
from A2 import *

# maps the class name string to the actual class
breedClasses = {
    "AlaskanMalamute": AlaskanMalamute,
    "AustralianKelpie": AustralianKelpie,
    "Bengal": Bengal,
    "DevonRex": DevonRex
}

def loadBreeds(filename):  # reads txt and builds the correct concrete breed object for each line
    breeds = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue # skips blank lines

                parts = line.split("|")
                className = parts[0]
                breedName, petType, size, coat, energy, weight, colour, shedding, temperament, lifespan, matchNotes = parts[1:]

                breedClass = breedClasses.get(className)
                if breedClass is not None:
                    newId = len(breeds) + 1
                    newBreed = breedClass(newId, breedName, size, coat, energy, weight, colour, shedding, temperament, lifespan, matchNotes)
                    breeds.append(newBreed)

    except FileNotFoundError:   # file does not exist yet but program can still run
        print(f"{filename} not found, starting with an empty breed list. ")
    return breeds

def saveBreeds(filename, breeds): # overwrites with info in system
    with open(filename, "w") as f:
        for breed in breeds:
            className = type(breed).__name__
            line = "|".join([
                className, breed.breedName, breed.petType, breed.size, breed.coat,
                breed.energy, str(breed.weight), breed.colour, breed.shedding,
                breed.temperament, breed.lifespan, breed.matchNotes
            ])
            f.write(line + "\n")
    print(f"Breed data saved to {filename}")

def generateReport(system, criteria: dict): # searches system.pets for breeds matching every non 'any' > writes results to a report file
    matches = []
    for breed in system.pets:
        isMatch = True
        for attr, val in criteria.items():
            if val.lower() == "any":
                continue
            if not hasattr(breed, attr) or str(getattr(breed, attr)).lower() != val.lower():
                isMatch = False
                break
        if isMatch:
            matches.append(breed)

    with open("PetMatch_report.txt", "w") as f:
        f.write("PetMatch Summary Report\n")
        f.write(f"Criteria: {criteria}\n\n")
        if not matches:
            f.write("No breed matches found.\n")
            print("No breed matches found.")
        else:
            for breed in matches:
                f.write(f"{breed.breedName} | {breed.petType} | {breed.size} | {breed.coat} | {breed.energy}\n")
                breed.displayProfile()
    print("Report saved to PetMatch_report.txt")
    return matches
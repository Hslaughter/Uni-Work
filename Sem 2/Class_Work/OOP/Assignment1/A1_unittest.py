import unittest
from A1 import Dog, Cat, PetMatchSystem

class TestSearchByName(unittest.TestCase):

    def setUp(self):
        # This runs before every test method
        self.system = PetMatchSystem()

        self.dog1 = Dog(1, "Alaskan Malamute", "Giant", "Medium", "High",
                         56, "Grey and White", ["Sledding", "Agility"], 71)
        self.cat1 = Cat(2, "American Bobtail", "Medium", "Short", "Medium",
                         7, "Brown Tabby", ["Play", "Climbing"], "Weekly brushing")

        self.system.addPet(self.dog1)
        self.system.addPet(self.cat1)

    def test_successful_search(self):
        # searching for a breed that exists returns the correct object
        result = self.system.searchByName("Alaskan Malamute")
        self.assertIsNotNone(result)
        self.assertEqual(result.breedName, "Alaskan Malamute")

    def test_unsuccessful_search(self):
        # searching for a breed that does NOT exist returns None
        result = self.system.searchByName("Golden Retriever")
        self.assertIsNone(result)

    def test_case_insensitive_search(self):
        # search should match regardless of the case typed in
        result = self.system.searchByName("alaskan malamute")
        self.assertIsNotNone(result)
        self.assertEqual(result.breedName, "Alaskan Malamute")


if __name__ == "__main__":
    unittest.main()
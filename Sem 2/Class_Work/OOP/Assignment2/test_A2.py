import unittest
import os
from A2 import *
from filehandling import *
from mainmenu import *


class TestSearchByName(unittest.TestCase):
    def setUp(self):
        self.system = PetMatchSystem()
        self.dog1 = AlaskanMalamute(1, "Alaskan Malamute", "Giant", "Medium", "High", "38 to 56kg", "Grey", "Heavy", "Friendly", "10 to 14 years", "Active lifestyle")
        self.cat1 = Bengal(2, "Bengal", "Medium To Large", "Medium", "High", "4 to 8kg", "Orange", "Minimal", "Playful", "12 to 16 years", "Needs mental stimulation")
        self.system.addPet(self.dog1)
        self.system.addPet(self.cat1)

    def test_successful_search(self):
        result = self.system.searchByName("Alaskan Malamute")
        self.assertIsNotNone(result)
        self.assertEqual(result.breedName, "Alaskan Malamute")

    def test_unsuccessful_search(self):
        result = self.system.searchByName("Golden Retriever")
        self.assertIsNone(result)

    def test_case_insensitive_search(self):
        result = self.system.searchByName("alaskan malamute")
        self.assertIsNotNone(result)
        self.assertEqual(result.breedName, "Alaskan Malamute")


class TestFileIO(unittest.TestCase):
    def setUp(self):
        self.testFile = "test_PetBreed.txt"
        with open(self.testFile, "w") as f:
            f.write("AlaskanMalamute|Alaskan Malamute|Dog|Giant|Medium|High|38 to 56kg|Grey|Heavy|Friendly|10 to 14 years|Active\n")
            f.write("Bengal|Bengal|Cat|Medium To Large|Medium|High|4 to 8kg|Orange|Minimal|Playful|12 to 16 years|Needs stimulation\n")

    def tearDown(self):
        if os.path.exists(self.testFile):
            os.remove(self.testFile)

    def test_load_breeds_creates_correct_number(self):
        breeds = loadBreeds(self.testFile)
        self.assertEqual(len(breeds), 2)

    def test_load_breeds_creates_correct_classes(self):
        breeds = loadBreeds(self.testFile)
        self.assertIsInstance(breeds[0], AlaskanMalamute)
        self.assertIsInstance(breeds[1], Bengal)

    def test_load_breeds_missing_file_returns_empty_list(self):
        breeds = loadBreeds("nonexistent_file.txt")
        self.assertEqual(breeds, [])

    def test_save_and_reload_breeds(self):
        breeds = loadBreeds(self.testFile)
        saveBreeds(self.testFile, breeds)
        reloadedBreeds = loadBreeds(self.testFile)
        self.assertEqual(reloadedBreeds[0].breedName, "Alaskan Malamute")


class TestGenerateReport(unittest.TestCase):
    def setUp(self):
        self.system = PetMatchSystem()
        self.dog1 = AlaskanMalamute(1, "Alaskan Malamute", "Giant", "Medium", "High", "38 to 56kg", "Grey", "Heavy", "Friendly", "10 to 14 years", "Active lifestyle")
        self.cat1 = Bengal(2, "Bengal", "Medium To Large", "Medium", "High", "4 to 8kg", "Orange", "Minimal", "Playful", "12 to 16 years", "Needs mental stimulation")
        self.system.addPet(self.dog1)
        self.system.addPet(self.cat1)

    def tearDown(self):
        if os.path.exists("PetMatch_report.txt"):
            os.remove("PetMatch_report.txt")

    def test_report_finds_matching_dog(self):
        criteria = {"petType": "Dog", "size": "Giant", "energy": "Any"}
        matches = generateReport(self.system, criteria)
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0].breedName, "Alaskan Malamute")

    def test_report_no_match_found(self):
        criteria = {"petType": "Dog", "size": "Tiny", "energy": "Any"}
        matches = generateReport(self.system, criteria)
        self.assertEqual(len(matches), 0)

    def test_report_creates_file(self):
        criteria = {"petType": "Cat", "size": "Any", "energy": "Any"}
        generateReport(self.system, criteria)
        self.assertTrue(os.path.exists("PetMatch_report.txt"))


if __name__ == "__main__":
    unittest.main()
from lab3 import note, notebook
import unittest

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.nb = notebook()
        self.note1 = note(1,"generic tag", "generic memo")
        self.note2 = note(2,"generic tag", "generic memo")
        self.nb.addNote(self.note1)
        self.nb.addNote(self.note2)

    def test_successful_search(self):
        result = self.nb.searchById(1)
        self.assertIsNotNone(result)
        self.assertEqual(result.noteId, 1)

    def test_unsuccessful_search(self):
        result = self.nb.searchById(999)
        self.assertIsNone(result)

class TestAddNote(unittest.TestCase):
    def setUp(self):
        self.nb = notebook()

    def test_addNote_success(self):
        n1 = note(1,"generic tag", "generic memo")
        result = self.nb.addNote(n1)
        self.assertTrue(result)

    def test_add_duplicate_note(self):
        self.note1 = note(1,"generic tag", "generic memo")
        self.note2 = note(1,"generic tag", "generic memo")
        self.nb.addNote(self.note1)
        result2 = self.nb.addNote(self.note2)
        self.assertFalse(result2)

if __name__ == "__main__":
    unittest.main()
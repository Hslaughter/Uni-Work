from  lab4 import *
import unittest

class Base_Test_Class(unittest.TestCase):
    def setUp(self):
        self.sys = System()
        s1 = Staff(1, 'harry', "16-12-2002", "Waterloo", "911-000")
        s2 = Staff(2, 'barry', "15-12-2002", "Wollongong", "911-000-111")
        self.sys.addStaff(s1)
        self.sys.addStaff(s2)
        
    def test_search(self):
        test = self.sys.searchStaff(1)
        self.assertIsNotNone(test)
        
    def test_bad_search(self):
        test2 = self.sys.searchStaff(3)
        self.assertIsNone(test2)

    def test_add_staff(self):
        s3 = Staff(3, 'garry', "14-12-2002", "Wollongong", "911-000-111")
        result = self.sys.addStaff(s3)
        self.assertTrue(result)

    def test_edit_staff(self):
        updates = {'staffId': 999}    
        result = self.sys.editStaff(1,updates)
        self.assertTrue(result)

    def test_del_staff(self):
        result = self.sys.delStaff(1)
        self.assertTrue(result)
    









if __name__ == "__main__":
    unittest.main()
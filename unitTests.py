import unittest
import userStories
import os
from model import GEDCOMParser as modelParser


def reader(path):
    if os.path.exists(path):
        individual, families = modelParser(path)
        return individual, families
    else:
        print("The file \"%s\" does not exist\n" % path)
        exit(-1)


class TestUserStory9(unittest.TestCase):
    def test_1(self):
        individual, families = reader("birthb4marriage_1.ged")
        self.assertEqual(userStories.birth_before_parents_marry(individual, families), False)  # add assertion here
    def test_2(self):
        individual, families = reader("Seinfelds.ged")
        self.assertNotEqual(userStories.birth_before_parents_marry(individual, families), False)  # add assertion here
    def test_3(self):
        individual, families = reader("birthb4marriage_1.ged")#for bad file
        self.assertIsNotNone(userStories.birth_before_parents_marry(individual, families))
    def test_4(self):
        individual, families = reader("Seinfelds.ged")#for good file
        self.assertIsNotNone(userStories.birth_before_parents_marry(individual, families))
    def test_5(self):
        individual, families = reader("birthb4marriage_1.ged")
        self.assertFalse(userStories.birth_before_parents_marry(individual, families))  # add assertion here


class TestUserStory5(unittest.TestCase):
    def test_1(self):
        individual, families = reader("birthb4marriage_1.ged")#good file
        self.assertEqual(userStories.marriage_before_death(individual, families), True)
    def test_2(self):
        individual, families = reader("Seinfelds.ged")
        self.assertNotEqual(userStories.marriage_before_death(individual, families), True)
    def test_3(self):
        individual, families = reader("birthb4marriage_1.ged")#for bad file
        self.assertIsNotNone(userStories.marriage_before_death(individual, families))
    def test_4(self):
        individual, families = reader("Seinfelds.ged")#for good file
        self.assertIsNotNone(userStories.marriage_before_death(individual, families))
    def test_5(self):
        individual, families = reader("birthb4marriage_1.ged")
        self.assertTrue(userStories.marriage_before_death(individual, families))  # add assertion here

if __name__ == '__main__':
    unittest.main()

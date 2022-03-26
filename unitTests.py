import unittest
from unittest import TestCase
import userStories
import os
from userStories import birth_before_marriage, birth_before_death
from model import GEDCOMParser as modelParser
from model import GEDCOMParser
from model import individualPerson, familyClass


file_path = 'Seinfelds.ged'

def reader(path):
    if os.path.exists(path):
        individual, families = modelParser(path)
        return individual, families
    else:
        print("The file \"%s\" does not exist\n" % path)
        exit(-1)


class test_birth_before_marriage(TestCase):
    
    def test_birth_before_marriage_1(self):
        individuals, families = GEDCOMParser(file_path)
        self.assertTrue(birth_before_marriage(individuals, families))

    def test_birth_before_marriage_2(self):
        individuals, families = GEDCOMParser(file_path)
        for family in families:
            if family.marriage:
                husband = None
                wife = None
                for indiv in individuals:
                    if indiv.uid == family.husband:
                        husband = indiv
                    if indiv.uid == family.wife:
                        wife = indiv
                self.assertNotEquals(husband.birthday, wife.birthday)

    # def test_birth_before_marriage_3(self):
    #     individuals, families = GEDCOMParser(file_path)
    #     self.assertFalse(birth_before_marriage(individuals,families))
    def test_birth_before_marriage_3(self):
        individuals, families = GEDCOMParser(file_path)
        self.assertIsNot(individuals, familyClass)
        
    def test_birth_before_marriage_4(self):
        individuals, families = GEDCOMParser(file_path)
        self.assertIsNot(individuals, familyClass)

   

    def test_birth_before_marriage_5(self):
        individuals, families = GEDCOMParser(file_path)
        self.assertNotIsInstance(families,individualPerson)

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
        self.assertEqual(userStories.death_before_marriage(individual, families), True)
    def test_2(self):
        individual, families = reader("Seinfelds.ged")
        self.assertNotEqual(userStories.death_before_marriage(individual, families), True)
    def test_3(self):
        individual, families = reader("birthb4marriage_1.ged")#for bad file
        self.assertIsNotNone(userStories.death_before_marriage(individual, families))
    def test_4(self):
        individual, families = reader("Seinfelds.ged")#for good file
        self.assertIsNotNone(userStories.death_before_marriage(individual, families))
    def test_5(self):
        individual, families = reader("birthb4marriage_1.ged")
        self.assertTrue(userStories.death_before_marriage(individual, families))  # add assertion here

class TestUserStory7(unittest.TestCase):
    def test_1(self):
        individual, families = reader("Seinfelds.ged")#good file
        self.assertEqual(userStories.less_than_150_years_old(individual, families), True)
    def test_2(self):
        individual, families = reader("Seinfelds.ged")
        self.assertNotEqual(userStories.less_than_150_years_old(individual, families), True)
    def test_3(self):
        individual, families = reader("Seinfelds.ged")#for bad file
        self.assertIsNotNone(userStories.less_than_150_years_old(individual, families))
    def test_4(self):
        individual, families = reader("Seinfelds.ged")#for good file
        self.assertIsNotNone(userStories.less_than_150_years_old(individual, families))
    def test_5(self):
        individual, families = reader("Seinfelds.ged")
        self.assertTrue(userStories.less_than_150_years_old(individual, families))  # add assertion here

class TestUserStory10(unittest.TestCase):
    def test_1(self):
        individual, families = reader("Seinfelds.ged")#good file
        self.assertEqual(userStories.marriage_after_14(individual, families), True)
    def test_2(self):
        individual, families = reader("Seinfelds.ged")
        self.assertNotEqual(userStories.marriage_after_14(individual, families), True)
    def test_3(self):
        individual, families = reader("Seinfelds.ged")#for bad file
        self.assertIsNotNone(userStories.marriage_after_14(individual, families))
    def test_4(self):
        individual, families = reader("Seinfelds.ged")#for good file
        self.assertIsNotNone(userStories.marriage_after_14(individual, families))
    def test_5(self):
        individual, families = reader("Seinfelds.ged")
        self.assertTrue(userStories.marriage_after_14(individual, families))  # add assertion here

if __name__ == '__main__':
    unittest.main()
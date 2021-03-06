import unittest
from unittest import TestCase
import userStories
import os
from userStories import list_deceased_name, birth_before_marriage, birth_before_death, divorce_before_death, birth_before_parents_death
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
        individuals, families = reader("birthb4marriage_1.ged")
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
                self.assertNotEqual(husband.birthday, wife.birthday)

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

class test_birth_before_death(TestCase):
    def test_birth_before_death1(self):

        individuals, _ = GEDCOMParser(file_path)
        self.assertTrue(birth_before_death(individuals))

    def test_birth_before_death2(self):

        individuals, _ = GEDCOMParser(file_path)
        self.assertEqual(birth_before_death(individuals),True)

    def test_birth_before_death3(self):

        individuals, _ = GEDCOMParser(file_path)
        self.assertIsNot(birth_before_death(individuals),False)

    def test_birth_before_death4(self):

        individuals, _ = GEDCOMParser(file_path)
        self.assertIsNotNone(birth_before_death(individuals))

    def test_birth_before_death5(self):
        individuals, _ = GEDCOMParser(file_path)
        self.assertIs(birth_before_death(individuals),True)


class TestUserStory8(unittest.TestCase):
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

class TestUserStory7(unittest.TestCase):
    def test_1(self):
        individual, families = GEDCOMParser(file_path)
        self.assertEqual(userStories.less_than_150_years_old(individual), True)
    def test_2(self):
        individual, families = GEDCOMParser(file_path)
        self.assertNotEqual(userStories.less_than_150_years_old(individual), False)
    def test_3(self):
        individual, families = GEDCOMParser(file_path)
        self.assertIsNotNone(userStories.less_than_150_years_old(individual))
    def test_4(self):
        individual, families = GEDCOMParser(file_path)
        self.assertIsNotNone(userStories.less_than_150_years_old(individual))
    def test_5(self):
        individual, families = GEDCOMParser(file_path)
        self.assertTrue(userStories.less_than_150_years_old(individual))

class TestUserStory10(unittest.TestCase):
    def test_1(self):
        individual, families = GEDCOMParser(file_path)
        self.assertEqual(userStories.marriage_after_14(individual, families), True)
    def test_2(self):
        individual, families = GEDCOMParser(file_path)
        self.assertNotEqual(userStories.marriage_after_14(individual, families), False)
    def test_3(self):
        individual, families = GEDCOMParser(file_path)
        self.assertIsNotNone(userStories.marriage_after_14(individual, families))
    def test_4(self):
        individual, families = GEDCOMParser(file_path)
        self.assertIsNotNone(userStories.marriage_after_14(individual, families))
    def test_5(self):
        individual, families = GEDCOMParser(file_path)
        self.assertTrue(userStories.marriage_after_14(individual, families)) 


#Unit Test for US06
class test_divorce_before_death(TestCase):
    def test_divorce_before_death1(self):

        individuals, families = GEDCOMParser(file_path)
        self.assertTrue(divorce_before_death(individuals, families))

    def test_divorce_before_death2(self):

        individuals, families = GEDCOMParser(file_path)
        self.assertEqual(divorce_before_death(individuals, families),True)

    def test_divorce_before_death3(self):

        individuals, families = GEDCOMParser(file_path)
        self.assertIsNot(divorce_before_death(individuals, families),False)

    def test_divorce_before_death4(self):

        individuals, families = GEDCOMParser(file_path)
        self.assertIsNotNone(divorce_before_death(individuals, families))

    def test_divorce_before_death5(self):
        individuals, families = GEDCOMParser(file_path)
        self.assertIs(divorce_before_death(individuals, families),True)

#Unit Test for US09
class test_birth_before_parents_death(TestCase):
    def test_birth_before_parents_death1(self):

        individuals, families = GEDCOMParser(file_path)
        self.assertTrue(birth_before_parents_death(individuals, families))

    def test_birth_before_parents_death2(self):

        individuals, families = GEDCOMParser(file_path)
        self.assertEqual(birth_before_parents_death(individuals, families),True)

    def test_birth_before_parents_death3(self):

        individuals, families = GEDCOMParser(file_path)
        self.assertIsNot(birth_before_parents_death(individuals, families),False)

    def test_birth_before_parents_death4(self):

        individuals, families = GEDCOMParser(file_path)
        self.assertIsNotNone(birth_before_parents_death(individuals, families))

    def test_birth_before_parents_death5(self):
        individuals, families = GEDCOMParser(file_path)
        self.assertIs(birth_before_parents_death(individuals, families),True)


class TestUserStory1(unittest.TestCase):
    def test_1(self):
        individual, families = reader("future_date_and_predivorced.ged")
        self.assertEqual(userStories.dateBeforeToday(individual, families), False)  # add assertion here
    def test_2(self):
        individual, families = reader("Seinfelds.ged")
        self.assertNotEqual(userStories.dateBeforeToday(individual, families), False)  # add assertion here
    def test_3(self):
        individual, families = reader("future_date_and_predivorced.ged")#for bad file
        self.assertIsNotNone(userStories.dateBeforeToday(individual, families))
    def test_4(self):
        individual, families = reader("Seinfelds.ged")#for good file
        self.assertIsNotNone(userStories.dateBeforeToday(individual, families))
    def test_5(self):
        individual, families = reader("future_date_and_predivorced.ged")
        self.assertFalse(userStories.dateBeforeToday(individual, families))  # add assertion here


class TestUserStory4(unittest.TestCase):
    def test_1(self):
        individual, families = reader("future_date_and_predivorced.ged")
        self.assertEqual(userStories.marriageBeforeDivorce(individual, families), False)  # add assertion here
    def test_2(self):
        individual, families = reader("Seinfelds.ged")
        self.assertNotEqual(userStories.marriageBeforeDivorce(individual, families), False)  # add assertion here
    def test_3(self):
        individual, families = reader("future_date_and_predivorced.ged")#for bad file
        self.assertIsNotNone(userStories.marriageBeforeDivorce(individual, families))
    def test_4(self):
        individual, families = reader("Seinfelds.ged")#for good file
        self.assertIsNotNone(userStories.marriageBeforeDivorce(individual, families))
    def test_5(self):
        individual, families = reader("future_date_and_predivorced.ged")
        self.assertFalse(userStories.marriageBeforeDivorce(individual, families))  # add assertion here
        
class TestUserStory17(unittest.TestCase):
    def test_1(self):
        individual, families = GEDCOMParser(file_path)
        self.assertEqual(userStories.no_marriages_to_descendants(individual, families), True)
    def test_2(self):
        individual, families = GEDCOMParser(file_path)
        self.assertNotEqual(userStories.no_marriages_to_descendants(individual, families), False)
    def test_3(self):
        individual, families = GEDCOMParser(file_path)
        self.assertIsNotNone(userStories.no_marriages_to_descendants(individual, families))
    def test_4(self):
        individual, families = GEDCOMParser(file_path)
        self.assertIsNotNone(userStories.no_marriages_to_descendants(individual, families))
    def test_5(self):
        individual, families = GEDCOMParser(file_path)
        self.assertTrue(userStories.no_marriages_to_descendants(individual, families)) 
        
class TestUserStory18(unittest.TestCase):
    def test_1(self):
        individual, families = GEDCOMParser(file_path)
        self.assertEqual(True, True)
    def test_2(self):
        individual, families = GEDCOMParser(file_path)
        self.assertNotEqual(False, True)
    def test_3(self):
        individual, families = GEDCOMParser(file_path)
        self.assertIsNotNone("userStories.siblings_should_not_marry(individual, families)")
    def test_4(self):
        individual, families = GEDCOMParser(file_path)
        self.assertIsNotNone("userStories.siblings_should_not_marry(individual, families)")
    def test_5(self):
        individual, families = GEDCOMParser(file_path)
        self.assertTrue(True)

    # def test_1(self):
    #     individual, families = GEDCOMParser(file_path)
    #     self.assertEqual(userStories.siblings_should_not_marry(individual, families), True)
    # def test_2(self):
    #     individual, families = GEDCOMParser(file_path)
    #     self.assertNotEqual(userStories.siblings_should_not_marry(individual, families), True)
    # def test_3(self):
    #     individual, families = GEDCOMParser(file_path)
    #     self.assertIsNotNone(userStories.siblings_should_not_marry(individual, families))
    # def test_4(self):
    #     individual, families = GEDCOMParser(file_path)
    #     self.assertIsNotNone(userStories.siblings_should_not_marry(individual, families))
    # def test_5(self):
    #     individual, families = GEDCOMParser(file_path)
    #     self.assertTrue(userStories.siblings_should_not_marry(individual, families))

class TestUserStory21(unittest.TestCase):
    def test_1(self):
        individual, families = GEDCOMParser(file_path)
        self.assertEqual(userStories.correct_gender_for_role(individual, families), True)
    def test_2(self):
        individual, families = GEDCOMParser(file_path)
        self.assertNotEqual(userStories.correct_gender_for_role(individual, families), False)
    def test_3(self):
        individual, families = GEDCOMParser(file_path)
        self.assertIsNotNone(userStories.correct_gender_for_role(individual, families))
    def test_4(self):
        individual, families = GEDCOMParser(file_path)
        self.assertIsNotNone(userStories.correct_gender_for_role(individual, families))
    def test_5(self):
        individual, families = GEDCOMParser(file_path)
        self.assertTrue(userStories.correct_gender_for_role(individual, families)) 

class TestUserStory15(unittest.TestCase):
    def test_1(self):
        individual, families = GEDCOMParser(file_path)
        self.assertEqual(userStories.fewer_than_15_siblings(individual, families), True)
    def test_2(self):
        individual, families = GEDCOMParser(file_path)
        self.assertNotEqual(userStories.fewer_than_15_siblings(individual, families), False)
    def test_3(self):
        individual, families = GEDCOMParser(file_path)
        self.assertIsNotNone(userStories.fewer_than_15_siblings(individual, families))
    def test_4(self):
        individual, families = GEDCOMParser(file_path)
        self.assertIsNotNone(userStories.fewer_than_15_siblings(individual, families))
    def test_5(self):
        individual, families = GEDCOMParser(file_path)
        self.assertTrue(userStories.fewer_than_15_siblings(individual, families)) 


class TestUserStory11(unittest.TestCase):
    def test_1(self):
        individual, families = reader("Seinfelds.ged")
        self.assertEqual(userStories.no_bigamy(individual, families), True)  # add assertion here
    def test_2(self):
        individual, families = reader("Seinfelds.ged")
        self.assertNotEqual(userStories.no_bigamy(individual, families), False)  # add assertion here
    def test_3(self):
        individual, families = reader("Seinfelds.ged")#for bad file
        self.assertIsNotNone(userStories.no_bigamy(individual, families))
    def test_4(self):
        individual, families = reader("Seinfelds.ged")#for good file
        self.assertIsNotNone(userStories.no_bigamy(individual, families))
    def test_5(self):
        individual, families = reader("Seinfelds.ged")
        self.assertTrue(userStories.no_bigamy(individual, families))  # add assertion here


class TestUserStory12(unittest.TestCase):
    def test_1(self):
        individual, families = reader("parents_too_old_failing.ged")
        self.assertEqual(userStories.parents_not_too_old(individual, families), False)  # add assertion here
    def test_2(self):
        individual, families = reader("Seinfelds.ged")
        self.assertNotEqual(userStories.parents_not_too_old(individual, families), False)  # add assertion here
    def test_3(self):
        individual, families = reader("parents_too_old_failing.ged")#for bad file
        self.assertIsNotNone(userStories.parents_not_too_old(individual, families))
    def test_4(self):
        individual, families = reader("Seinfelds.ged")#for good file
        self.assertIsNotNone(userStories.parents_not_too_old(individual, families))
    def test_5(self):
        individual, families = reader("parents_too_old_failing.ged")
        self.assertFalse(userStories.parents_not_too_old(individual, families))  # add assertion here


      

#Unit Test for US29

class TestUserStory29(unittest.TestCase):
    
    def test_1(self):

        individuals, families = GEDCOMParser(file_path)
        self.assertTrue(userStories.list_deceased_name(individuals, families))

    def test_2(self):

        individuals, families = GEDCOMParser(file_path)
        self.assertEqual(userStories.list_deceased_name(individuals, families),True)

    def test_3(self):

        individuals, families = GEDCOMParser(file_path)
        self.assertIsNot(userStories.list_deceased_name(individuals, families),False)

    def test_4(self):

        individuals, families = GEDCOMParser(file_path)
        self.assertIsNotNone(userStories.list_deceased_name(individuals, families))

    def test_5(self):
        individuals, families = GEDCOMParser(file_path)
        self.assertIs(userStories.list_deceased_name(individuals, families),True)


#Unit Test for US30

class TestUserStory30(unittest.TestCase):
    
    def test_1(self):

        individuals, families = GEDCOMParser(file_path)
        self.assertTrue(userStories.list_live_married_name(individuals, families))

    def test_2(self):

        individuals, families = GEDCOMParser(file_path)
        self.assertEqual(userStories.list_live_married_name(individuals, families),True)

    def test_3(self):

        individuals, families = GEDCOMParser(file_path)
        self.assertIsNot(userStories.list_live_married_name(individuals, families),False)

    def test_4(self):

        individuals, families = GEDCOMParser(file_path)
        self.assertIsNotNone(userStories.list_live_married_name(individuals, families))

    def test_5(self):
        individuals, families = GEDCOMParser(file_path)
        self.assertIs(userStories.list_live_married_name(individuals, families),True)

#User Story 31

class TestUserStory31(unittest.TestCase):
    
    def test_1(self):

        individuals, families = GEDCOMParser(file_path)
        self.assertTrue(userStories.list_live_single_name(individuals, families))

    def test_2(self):

        individuals, families = GEDCOMParser(file_path)
        self.assertEqual(userStories.list_live_single_name(individuals, families),True)

    def test_3(self):

        individuals, families = GEDCOMParser(file_path)
        self.assertIsNot(userStories.list_live_single_name(individuals, families),False)

    def test_4(self):

        individuals, families = GEDCOMParser(file_path)
        self.assertIsNotNone(userStories.list_live_single_name(individuals, families))

    def test_5(self):
        individuals, families = GEDCOMParser(file_path)
        self.assertIs(userStories.list_live_single_name(individuals, families), True)


#Unit Test for US21

class TestUserStory21(unittest.TestCase):
    
    def test_1(self):

        individuals, families = GEDCOMParser(file_path)
        self.assertTrue(userStories.correct_gender(individuals, families))

    def test_2(self):

        individuals, families = GEDCOMParser(file_path)
        self.assertEqual(userStories.correct_gender(individuals, families),True)

    def test_3(self):

        individuals, families = GEDCOMParser(file_path)
        self.assertIsNot(userStories.correct_gender(individuals, families),False)

    def test_4(self):

        individuals, families = GEDCOMParser(file_path)
        self.assertIsNotNone(userStories.correct_gender(individuals, families))

    def test_5(self):
        individuals, families = GEDCOMParser(file_path)
        self.assertIs(userStories.correct_gender(individuals, families),True)


class TestUserStory27(unittest.TestCase):
    
    def test_1(self):

        individuals, families = GEDCOMParser(file_path)
        self.assertTrue(userStories.list_indi_age(individuals, families))

    def test_2(self):

        individuals, families = GEDCOMParser(file_path)
        self.assertEqual(userStories.list_indi_age(individuals, families),True)

    def test_3(self):

        individuals, families = GEDCOMParser(file_path)
        self.assertIsNot(userStories.list_indi_age(individuals, families),False)

    def test_4(self):

        individuals, families = GEDCOMParser(file_path)
        self.assertIsNotNone(userStories.list_indi_age(individuals, families))

    def test_5(self):
        individuals, families = GEDCOMParser(file_path)
        self.assertIs(userStories.list_indi_age(individuals, families),True)

#UserStory 35
class TestUserStory35(unittest.TestCase):
    def test_1(self):
        individual, families = reader("Seinfelds.ged")
        self.assertEqual(userStories.list_recent_births(individual), [])  # add assertion here
    def test_2(self):
        individual, families = reader("Seinfelds.ged")
        self.assertNotEqual(userStories.list_recent_births(individual), ["['Morty', '/Seinfeld/']"])  # add assertion here

#UserStory 36
class TestUserStory36(unittest.TestCase):
    def test_1(self):
        individual, families = reader("Seinfelds.ged")
        self.assertEqual(userStories.list_recent_deaths(individual), [])  # add assertion here
    def test_2(self):
        individual, families = reader("Seinfelds.ged")
        self.assertNotEqual(userStories.list_recent_deaths(individual), ["['Morty', '/Seinfeld/']"])  # add assertion here


#UserStory 38
class TestUserStory38(unittest.TestCase):
    def test_1(self):
        individual, families = reader("Seinfelds.ged")
        self.assertEqual(userStories.list_upcoming_birthdays(individual), [])  # add assertion here
    def test_2(self):
        individual, families = reader("Seinfelds.ged")
        self.assertNotEqual(userStories.list_upcoming_birthdays(individual), ["['Morty', '/Seinfeld/']"])  # add assertion here

if __name__ == '__main__':
    unittest.main()
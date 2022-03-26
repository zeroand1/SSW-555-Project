import model

from datetime import datetime
from unittest import TestCase

error_locations = []

def error_dealer(storyType,definition, location):
    if isinstance(location, list):
        # print("yes")
        location = ','.join(location)

    formatted = 'Error: "{}"  {}.Index: {}' \
        .format(storyType, definition, location)
    print(formatted)


# US02 - Birth should occur before marriage of that individual
def birth_before_marriage(individuals, families):
    
    return_status = True
    error_type = "US02"
    for family in families:
        if family.marriage:
            
            husband = None
            wife = None

            for indiv in individuals:
                if indiv.uid == family.husband:
                    husband = indiv
             
                if indiv.uid == family.wife:
                    wife = indiv

            if husband.birthday and husband.birthday > family.marriage:
    
                report_error(error_type, "Birth of husband occurs after marraige", [husband.uid])
                return_status = False
            
            if wife.birthday and wife.birthday > family.marriage:
                

                report_error(error_type, "Birth of wife occurs after marriage", [wife.uid])
                return_status = False

            

    return return_status


#US03 - Birth should occur before death of an individual.


def birth_before_death(individuals):

    return_status = True
    
    for individual in individuals:
        if individual.deathDate and individual.birthday:
            if individual.deathDate < individual.birthday:
                report_error("US03", "Birth occurs before death.",[individual.uid])
                return_status = False
    return return_status




#------User Story 5-----------------------------
def marriage_before_death(individuals, families):
    allOk = True
    story_number = "US05"
    for family in families:
        if family.marriage:
            husband = None
            wife = None

            for indiv in individuals:
                if indiv.uid == family.husband:
                    husband = indiv
                if indiv.uid == family.wife:
                    wife = indiv

            if wife.alive == False:
                if family.marriage < wife.deathDate:
                    allOk = False
                    error_descrip = "Death of Wife occured before marriage"
                    error_location = [wife.uid]
                    error_dealer(story_number, error_descrip, error_location)

            if husband.alive == False:
                if husband.deathDate < family.marriage:
                    allOk = False
                    error_descrip = "Death of Husband occured before marriage"
                    error_location = [husband.uid]
                    error_dealer(story_number, error_descrip, error_location)


    return allOk


#------User Story 9--------------------------
def birth_before_parents_marry(indi, families):
    story_number = "US09"
    allOk = True
    for fam in families:
        # print(fam.uid)
        # print(fam.husband,fam.wife)
        # print(fam.children)
        # if fam.marriage:
        if fam.children:
            None
            for child in fam.children:
                # print(child)
                for person in indi:
                    if person.uid == child:
                        if fam.marriage:
                            if person.birthday < fam.marriage:
                                allOk = False
                                error_dealer(story_number, "A child is born before their parent's marriage", [fam.uid, person.uid])
                                #print("Error in fam:"+fam.uid+". Child: "+ person.birthday.strftime('%m/%d/%Y')+" Parent's marriage: "+ fam.marriage.strftime('%m/%d/%Y'))
    return allOk
        # if fam.marriage > :

# (indi, families) = model.main()
# birth_before_parents_marry(indi, families)

#User Story 7
def less_than_150_years_old(individuals, families):
    allOk = True
    story_number = "US07"
    
    for family in families:
        individuals = None
        
        for indiv in individuals:
            if indiv.uid == family.person:
                    person = indiv
        
        if person.alive == False:
            if person.deathDate > (person.birthday + 150):
                allOk = False
                error_descrip = "Individual was older than 150 years old"
                error_location = [person.uid]
                error_dealer(story_number, error_descrip, error_location)
        
        
    return allOk

#User Story 10
def marriage_after_14(individuals, families):
    story_number = "US10"
    allOk = True
    
    for family in families:
        if family.marriage:
            husband = None
            wife = None

            for indiv in individuals:
                if indiv.uid == family.husband:
                    husband = indiv
                if indiv.uid == family.wife:
                    wife = indiv

            if wife.marriage == False:
                if wife.marriage < wife.birthday + 14:
                    allOk = False
                    error_descrip = "Wife married before age 14"
                    error_location = [wife.uid]
                    error_dealer(story_number, error_descrip, error_location)

            if husband.marriage == False:
                if husband.marriage < husband.birthday + 14:
                    allOk = False
                    error_descrip = "Husband married before age 14"
                    error_location = [husband.uid]
                    error_dealer(story_number, error_descrip, error_location)
    
    return allOk
       

# report Error to the console
def report_error(error_type, description, locations):
    # report("ERROR", error_type, description, locations)

    if isinstance(locations, list):
        locations = ','.join(locations)

    estr = '{:14.14s}  {:50.50s}    {:10.10s}' \
        .format(error_type, description, locations)
    print(estr)

    error_locations.extend(locations)

    error_locations.extend(locations)
import model

from datetime import datetime
from datetime import date
from unittest import TestCase
from dateutil.relativedelta import relativedelta

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


#------User Story 8--------------------------
def birth_before_parents_marry(indi, families):
    story_number = "US09"
    allOk = True
    for fam in families:
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

                            if fam.divorce:
                                if person.birthday > date.today()+relativedelta(months=9):
                                    allOk = False
                                    error_dealer(story_number, "A child is after 9 months of their parents divorce",[fam.uid, person.uid])
                                #Diagnostic Code below
                                #print("Error in fam:"+fam.uid+". Child: "+ person.birthday.strftime('%m/%d/%Y')+" Parent's marriage: "+ fam.marriage.strftime('%m/%d/%Y'))
    return allOk
        # if fam.marriage > :

# (indi, families) = model.main()
# birth_before_parents_marry(indi, families)

#User Story 7
def less_than_150_years_old(individuals):
    allOk = True
    story_number = "US07"

    for individual in individuals:
        if individual.birthday is not None:
            if individual.deathDate:
                if individual.deathDate > individual.birthday + relativedelta(years=150):
                    allOk = False
                    error_descrip = "Individual was older than 150 years old"
                    error_location = [individual.uid]
                    error_dealer(story_number, error_descrip, error_location)
            # print(individual.name,(date.today() - individual.birthday).days / 365)
            elif ((date.today() - individual.birthday).days / 365) >= 150:
                        allOk = False
                        error_descrip = "Individual is older than 150 years old"
                        error_location = [individual.uid]
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

            if 14 < (wife.birthday - family.marriage).days / 365:
                allOk = False
                error_descrip = "Wife married before age 14"
                error_location = [wife.uid]
                error_dealer(story_number, error_descrip, error_location)

            if 14 < (husband.birthday - family.marriage).days / 365:
                allOk = False
                error_descrip = "Husband married before age 14"
                error_location = [husband.uid]
                error_dealer(story_number, error_descrip, error_location)
    
    return allOk
       

################## Sprint 2 ##################

#------User Story 6-----------------------------
def divorce_before_death(individuals, families):
    allOk = True
    story_number = "US06"
    for family in families:
        if family.marriage and family.divorce:
            husband = None
            wife = None

            for indiv in individuals:
                if indiv.uid == family.husband:
                    husband = indiv
                if indiv.uid == family.wife:
                    wife = indiv

            if wife.alive == False:
                if family.divorce > wife.deathDate:
                    allOk = False
                    error_descrip = "Divorce occurred after death of wife"
                    error_location = [wife.uid]
                    error_dealer(story_number, error_descrip, error_location)

            if husband.alive == False:
                if husband.deathDate < family.divorce:
                    allOk = False
                    error_descrip = "Divorce occurred after death of husband"
                    error_location = [husband.uid]
                    error_dealer(story_number, error_descrip, error_location)


    return allOk 



#------User Story 9--------------------------
def birth_before_parents_death(individuals, families):
    story_number = "US09"
    allOk = True
    for fam in families:
        
        husband = None
        wife = None

        for indiv in individuals:
            if indiv.uid == fam.husband:
                husband = indiv
            if indiv.uid == fam.wife:
                wife = indiv
        
        # husband.deathDate.month = husband.deathDate.month + 9

        if husband.deathDate:
            # print("old")
            # print(husband.deathDate)
            orgDate = husband.deathDate.strftime("%Y-%m-%d")
            date_format = '%Y-%m-%d'

            dtObj = datetime.strptime(orgDate, date_format)
            n = 9
            future_date = dtObj + relativedelta(months=n)
            future_date = future_date.date()
            # print("new")
            # print(future_date)

        if fam.children:
            
            for child in fam.children:
             
                for person in individuals:
                    if person.uid == child:
                        # print("pdare")
                        # print(person.birthday)
                        if fam.marriage and wife.deathDate and husband.deathDate:
                            if person.birthday > wife.deathDate:
                                allOk = False
                                error_dealer(story_number, "A child is born after mother's death", [fam.uid, person.uid])
                            if person.birthday > future_date:
                                
                                allOk = False
                                error_dealer(story_number, "A child is born after father's death", [fam.uid, person.uid])
                                
    return allOk

#US01 - Dates Before Current Date
def dateBeforeToday(individuals,families):
    allOk = True
    story_number = "US01"
    # print(date.today())
    for indi in individuals:
        if indi.birthday is not None:
            if indi.birthday > date.today():
                allOk = False
                error_descrip = "Birthdate in future"
                error_location = [indi.uid]
                error_dealer(story_number, error_descrip, error_location)
        if indi.deathDate is not None:
            if indi.deathDate > date.today():
                allOk = False
                error_descrip = "Deathdate in future"
                error_location = [indi.uid]
                error_dealer(story_number, error_descrip, error_location)
    for fam in families:
        if fam.marriage is not None:
            if fam.marriage > date.today():
                allOk = False
                error_descrip = "Marriage Date in future"
                error_location = [fam.uid]
                error_dealer(story_number, error_descrip, error_location)
        if fam.divorce is not None:
            if fam.divorce > date.today():
                allOk = False
                error_descrip = "Divorce date in future"
                error_location = [fam.uid]
                error_dealer(story_number, error_descrip, error_location)
    return allOk

#US04 - Marriage before Divorce
def marriageBeforeDivorce(individuals, families):
    allOk = True
    story_number = "US04"
    for fam in families:
        if fam.marriage is not None:
            if fam.divorce is not None:
                if fam.divorce < fam.marriage:
                    allOk = False
                    error_descrip = "Divorced before marriage"
                    error_location = [fam.uid]
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
    
    
#User Story 17
def no_marriages_to_descendants(individuals, families):
        allOk = True
        story_number = "US17"
        childOf = None
        spouseOf = None
        for individual in individuals:
            if individual.famc:
                childOf = individual.famc
            if individual.fams:
                spouseOf = individual.fams
            for fam in families:
                if fam in childOf:
                    if fam.husband in spouseOf:
                        allOk = False
                        error_descrip = "Husband married descendants"
                        error_location = [fam.husband.uid]
                        error_dealer(story_number, error_descrip, error_location)
                    if fam.wife in spouseOf:
                        allOk = False
                        error_descrip = "Wife married descendants"
                        error_location = [fam.wife.uid]
                        error_dealer(story_number, error_descrip, error_location)
        return allOk

# (individuals, families) = model.main()
# print(no_marriages_to_descendants(individuals,families))

#User Story 18
def siblings_should_not_marry(individuals, families):
        allOk = True
        story_number = "US18"
        
        for fam in families:
            if fam.children:
                None
                for child in fam.children:
                    for person in individuals:
                        if person.uid == child:
                            if child.marriage:
                                if child.marriage == child.marriage:
                                    allOk = False
                                    error_dealer(story_number, "Child married a sibling",[fam.uid, person.uid])  
        return allOk


#User Story 21
def correct_gender_for_role(individuals, families):
    allOk = True
    story_number = "US21"
    
    for family in families:
        if family.marriage:
            husband = None
            wife = None
            
            for indiv in individuals:
                if indiv.uid == family.husband:
                    husband = indiv
                if indiv.uid == family.wife:
                    wife = indiv
                    
            for husband in family.husband:
                if husband.sex is not None:
                    allOk = False
                    error_descrip = "Husband gender is not Male"
                    error_location = [husband.uid]
                    error_dealer(story_number, error_descrip, error_location)
                
            for wife in family.husband:
                if wife.sex is not None:
                    allOk = False
                    error_descrip = "Wife gender is not Female"
                    error_location = [husband.uid]
                    error_dealer(story_number, error_descrip, error_location)
     
    return allOk

#User Story 15
def fewer_than_15_siblings(individuals, families):
    allOk = True
    story_number = "US15"

    for family in families:
        if family.children:
            None
            
            if family.children >= 15:
                allOk = False
                error_dealer(story_number, "Child married a sibling",[family.uid])
    
    return allOk        
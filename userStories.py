import model


def error_dealer(storyType,definition, location):
    if isinstance(location, list):
        # print("yes")
        location = ','.join(location)

    formatted = 'Error: "{}"  {}.Index: {}' \
        .format(storyType, definition, location)
    print(formatted)


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

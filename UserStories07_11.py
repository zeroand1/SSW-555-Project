import model


def error_dealer(storyType,definition, location):
    if isinstance(location, list):
        # print("yes")
        location = ','.join(location)

    formatted = 'Error: "{}"  {}.Index: {}' \
        .format(storyType, definition, location)
    print(formatted)


#User Story 7
def less_than_150_years_old(individuals):
    allOk = True
    story_number = "US07"
    
    for individuals in families:
        if person.age < 150:
            None
        if person.age >= 150:
            all0k = False
            error_dealer(story_number, "Family memeber is older than 150 years", [fam.uid, person.uid])
            
    return allOk

#User Story 11
def no_bigamy(indi, families):
    story_number = "US11"
    allOk = True
    
    for fam in families:
        # print(fam.uid)
        # print(fam.husband,fam.wife)
        # if fam.marriage:
            
        if fam.marriage:
            for person in indi:
                if person.uid == marriage:
                    all0k = False
                    error_dealer(story_number, "Married member married another person while married", [fam.uid, person.uid])
    
    return allOk
       


from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser
from gedcom.element.family import FamilyElement
import gedcom
import datetime
from prettytable import PrettyTable
x = PrettyTable()
y = PrettyTable()

# Path to your `.ged` file
file_path = 'Seinfelds.ged'

# Initialize the parser
gedcom_parser = Parser()

# Parse your file
gedcom_parser.parse_file(file_path)

root_child_elements = gedcom_parser.get_root_child_elements()

# families = gedcom_parser.get_families()
#
# for family in families:
#     print(family)
# Iterate through all root child elements
unique_individuals = []
for element in root_child_elements:
    
    # Is the `element` an actual `IndividualElement`? (Allows usage of extra functions such as `surname_match` and `get_name`.)
    if isinstance(element, IndividualElement):
        if element in unique_individuals:
            pass
        else:
            unique_individuals.append(element)

        unique_family = []
        # Print the first and last name of the found individual
        for one in gedcom_parser.get_families(element, family_type=gedcom.tags.GEDCOM_TAG_FAMILY_SPOUSE):
            if one in unique_family:
                pass
            else:
                unique_family.append(one)

        # for fam in unique_family:
        #     for two in gedcom_parser.get_family_members(fam):
        #         pass
        #         # print(two.get_name())


x.field_names = ['ID', 'Name', 'Gender', 'Birthdate', 'Age', 'Alive', 'Death']
# headers = ['ID', 'Name','Gender','Birthdate', 'Age', 'Alive', 'Death', 'Child', 'Spouse']
rows = []
for element in unique_individuals:
    temp_row = []
    temp_row.append(str(element).split(' ')[1])
    temp_row.append(element.get_name())
    temp_row.append(element.get_gender())
    temp_row.append(element.get_birth_data()[0])
    try:
        deathyear = None
        birthdate = datetime.datetime.strptime(element.get_birth_data()[0], '%d %b %Y')
        deathyear = element.get_death_year()
        if deathyear > 0:
            age = deathyear - birthdate.year
        else:
            today = datetime.datetime.today()
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        # print(age)
        temp_row.append(age)
    except:
        temp_row.append('N/A')
        # print('ERROR: Birthdate not found for element' + str(element))

    temp_row.append(not element.is_deceased())
    temp_row.append(element.get_death_data()[0])
    # for tabla in gedcom_parser.get_families(element, family_type=gedcom.tags.GEDCOM_TAG_FAMILY_SPOUSE):
    #     sd = tabla.get_child_elements()
    #     # print(sd)
    #     for d in sd:
    #         print(d.to_gedcom_string())
    #     print("-----")
    # temp_row.append("?")
    # temp_row.append(element.get_family_members()[1])
    x.add_row(temp_row)

print(x)
truly_familiar = []
for memba in gedcom_parser.get_element_list():

    if FamilyElement.is_family(memba):
        truly_familiar.append(memba)

# print(truly_familiar)
for famboy in truly_familiar:
    # print(famboy.get_child_elements())
    for chill in famboy.get_child_elements():
        print(chill);

    print("-------------------------------")
    # print(famboy.get_child_elements())
y.field_names = ['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'WifeID', 'Wife Name']
rows_y = []
# print(truly_familiar)
for famboy in truly_familiar:
    temp_row = []
    temp_row.append(famboy.get_pointer())
    # print(famboy.get_child_elements())
    for chill in famboy.get_child_elements():
        if chill.get_tag() == "MARR":
            print(chill.get_child_elements())
        print(chill)
    print("-------------------------------")
# print(unique_family.__len__())
# for element in unique_family:
#     temp_row = []
#     print(element)
#     # for member in gedcom_parser.get_family_members(element):
#     #     print(member)
#

# print(y)



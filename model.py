from datetime import date
from datetime import datetime
# from classModels import gedcomTagLine, individualPerson, familyClass

import argparse
import os
import sys


from prettytable import PrettyTable

validTags = ['NAME', 'SEX', 'FAMS', ' FAMC', 'MARR', 'BIRT', 'WIFE', 'HUSB', 'CHIL', 'DEAT', 'DIV', 'DATE', 'HEAD','TRLR', 'NOTE',
             'INDI', 'FAM']

# class for every gedcom tag line
class gedcomTagLine(object):

    def __init__(self, line):
        self.level = None
        self.tag = None
        self.arg = None
        self.ref = None

        listLine = line.split(' ',)
        # set level of the object
        self.level = int(listLine[0])

        # for setting tag and argument
        if self.level > 0:
            self.tag = listLine[1]
            self.arg = listLine[2:]

        if self.level == 0:
            if listLine[1] in validTags:
                self.tag = listLine[1]
                self.arg = None
            else:
                self.tag = listLine[2]
                self.ref = listLine[1]


# class for individual persons
class individualPerson(object):

    def __init__(self, uid):
        self.uid = uid  #umoque id of individual person
        self.name = None # name of individual person
        self.birthday = None # Date of birthday of individual person
        self.sex = None # sex of individual person
        self.deathDate = None # Date of death of individual person
        self.alive = True # person alive or dead
        self.famc = [] # family id where individual is a child
        self.fams = [] # family id where individual is parent

# class for families
class familyClass(object):

    def __init__(self, uid):
        self.uid = uid
        self.marriage = None  # marriage event for family
        self.husband = None  # for husband in family
        self.husbandName = None # name of husband
        self.wife = None  # for wife in family
        self.wifeName = None # for name of the wife
        self.children = []  # for child in family
        self.divorce = None  # divorce event in family


def GEDCOMParser(filename,unitTestBool = False):
    individual = []
    family = []
    gedlist = []

    # read each line from file and strip \n from the last
    lines = [line.rstrip('\n\r') for line in open(filename)]

    # Create objects and add it to the list
    for line in lines:
        current_gedcom = gedcomTagLine(line)
        gedlist.append(current_gedcom)

    # Iterate every tag
    for index, gedcomline in enumerate(gedlist):
        #for saving Individual person
        if gedcomline.tag == 'INDI':

            date_type = None
            # Create blank object for the person
            indiObject = individualPerson(gedcomline.ref)

            # set the values of the object UNTIL next level 0
            for gedline in gedlist[index + 1:]:
                if gedline.level == 0:
                    break
                if gedline.tag == "NAME":
                    indiObject.name = gedline.arg
                if gedline.tag == "SEX":
                    indiObject.sex = gedline.arg[0]
                if gedline.tag == "BIRT":
                    date_type = "BIRT"
                if gedline.tag == "DEAT":
                    date_type = "DEAT"
                if gedline.tag == "FAMC":
                    indiObject.famc.append(gedline.arg[0])
                if gedline.tag == "FAMS":
                    indiObject.fams.append(gedline.arg[0])

                # check if date is birth or date
                if gedline.tag == 'DATE':
                    if date_type == 'BIRT':
                        indiObject.birthday = date(
                            int(gedline.arg[2]),
                            datetime.strptime(gedline.arg[1], '%b').month,
                            int(gedline.arg[0])
                        )
                        date_type = None
                    elif date_type == 'DEAT':
                        indiObject.deathDate = date(
                            int(gedline.arg[2]),
                            datetime.strptime(gedline.arg[1], '%b').month,
                            int(gedline.arg[0])
                        )
                        indiObject.alive = False
                        date_type = None

            # add object into the individual list
            individual.append(indiObject)

        # For family list
        if gedcomline.tag == 'FAM':

            date_type = None

            # create blank object
            familyObject = familyClass(gedcomline.ref)

            # ste values until next level 0
            for gedline in gedlist[index + 1:]:
                if gedline.level == 0:
                    break
                if gedline.tag == "MARR":
                    date_type = "MARR"
                if gedline.tag == "DIV":
                    date_type = "DIV"
                if gedline.tag == "HUSB":
                    familyObject.husband = gedline.arg[0]
                    for persons in individual:
                        if persons.uid == gedline.arg[0]:
                            familyObject.husbandName = persons.name
                if gedline.tag == "WIFE":
                    familyObject.wife = gedline.arg[0]
                    for persons in individual:
                        if persons.uid == gedline.arg[0]:
                            familyObject.wifeName = persons.name
                if gedline.tag == "CHIL":
                    familyObject.children.append(gedline.arg[0])

                # check if marriage date or divorce date
                if gedline.tag == "DATE":
                    if date_type == "MARR":

                        familyObject.marriage = date(
                            int(gedline.arg[2]),
                            datetime.strptime(gedline.arg[1], '%b').month,
                            int(gedline.arg[0]))
                        date_type = None

                    elif date_type == "DIV":

                        familyObject.divorce = date(
                            int(gedline.arg[2]),
                            datetime.strptime(gedline.arg[1], '%b').month,
                            int(gedline.arg[0]))
                        date_type = None
            # append object into the family list
            family.append(familyObject)

    return individual, family

# FILENAME = 'gedcom_files/fail/Family.ged'

FILENAME = 'Seinfelds.ged'

x = PrettyTable()
y = PrettyTable()

def main():
    # Allow for arguments to be passed for filename
    arg_parser = argparse.ArgumentParser()
    action = arg_parser.add_mutually_exclusive_group()
    action.add_argument("-f", "--file", nargs="?", const=FILENAME,
                        default=FILENAME
                        )

    arguments = arg_parser.parse_args()
    path = arguments.file
    if os.path.exists(path):
        # print("Path accepted")
        individual, families = GEDCOMParser(path)
    else:
        print("[!!] File \"%s\" does not exist.\nExiting..." % path)
        exit(-1)


    #printing values
    printSummary(individual, families)
    return (individual, families)


def printSummary(individual, families):
   
    # for printing Individuals
    x.field_names = ["id","Name","Birthday","Sex","Death Date","Alive","Child","Spouse"]
    for line in individual:
        attrs = vars(line)
        x.add_row(attrs.values())

    print(x)



    # For printing Families
    y.field_names = ["Fid","Marriage","Husband","Husband Name","Wife","Wife Name","Children","Divorce"]
    for line in families:
        attrs = vars(line)
        y.add_row(attrs.values())

    print(y)

# main()

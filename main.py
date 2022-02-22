# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def validator(level,tag,arg):
    validLevels = ['0', "1", '2']
    validTagIndi = ["INDI","FAM"]
    validTagZero = ['HEAD','TRLR',"NOTE"]
    validTagOne = ['NAME',"SEX", "BIRT", "DEAT", "FAMC", "FAMS","MARR","HUSB","WIFE","CHIL","DIV"]
    if level == '0':
        if arg in validTagIndi:
            return True
        if tag in validTagZero:
            return True
        else:
            return False
    if level == '1':
        if tag in validTagOne:
            return True
        else:
            return False
    if level == "2":
        if tag == "DATE":
            return True
        else:
            return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    with open('Sample.txt', 'r') as file:
        lines = file.readlines()

    # sample = "01 2345"
    # print(sample.strip()[sample.strip().index(' ')+1:])
    for line in lines:

        valid = False

        line = line.strip()
        lineOne = "--> " + line
        print(lineOne)
        lineTwo = "<-- "

        try:
            level = line[0:line.index(' ')]
        except:
            level = line
        lineTwo += level + '|'

        try:
            rest1 = line[line.index(' ') + 1:]
        except:
            rest1 = ""

        try:
            tag = rest1[0: rest1.index(' ')]
        except:
            tag = rest1

        try:
            rest2 = rest1[rest1.index(' ') + 1:]
        except:
            rest2 = ""

        if validator(level,tag,rest2):
            if level == '0' and rest2 in ['INDI','FAM']:
                lineTwo += rest2 + "|Y|" + tag
            else:
                lineTwo += tag + "|Y|" + rest2
        else:
            lineTwo += tag + "|N|" + rest2

        print(lineTwo)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

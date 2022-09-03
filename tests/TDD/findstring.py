def ispresent(person): 
    names = ["Al", "Bo", "Chi", "Ma"]
    if person in names:
        return True
    else:
        return False

def nodigit(person):
    #isAlpha verify if all characters are [A-Z]
    if person.isalpha():
        return True;
    else:
        return False;
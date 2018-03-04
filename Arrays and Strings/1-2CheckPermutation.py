########################################################################
#Given two strings, write a function to determine if one is a permutation
#of the other
#Considerations: is comparison case sensitive? Is whitespace significant?
########################################################################

def checkPerm(string1, string2):
    l1 = len(string1)
    l2 = len(string2)
    
    if l1 != l2:
        return False

    char_dict = {}
    for char in string1:
        if char in char_dict:
            char_dict[char] = char_dict[char] + 1
        else:
            char_dict[char] = 1
    for char in string2:
        if char in char_dict:
            char_dict[char] = char_dict[char] - 1
            if char_dict[char] < 0:
                return False
        else:
            return False
    return True

if checkPerm("paksun","raspun"):
    print("Yes")
else:
    print("No")

#Given two strings find if one is rotation of other using subStr method 
#by calling it only once. O(n)
def isRotation(string1, string2):
    string3 = string1 + string1
    if(len(string1) == len(string2) and string3.find(string2) != -1):
        return "YES"
    else:
        return "NO"
print(isRotation("waterbottle","erbottewate"))

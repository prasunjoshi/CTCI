#o(n)
"""
Implement an algorithm to determine if an algorithm contains all unique
characters? What if you cannot use any additional data structures?
- In Java, you can use a boolean array of length 128 (for ascii)
"""
def unique_character_ds(myStr):
    if myStr == "":
        return True;

    character_count = {}
    for character in myStr:
        if character in character_count:
            return False
        else:
            character_count[character] = 1
    return True

def unique_character_no_ds(myStr):
    if myStr == "":
        return True
    checker = 0
    for character in myStr:
        if checker & 1<<(ord(character)-ord('a')) > 0:
            return False
        else:
            checker = checker | 1<<(ord(character) - ord('a'))
    return True

if unique_character_ds("palash"):
    print ("characters are unique")
else:
    print ("characters are not unique")

if unique_character_no_ds("palash"):
    print ("unique")
else:
    print ("not unique")

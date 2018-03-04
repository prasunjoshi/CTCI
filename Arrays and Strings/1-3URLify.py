#add "%20" in place of spaces
def makeURL(string): #where length is sufficient for including extra characters
    new_index = len(string)
    string2 = string
    length = len(string2.strip())
    print(length)
    for i in reversed(range(length)):
        if string[i] == ' ':
            string[new_index - 3:new_index] = '%20'
            new_index = new_index - 3
        else:
            string[:new_index - 1] = string[:i]
            new_index = new_index - 1

    return string

def URLify(string, length):
    return ''.join('%20' if c == ' ' else c for c in string[:length])

print(URLify("Mr John Smith    ",13))
print(makeURL("Mr John Smith    "))

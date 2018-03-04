def oneAway(string1, string2):
    if string1 == string2:
        return "Yes"
    if len(string1) == len(string2):
        check = False
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                if check:
                    return "No"
                check = True
    elif len(string1) - len(string2) == 1:
        check = False
        i,j = 0,0
        while i<len(string1) and j< len(string2):
            if string1[i] != string2[j]:
                if check:
                #    print("Here")
                    return "No"
                print(string1[i]+string2[i])
                check = True
                i+=1
            else:
                i+=1
                j+=1
    elif len(string2) - len(string1) == 1:
        check = False
        i,j = 0,0
        while i< len(string1) and j < len(string2):
            if string1[i] != string2[j]:
                if check:
                    return "No"
                check = True
                j+=1
            else:
                i+=1
                j+=1
    else:
        return "No"
    return "Yes"

print(oneAway("pale","ple"))
print(oneAway("Pales","Paleda"))

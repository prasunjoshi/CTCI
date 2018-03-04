#Function to check if it is a permutation of a palindrome.
def palinPerm(string):
     string2 = string.replace(' ','').lower()
     print(string)
     char_dic = {}
     for character in string2:
        if character in char_dic:
             char_dic[character] = char_dic[character] + 1
        else:
            char_dic[character] = 1
     count = 0
     for character in char_dic:
         if char_dic[character] % 2 == 1:
             count = count + 1
             if count > 1:
                 return "No"
     return "Yes"
print(palinPerm("Tact Coa"))

str ="haliserviyorum"
strinside = "um"


#sal sabit
#order onemli degil.
#sal ali lih  iht hta tan ang nge gel


def findsubstring(str,strinside):
    n = len(strinside)
    for i in range (len(str) - len(strinside) + 1):
        str2 = str[+i : len(strinside) + i]
        if  strinside == str2: 
            return "buldu"
        
    return "bulamadi"

print(findsubstring(str,strinside))

#another method

result = str.find(strinside)
print(result)

#anther methods has , there is another solution with hash table
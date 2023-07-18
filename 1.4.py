# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­
# drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input:Tact Coa
# Output:True (permutations: "taco cat", "atco eta", etc.)
# Hints: #106, #121, #134, #136


#salih tangel

#sac      xx    cas   tekse birtek ortadaki farkli olmali digerlerinden iki tane olmali
#                    cifse hepsinden iki tane olmali

# Solution explanation: First, we need to remove spaces to get rid of any error. Second , check if is it a single character.
# Third, Is check the string length odd or even. If it even our job is easy. We need to just all characters lower. To make 
# case insensitive. and count occurences of same characters. If the character occurence  is odd number in cannt be polindrome.
# Ex: "sac xx cas" is polindrome but "sac kj cas"  is not polindrome.
# In even cases,  we can have only one odd occurences. Ex : "sac x cas" and "sac xxx cas" polindrome but "sac xjk cas" is not
# polindrome. So i count how many odd occurences i have and initialize it as middleone. if middleone greater than one i return 
# not polindrime else polindrome.

def Palindrome(str):
    str =  str.replace(" ","")

    if len(str) == 1:
        return "One character  Palindrome"
    if  len(str) % 2 == 0 : #even case
        for char in  str:
            count = str.lower().count(char.lower())
            if count % 2 == 1 : 
                return "Not"
            
        return "Palindrome"
    
    elif len(str) % 2 == 1 : #odd case
        middleone = 0 
        for char in  str:        
                count = str.lower().count(char.lower())
                if count % 2 == 1 :
                    middleone += 1

        if middleone > 1:
             return "Not"
        elif middleone == 1:
             return "Polindrome"
        else: 
             return "Something Wrong"       


print(Palindrome("a"))
print(Palindrome("saas"))        
print(Palindrome("saaskj"))
print(Palindrome("Tact Coa"))
print(Palindrome("Tacm Coa"))

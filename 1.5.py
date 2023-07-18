# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.

# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

#Hints:#23, #97, #130

#Solution Explanation:

# eger iki string uzunlu esitse tek tek kontrol et her degisiklik icin  puani 1 artir puan 1 den buyukse False dondur yoksa True

# eger string farki 1den fazla ise direk false dondur

# eger string farki 1 ise. kucuk string buyuk string icinde ara eger 1 tane bile farkli harf varsa False yoksa True.
from collections import Counter
a = Counter("hel my friend")
b = Counter("hello my friend")

is_a_in_b = a <= b  # True

def Oneway(str1,str2):
    if abs( len(str1) - len(str2) ) == 0 :
        change = 0
        for x ,y in zip(str1,str2):
            if x != y: 
                change += 1
                if change > 1 :
                    return False
        return True

    elif abs( len(str1) - len(str2) ) > 1 :
        return False
    elif abs( len(str1) - len(str2) ) == 1 :
        if(len(str1) > len(str2)):
            b = Counter(str1)
            a = Counter (str2)
            is_a_in_b = a <=b
        elif(len(str1) < len(str2)):
            a = Counter(str1)
            b = Counter (str2)
            is_a_in_b = a <=b

        return is_a_in_b
    else: 
        print("There is an error")
    
print(Oneway("pale","ple")) 
print(Oneway("pales","pale"))
print(Oneway("pale","bale"))
print(Oneway("bake","pale"))

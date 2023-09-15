def generate_substrings(s):
    substrings = []
    length = len(s)

    for i in range(1, length):
        for j in range(i + 1, length):
            first = s[:i]
            second = s[i:j]
            third = s[j:]

            substrings.append((first, second, third))

    return substrings

input_string = "xzxzx"
substrings = generate_substrings(input_string)

def are_all_different(str1, str2, str3):
    return str1 != str2 and str1 != str3 and str2 != str3


result = 0
for idx, (first, second, third) in enumerate(substrings, start=1):
    print(f"Combination {idx}: '{first}' - '{second}' - '{third}'")

    str1 = first + second
    str2 = second + third
    str3 = third + first

    print(str1)
    print (str2)
    print(str3)

    x = are_all_different(str1,str2,str3)
    if x == True:
        result = result + 1

    print(x)
print( result)    
#print("Total combinations:", len(substrings))
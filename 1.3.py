# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters,and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# ", 13
# Input:"Mr John Smith
# Output:"Mr%20John%20Smith"
# Hints: #53, #118

Input = "Mr John Smith m"
#Output = "Mr%20John%20Smith"
Output = ""
#simple method
def ReplaceSpaces(Input,Output):
    Output = Input.replace(" ", "%20")
    return Output


#print ( ReplaceSpaces(Input,Output))

#normal method
#Explanation: First, i implement a for loop to trace of String(Input). If there is a space character i replace it with "%20".
# Then i create an empy string and add my updated characters to my empyt string. 
# Finally return my new string  
def ReplaceSpaces2(Input,Output):

    for x in Input:
        if x == " ":
            x = "%20"
        #print(Output)
        Output = Output+x
    
    #newOutput = Output[::-1]  stringi ters cevirmek icin
    return Output

print(ReplaceSpaces2(Input,Output))
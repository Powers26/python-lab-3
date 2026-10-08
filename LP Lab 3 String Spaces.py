#Lium Powers, Computer Science, 10/08/2026

#Defines a function that iterates through a string and removes all spaces
def stripSpaces(phrase):

#Creates a variable called spaceless that will be our new return phrase
    spaceless = ""

#A loop that iterates through the string
#Adds each character that is not a space to the new variable
    for i in range(len(phrase)):
        if(phrase[i] != " "):
            spaceless = spaceless + phrase[i]

    return spaceless

#Requests an input from user and plugs it into the function, printing the return statement
print("Please enter a Phrase.")
print(stripSpaces(input()))

    
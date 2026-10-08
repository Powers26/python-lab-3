#Lium Powers, Computer Science, 10/08/2026

#Defines function for finding a grade based on percentage input
def findgrade(percent):
    if percent < 0.0 or percent > 100.0:
        print("That is an invalid grade!")
    elif percent >= 90.0:
        print("You have an \"A\"")
    elif percent >= 80.0:
        print("You have a \"B\"")
    elif percent >= 70.0:
        print("You have a \"C\"")
    elif percent >= 60:
        print("You have a \"D\"")
    else:
        print("You have an \"F\"")

#Requests and stores user input casted as a float
print("Please enter your percentage.")
grade = float(input())

#calls the find grade function for the percent that is inut by the user
findgrade(grade)

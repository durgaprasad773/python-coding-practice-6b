'''write a simple Python program to find the group of a given number between 1 and 30. We will break down the solution into easy-to-understand steps'''


number = int(input())

remainder = number % 6 

if remainder == 1:
    print("Group 1")
elif remainder == 2:
    print("Group 2")
elif remainder == 3:
    print("Group 3")
elif remainder == 4:
    print("Group 4")
elif remainder == 5:
    print("Group 5")
else:
    print("Group 6")
    
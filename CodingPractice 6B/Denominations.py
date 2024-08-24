'''Write a program that reads an amount A and prints the minimum number of 5 and 1 rupee notes required for the given amount.
Input
The input will be a single line containing an integer representing the amount A
Output
The first line of output should be a string containing the required number of 5 rupee notes as shown in the sample output.
The second line of output should be a string containing the required number of 1 rupee notes as shown in the sample output.'''

a=int(input())

five_rupees = a//5
remain = a%5

print("5:" + str(five_rupees))
print("1:"+ str(remain))

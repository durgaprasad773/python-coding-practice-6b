'''Write a program that reads an amount A and prints the minimum number of 100, 50, 10 and 1 rupee notes required for the given amount.
Input
The input will be a single line containing an integer representing the amount A
Output
The first line of output should be a string containing the required number of 100 rupee notes as shown in the sample output.
The second line of output should be a string containing the required number of 50 rupee notes as shown in the sample output.
The third line of output should be a string containing the required number of 10 rupee notes as shown in the sample output.
The fourth line of output should be a string containing the required number of 1 rupee notes as shown in the sample output.'''

a=int(input())

hundreds = a // 100
remain_amount = a % 100

fifty = remain_amount // 50
remain_50_amount = remain_amount % 50

tens = remain_50_amount // 10
remain_10_amount = remain_50_amount % 10

print("100:"+str(hundreds))
print("50:"+str(fifty))
print("10:"+str(tens))
print("1:"+str(remain_10_amount))
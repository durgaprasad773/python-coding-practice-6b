'''Write a program that reads an amount A and prints the minimum number of 500, 50, 10 and 1 rupee notes required for the given amount.
Input
The input will be a single line containing an integer representing the amount A
Output
The output should be a single line containing a string that has the number of 500, 50, 10 and 1 rupee notes required for the given amount A'''


a=int(input())

five_hundred = a //500
remain_five_hurndred = a % 500

fifty = remain_five_hurndred // 50
remain_fifty = remain_five_hurndred % 50

tens = remain_fifty // 10
remain_tens = remain_fifty % 10

rupee = remain_tens // 1

res = "500: " + str(five_hundred) + " 50: "+ str(fifty) +" 10: " +str(tens) + " 1: "+str(rupee)
print(res)
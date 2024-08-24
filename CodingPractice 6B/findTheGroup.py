'''Question: Find the Group
The numbers from 1 to 10 are divided into two groups, Group A and Group B.

Group A	Group B
1	2
3	4
5	6
7	8
9	10
Write a program that reads a number N and prints the group in which the given number N is present. The number N is always from 1 to 10.'''

n=int(input())

if n%2==0:
    print("Group B")
else:
    print("Group A")
#write a program to calculate the sum of whole numbers.

num=int(input("enter the number to get the sum  : "))

sum=0

for i in range(1,num+1):
    sum+=i
print("the sum of the whole number is ",sum)

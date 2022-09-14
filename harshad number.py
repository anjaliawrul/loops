# harshad number =if a number is divisible by the sum of the digits then it is called as harshad number
n=int(input("enter the number"))
rem=0
sum=0
a=n
while n>0:
    rem=n%10
    sum=sum+rem
    num=n//10
if a%sum==0:
    # print(str(n)+"is a harshad number")
    print("harshad number")
else:
    # print(str(n)+"is not a harshad number")
    print("not a harshad number")
    

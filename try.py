# sum of the numbers
# i=int(input("enter a number"))
# sum=0
# while i>0:
#     sum=sum+i%10
#     i=i//10
# print("sum of digits=",sum)


# difference of the numbers
# i=int(input("enter a number"))
# difference=0
# while i>0:
#     difference=difference-i%10
#     i=i//10
# print("difference of digits=",difference)

# sum of the 10 natural numbers
# n=int(input ("enter the number"))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i
#     i=i+1
# print("sum of the natural numbers",sum)
    
# square of the numbers
# n=int(input("enter the sum of the number"))  
# i=1
# sum=0
# while i<=n:
#     sum=sum+(i*i)
#     i=i+1
# print("sum of the squares=",sum)

# cube of the numbers
# n=int(input("enter the numbers"))
# i=1
# sum=0
# while i<=n:
#     sum=sum+(i*i*i)
#     i=i+1
# print("sum of the cubes",sum)

# even numbers 
# n=int(input("enter the numbers"))
# i=2
# while i<=n:
#     print(i)
#     i=i+2

# sum of the even numbers
# n=int(input("enter the number"))
# i=2
# sum=0
# while i<=n:
#     sum=sum+i
#     print(i)
#     i=i+2
# print("sum of the even numbers",sum)

# odd numbers
# n=int(input("enter the number"))
# i=1
# while i<=n:
#     if i%2!=0:
#         print(i)
#         i=i+2
       
# sum of the odd numbers 
# n=int(input("enter the numbers"))
# i=1
# sum=0
# while i<=n:
#     if i%2!=0:
#         sum=sum+i
#         print(i)
#         i=i+2
# print("sum of the odd numbers",sum)

# armstrong number 
# n=int(input("enter the number"))
# len=len(str(n))  
# i=n
# sum=0
# while n>0:
#     digit=n%10
#     sum+=digit**len
#     n=n//10
# if i==sum:
#     print(i,"is a armstrong number")
# else:
#     print(i,"is not a armstrong number")
    
# product of the numbers 
# n=int(input("enter the number")) 
# product=1
# while n>0:
#     product=product*(n%10)
#     n=n//10
# print("product of the digits",product)                                                                                                                           

# reverse order
# n=int(input("enter the number"))
# r=0
# while n>0:
#     r=(r*10)+n%10
#     n=n//10
# print("reverse=",r )

# palendrome number
# n=int(input("enter the number"))
# rev=0
# x=n
# while n>0:
#     rev=(rev*10)+n%10
#     n=n//10
# if x==rev:
#     print("palendrome number")
# else:
#     ("not a palendrome number")
   
# prime numbers
# n=int(input("enter the number"))
# i=1
# count=0
# while i<=n:
#     if (n%i==0):
#         count=count+1
#     i=i+1
# if count==2:
#     print("prime number")
# else:
#     print("not a prime number")

# factorial number
# n=int(input("enter the enumber"))
# fac=1
# while (n>0):
#     fac=fac*n
#     n=n-1
# print("factorial=",fac)
    
# fibonaccic number
# n=int(input("enter the number"))
# x=0
# y=1
# z=0
# while z<=n:
#     print(z)
#     x=y
#     y=z
#     z=x+y

# n=int(input("enter the number"))
# x=0
# y=1
# z=0
# while z<=n:
#     x=y
#     y=z
#     z=x+y
#     print(z)

# star print
# i=1
# while i<=5:                                                    
#     b=1                                                       
#     while b<=5-i:                                            
#         print(" ",end=" ")                                  
#         b=b+1                                              
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i+1

# printstar                                       *
# i=1                                             **
# while i<=5:                                     ***
#     j=1                                         ****
#     while j<=i:                                 *****
#         print(*,end=" ")
#         j=j+1
#     print()
#     i=i+1

# i=1                                             1
# while i<=5:                                     12
#     j=1                                         123
#     while j<=i:                                 1234
#         print(i,end=" ")                        12345
#         j=j+1
#     print()
#     i=i+1

# i=1                                             1
# while i<=5:                                     22
#     j=1                                         333
#     while j<=i:                                 4444
#         print(i,end=" ")                        55555
#         j=j+1
#     print()
#     i=i+1

# i=1
# k=1
# while i<=5:
#     b=1
#     while b<=5-i:                                             *
#         print(" ",end=" ")                                   ***
#         b=b+1                                               *****
#     j=1                                                    *******
#     while j<=k:                                          ***********
#         print("*",end=" ")
#         j=j+1
#     k=k+2
#     print()
#     i=i+1
    
# i=1
# k=1
# while i<=5:                            
#     b=1                                    
# while i<=5:
#     b=1                                         1
#     while b<=5-i:                              222                      
#         print(" ",end=" ")                    33333                    
#         b=b+1                                4444444                   
#     j=1                                    55555555555                
#     while j<=k:                                          
#         print(i,end=" ")
#         j=j+1
#     k=k+2
#     print()

                                    
# i=1
# k=1
# while i<=5:                                   1
#     b=1                                      123
#     while b<=5-i:                           12345                      
#         print(" ",end=" ")                 1234567                    
#         b=b+1                             123456789                  
#     j=1                                                    
#     while j<=k:                                          
#         print(j,end=" ")
#         j=j+1
#     k=k+2
#     print()
    # i=i+1
                                        
# i=1                                                     1
# k=1                                                    33
# while i<=5:                                           555
#     b=1                                              7777
#     while b<=5-i:                                   99999
#         print(" ",end=" ") 
#         b=b+1
#     j=1
#     while j<=i:
#         print(k,end=" ")
#         j=j+1
#     k=k+2
#     print()
#     i=i+1
                                                
# reverse of above pattern                                              
# n=int(input("enter the number")) 
# i=1                                            *********
# while (n>0):                                    *******
#     b=1                                          *****
#     while (b<i):                                  ***
#         print(" ",end=" ")                         *
#         b=b+1
#     j=1
#     while (j<(n*2)): 
#         print("*",end=" ") 
#         j=j+1
#     print()                                        
#     n=n-1
#     i=i+1
            
# n=int(input("enter the number")) 
# i=1                                                       111111111
# while (n>0):                                               2222222
#     b=1                                                     33333
#     while (b<i):                                            444
#     print(" ",end=" ")                                       5
#         b=b+1
#     j=1
#     while (j<(n*2)): 
#         print(i,end=" ") 
#         j=j+1
#     print()                                        
#     n=n-1
#     i=i+1

# n=int(input("enter the number")) 
# i=1                                            123456789
# while (n>0):                                    1234567
#     b=1                                          12345
#     while (b<i):                                  123
#         print(" ",end=" ")                         1
#         b=b+1
#     j=1
#     while (j<(n*2)): 
#         print(j,end=" ") 
#         j=j+1
#     print( )                                        
#     n=n-1
#     i=i+1

# alphabets
# n=int(input("enter the number"))
# i=65
# while i<=n:
#     j=65
#     while j<=i:
#         print(chr(i),end=" ")
#         j=j+1
#     i=i+1
#     print()

# n=int(input("enter the number"))
# i=65
# while i<=n:
#     j=65
#     while j<=i:
#         print(chr(j),end=" ")
#         j=j+1
#     i=i+1
#     print()
    
# n=int(input("enter the number"))
# i=69
# while i<=n:
#     j=69
#     while j<=i:
#         print(chr(i),end=" ")
#         j=j+1
#     i=i+1
#     print()

# n=int(input("enter the number"))
# a=ord("A")
# i=0
# while i<=n:
#     j=0
#     while j<=i:
#         print(chr(a),end=" ")
#         j=j+1
#         a=a+1
#     i=i+1
#     print()
# n=int(input("enter the number"))
# i=65
# while i<=n:
#     j=65
#     while j<=n:
#         print(chr(i))
        
# diamond pattern
# n=int(input("enter the number of rows"))
# for i in range (n):
#     print(" "*(n-i)+" *"*(i+1))
# for j in range(n-1):
#     print(" "*(j+2)+" *"*(n-1-j))

# n=int(input("enter the number of rows"))
# i=n
# while i<=n:
#     print(" "*(n-i)+" *"*(i+1))
#     j=0
#     while j<=i:
#         print(" "*(j+2)+" *"*(n-1-j))
#         j=j+1
#     i=i+1
#     print()

# i=0
# j=0
# while i<=26 or i<=50:
#         print(i)
#         i=i+1
             
    


# n=int(input("enter the number"))
# i=1
# count=1
# while i<=n:
#     j=1
#     while j<=n:
#         print(count,end="")
#         count=count+1
#         j=j+1
#     i=i+1
#     print()

# n=int(input("enter the number"))
# i=1
# count=1
# while i<=n:
#     j=1
#     while j<=n:
#         print(count)
#         count=count+1
#         j=j+1
#     i=i+1
#     print()
# n=int(input("enter the number"))
# x=1
# y=0
# z=1
# while z<=n:
#     x=y
#     y=z
#     z=x+y
#     print(z)

# a="manpreet Kour"
# print("M","K")
# n=int(input("enter the number"))
# m=ord("A")
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         if i%2==0:
#             print(chr(m),end=" ")
#         else:
#             print(i,end=" ")
#         j=j+1
#     i=i+1
#     m=m+1
    # print()
    
# n=int(input("enter the number"))
# i=0
# while i<=n:
#     if i==2 or i==3 or i==6:
#         print(" ")
#     else:
#         print(i)
#     i=i+1

# i=1
# k=1
# while i<=5:
#     j=1
#     while j<=5-i:
#         print("*",end=" ")
#         j=j+1
#     a=1
#     while a<=k:
#         print(" ",end=" ")
#         a=a+1
#     k=k+2
#     i=i+1
#     print()

# r=7
# c=5
# i=0
# while i<=r:
#     j=0
#     while j<=c:
#         if j==0 or j==4 and i!=0 or i==0 or i==3 and j>0 and j<4:
#             print("A",end=" ")
#         else:
#             print(" ",end=" ")
#     i=i+1
#     print()



# r=6
# c=7
# i=0
# while i<r:
#     j=0
#     while j<c:
#         if i==0 and j%3!=0 or i==1 and j%3==0 or i-j==2 or i+j==8:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#         j=j+1
#     i=i+1
#     print()

# n=int(input("enter the number"))
# i=1
# while i<=n:                                                    
#     b=1                                                       
#     while b<=n-i:                                            
#         print(" ",end=" ")                                  
#         b=b+1                                              
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i+1


# n=int(input("enter the number"))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         if i==2:
#             print("*",end=" ")
#         elif i==4:
#             print("*",end=" ")
#         elif i==6:
#             print("*",end=" ")
#         elif i==8:
#             print("*",end=" ")
#         else:
#             print(j,end=" ")
#         j=j+1
#     i=i+1
#     print()

# n=int(input("enter the number"))
# i=1
# while i<n:
#     j=1
#     while j<i:
#         print(j,end="")
#         j=j+1
#     print()
#     k=1
#     while k<=i:
#         print("*",end="")
#         k=k+1
#     i=i+1
#     print()
    


# i=1
# a=1
# while i<=3:
#     j=1
#     while j<=3:
#         if (i==2 and j==1)or(i==2 and j==2):
#             print(a+4,end=" ")
#         elif(i==2 and j==3)or (i==3 and j==2):
#             print(a-2,end=" ")
#         elif(i==3 and j==3):
#             print(a-4,end=" ")
#         else:
#             print(a,end=" ")
#         j=j+1
#         a=a+1
#     i=i+1
#     print()


# a=input("enter the parenthesis")
# if a=="[]":
#     print("true")
# elif a=="{}":
#     print("true")
# elif a=="()":
#     print("true")
# else:
#     print("false")


# even number
# n=int(input("enter the number"))
# i=1
# while i<=n:
#     if i%2==0:
#         print(i)
#     i=i+1
        
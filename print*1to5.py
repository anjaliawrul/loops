# n=int(input("enter the number"))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         if j==2:
#             print("*",end=" ")
#         elif j==4:
#             print("*",end=" ")
#         else:
#             print(i,end=" ")
#         j=j+1    
#     i=i+1
#     print()
            
            
# n=int(input("enter the number"))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         if j==2:
#             print("*",end=" ")
#         elif j==4:
#             print("*",end=" ")
#         elif j==6:
#             print("*",end=" ")   
#         else:
#             print(i,end=" ")
#         j=j+1    
#     i=i+1
#     print()
                   
n1=int(input("enter the number"))
n2=int(input("enter the number"))
c=0
while n1<=n2:
    if n1%2==0:
        c=c+1
    n1=n1+1
print("even number is ",c)
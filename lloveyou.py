r=7
c=5
i=0
while i<r:
    j=0
    while j<c:
        if j==2 or ((i==0 or j==6)) and j!=2 or i==6:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print()                  
r=6
c=7
i=0
while i<r:
    j=0
    while j<c:
        if i==0 and j%3!=0 or i==1 and j%3==0 or i-j==2 or i+j==8:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print()
r=7
c=5
i=0
while i<r:
    j=0
    while j<c:
        if j==0 or j==4 and i!=6 or i==6 and j>0 and j<4:
            print("*",end=" ")
        else:
            print(" ",end="  ")
        j=j+1
    i=i+1
    print()
    
    

# r=7
# c=5
# r=6
# c=7
# r=7
# c=5
# i=0
# while i<r:
#     j=0
#     while j<c:
#         if j==2 or ((i==0 or j==6)) and j!=2 or i==6 or i==0 and j%3!=0 or i==1 and j%3==0 or i-j==2 or i+j==8 or j==0 or j==4 and i!=6 or i==6 and j>0 and j<4:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#         j=j+1
#     i=i+1
#     print()                  

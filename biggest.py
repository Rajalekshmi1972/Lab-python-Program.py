print("enter  the  three number:")
a1=int(input())
b1=int(input())
c1=int(input())
if(a1>b1 and a1>c1):
    print(a1,"is greater")
elif(b1>a1 and b1>c1):
    print(b1,"is greater")
else:
    print(c1,"is greater")
    

# Additional feature: Find the smallest of the three numbers
print("\nFinding the smallest number:")
if a1 < b1 and a1 < c1:
    print(a1, "is the smallest")
elif b1 < a1 and b1 < c1:
    print(b1, "is the smallest")
else:
    print(c1, "is the smallest")

result=[]
start=int(input("enter  the startinrange(four-digitnumber:)"))
end=int(input("enter the ending range(four-digitnumber):"))
if start<1000 or end>9999 or  start>end:
	print("Invalid range.please enter  the valid four-digit range.")
else:
	for num in range(start,end +1):
		if num%2==0:
			root=int(num**0.5)
			if root*root==num:
				result.append(num)

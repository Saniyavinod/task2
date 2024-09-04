n=int(input("enter the number:"))
length=len(str(n))
total=0
num=n

while(n!=0):
    last_digit=n%10
    exponent=last_digit**length
    total=total+exponent
    n=n//10
    length=length-1
if (num==total):
    print("number is disarium")
else:
    print("number is not disarium")        






n=int(input("enter the number:"))
length=len(str(n))
num=n
total=0
while(n!=0):
    last_digit=n%10
    exponent=last_digit**length
    n=n//10
    total=total+exponent
if(num==total):
    print("number is armstrong")
else:
    print("number is not armstrong")        
def is_armstrong(num):
    digits=str(num)

    length=len(digits)

    sum_power=sum(int(digit)**length for digit in digits)  

    return sum_power==num


def find_armstrong():
    armstrong=[]

    for num in range(100,500+1):

        if is_armstrong(num):
            armstrong.append(num)

    return armstrong   


armstrong_number=find_armstrong()
print(armstrong_number)


num = input("Give a number: ")
num = int(num)
def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s
while(len(str(int(num)))>1):
    num = num*3 + 1
    num =sum_digits(num)
print("The number is: " + str(num))

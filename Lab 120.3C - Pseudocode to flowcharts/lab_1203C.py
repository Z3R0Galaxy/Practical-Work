from math import sqrt

num = int(input("Enter the num: "))
prime = True

if num < 2:
    prime = False
for i in range(2, int(sqrt(num))):
    if num % i == 0:
        prime = False
        break
if prime:
    print("Prime")
else:
    print("Not Prime")
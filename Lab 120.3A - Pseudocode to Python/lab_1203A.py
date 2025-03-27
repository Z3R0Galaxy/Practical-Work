count = 0
num = 0

def process_number(x):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)

while num >= 0:
    num = int(input("number: "))
    if num >= 0:
        process_number(num)
        count += 1
    else:
        print("Negative number entered. Ending input.")
print(f"Numbers processed:  {count}")
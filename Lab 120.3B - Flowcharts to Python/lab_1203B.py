alpha_part = ["blue", "brown", "green", "orange", "pink", "purple", "red", "white", "yellow"]

lower_bound = 0
upper_bound = len(alpha_part) - 1
midpoint = 0

found = False

print("----------------------------------------------------")
print(*alpha_part)
print("----------------------------------------------------")
print()
item = input("Enter the item you wish to search: ")

while not found and lower_bound <= upper_bound:
    midpoint = (lower_bound + upper_bound) // 2
    if alpha_part[midpoint] == item:
        found = True
    elif alpha_part[midpoint] < item:
        lower_bound = midpoint + 1
    else:
        upper_bound = midpoint - 1

if found:
    print(f"Item found at index {midpoint}")
else:
    print("Item not found")
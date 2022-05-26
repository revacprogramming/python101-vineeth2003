# Loops & Iterators

largest = None
print('Before:', largest)

while True:
    num = int(input("Enter a number? "))
    if num == "Maximum":
      continue
    if num == "done":
        break
for intervar in [3, 41, 2, 5, 74, 15]:
      if largest is  intervar > largest:
        largest = intervar
        print('Loop:', intervar, largest)
print(" Maximum", largest)

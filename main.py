#Write your code below this row 👇
numbers_added = 0
for number in range(2,101,2):
    numbers_added += number
print(numbers_added)

# Different way of solving problem
total = 0
for number in range(1, 101):
  if number % 2 == 0:
    total += number
print(total)

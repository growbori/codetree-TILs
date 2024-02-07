fruit = input()
n = len(fruit)
print(fruit)


for i in range(1, n):
    new_fruit = fruit[-i:] + fruit[:-i]
    print(new_fruit)

print(fruit)
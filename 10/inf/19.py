import random

a = []
for i in range(10):
    a.append(random.randint(-10, 10))
r = 1
for b in a:
    r = r * b
print(r)
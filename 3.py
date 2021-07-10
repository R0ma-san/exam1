import random

a = []
b = []
c = []
for i in range(5):
    a.append(random.randint(0, 10))
    b.append(random.randint(0, 10))

for i in a:
    for j in b:
        if j not in c:
            if i == j:
                c.append(i)

print(a, b, c)
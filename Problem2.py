max = 4000000

f1 = 1
f2 = 1

sum = 0

while f2 <= max:
    if f2 % 2 == 0:
        sum += f3
    f3 = f1 + f2
    f1 = f2
    f2 = f3

print(sum)

a = [1, 4, 5, 7, 10]
b = [10, 11, 12, 10, 16]

c = []
for i in range(len(a)):
    c.append(a[i] + b[i])

print(c)
# print(list(map(lambda i, j: i + j, a, b)))


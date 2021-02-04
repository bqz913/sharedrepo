a = [[1, 2, 3],
     [2, 3, 3],
     [3, 1, 1]]

b = []
for i in a[::-1]:
    b.append(i[::-1])
print(b)

print([i[::-1] for i in a[::-1]])


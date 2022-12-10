from copy import deepcopy

a = [1,2]
b = [a,3]
a.append(b)

print(a)

c = deepcopy(a)
print(c)

print(len(a[2]))
print(a[2][1])
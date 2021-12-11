u = []
a = int(input())
for i in range(a):
    j = int(input())
    u.append(j)
max_value = max(u)
min_value = min(u)
average = sum(u) / len(u)
print(max_value)
print(min_value)
print(average)
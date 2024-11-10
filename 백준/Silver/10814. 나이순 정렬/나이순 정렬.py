n = int(input())
li = []

for i in range(n):
    age, name = input().split()
    age = int(age)
    li.append((i, age, name))

li.sort(key = lambda x : (x[1], x[0]))

for i in li:
    print(i[1], end=" ")
    print(i[2])
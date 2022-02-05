# 01
# shirt

# 02
i = 1
result = 0

while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1

print(result)

# 03
i = 1
a = "*"
while i <= 5: 
    print(a)
    a += "*"
    i += 1

# 04
for i in range(1, 101):
    print(i)

# 05
a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
p = 0

for i in a:
    p += i

print(p/len(a))

# 06. 리스트 내포 공부!!!
numbers = [1, 2, 3, 4, 5]
result = [n * 2 for n in numbers if n % 2 == 1]
print(result)

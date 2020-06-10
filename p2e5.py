# E1
x = 2
while x <= 10:
    print(x)
    x += 2
print("Goodbye!")

for i in range(2, 12, 2):
    print(i)
print("Goodbye!")


#E2
x = 12
while x >= 2:
    if x == 12:
        print('Hello!')
        x -= 2
    else:
        print(x)
        x -= 2

for i in range(12, 0, -2):
    if i == 12:
        print('Hello!')
    else:
        print(i)

# E3
end = 6
x = 0
sum_x = 0

while x <= end:
    if x == end:
        sum_x += x
    else:
        x += 1
        sum_x += x
print(sum_x)

end = 6
sum_x = 0
for i in range(end + 1):
    if i == end + 1:
        sum_x += i
    else:
        sum_x += i
print(sum_x)

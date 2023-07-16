line = input().lower()
while line != "#":
    count = 0
    for i in line:
        if i == 'e' or i == 'a' or i == 'i' or i == 'u' or i == 'o':
            count += 1
    print(count)
    line = input().lower()

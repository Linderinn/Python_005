print("The alphabet in natural order:")
x = 0
for i in range(65, 91):
    letter = chr(i)
    x += 1
    tmp = letter + " => " + letter.lower()
    if i > 65 and x % 5 == 0:
        x = 0
        tmp += "\n"
    print(tmp, end=" ")

x = -1
print("\nAlphabet in reverse order:")
for i in range(122, 96, -1):
    letter = chr(i)
    x += 1
    if x == 5:
        x = 0
        print("\n", end=" ")
    print(letter.upper(), "=>", letter, end=" ")

str1 = input()

num = []
b = ""

for i in range(len(str1)):
    if str1[i] == '-':
        num.append(b)
        b= ""
    else:
        b += str1[i]

num.append(b)
for num in num:
    print(num)

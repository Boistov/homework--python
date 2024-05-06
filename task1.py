text = input()
word = input()
num = -1

for i in range(len(text) - len(word) + 1):
    if text[i:i + len(word)] == word:
        num = i

if num!= -1:
    print(i)
else:
    print("error")
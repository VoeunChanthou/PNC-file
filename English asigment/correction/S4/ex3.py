text1 = input("enter your text:")
text2 = input("enter your text:")
first = 0
sencond = 0
sum = 0
for i in range(len(text1)):
    if text1[i].isupper():
        first += 1
sum += first
for j in range(len(text2)):
    if text2[j].isupper():
        sencond += 1
sum += sencond
print(sum)

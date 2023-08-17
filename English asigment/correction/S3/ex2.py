text = input("input your text: ")
A = 0
B = 0
for i in range(len(text)):
    if text[i] == "A" or text[i] == "a":
        A = 10
    elif text[i] == "B"or text[i] == "b":
        B = 20
print(A+B)
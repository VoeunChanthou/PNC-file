text = input()
isFound = True
i = 0
result = -1
while isFound and i < len(text):
    if text[i] == "o" or text[i] == "O":
        result = i
        isFound = False
    i += 1
if result >= 0:
    print(result)
else:
    print(result)
text = input()
inRange = -1
for i in range(len(text)):
    if text[i] == "K" or text[i] == "k":
        inRange = i
if inRange >= 0:
    print(inRange)
else:
    print(inRange)
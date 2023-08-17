N = input()
inFound = False
for i in range(len(N)):
    if int(N[i]) > 6:
        inFound = True
    else:
        inFound = False
print(inFound)
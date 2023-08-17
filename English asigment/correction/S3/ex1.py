# ---EX1----#
N = int(input("inter your number:"))
inRange = False
if N >= 1 and N <= 10:
    inRange = True
elif N >= 29 and N <= 51:
    inRange = True
elif N >= 76 and N <= 101:
    inRange = True
print(inRange)
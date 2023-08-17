N = int(input())
text = input()
if (N >= 1 and N <= 10) and text == "inside":
    print("True")
elif (N > 10 or N < 1) and text == "outside":
    print("True")
else:
    print("False")
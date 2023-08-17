
# exercise-1
# number = input()
# i = 0
# result = ""
# isSeven = False
# while (i+1) < len(number) and not isSeven:
#     if int(number[i]) < int(number[i+1]):
#         result = "SORTED"
#     else:
#         result = "NOT SORTED"
#         isSeven = True
#     i += 1
# print(result)


# exercise-2
# text = input()
# sum = 0
# i = 0
# isSeven = False
# while (i+2) < len(text) and not isSeven:
#     if text[i].upper() + text[i+1].upper() + text[i+2].upper() == "ABC":
#         sum += 1
#     else:
#         isSeven = True
#     i += 1
# if sum > 0:
#     print("OK")
# else:
#     print("WRONG")


# exercise-3
# text = input()
# result = " "
# thou = ""
# isSeven = True
# isFound = True
# for i in range(len(text)):
#     if text[i].upper() == "X" and isSeven:
#         result = "OK"
#     elif text[i] == "[":
#         isSeven = False
#         thou += text[i]
#     elif text[i] == "]":
#         isFound = False
#         thou += text[i]
#         isSeven = True
#     elif text[i].upper() == "Y" and not isSeven and isFound:
#         result = "OK"
# if thou == "[]" and result == "OK":
#     print("OK")
# else:
#     print("WRONG")



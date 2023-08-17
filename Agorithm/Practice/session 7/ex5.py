#  exercise-1
# number = input()
# sum = 0
# isSeven = False
# i = 0
# while i < len(number) and not isSeven:
#     if number != "7":
#         sum += int(number[i])
#     else:
#         isSeven = True
#     i += 1
# print(sum)

# exercise-2
# number = input()
# sum = 0
# i = 0
# isSeven = False
# while (i+1) < len(number) and not isSeven:
#     if number[-(i+1)] != "7":
#         sum += int(number[-(i+1)])
#     else:
#         isSeven = True
#     i += 1
# print(sum)

# exercise-3
# text = input()
# i = 0
# sum = 0
# while (i+1) < len(text):
#     if text[i].upper() + text[i+1].upper()  == "AB":
#         sum += 1
#     i += 1
# print(sum)
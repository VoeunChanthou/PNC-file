# exercise-1
# number1 = int(input())
# number2 = int(input())
# sum = 0
# if number2 > number1:
#     sum = number1 + number2
# else:
#     sum = -1
# print(sum)

# exercise-2
# text = input()
# i = 0
# isRange = True
# while i < len(text) and isRange:
#     if text[i].upper() == "A":
#         isRange = "True"
#     else: 
#         isRange = False
#     i += 1
# print(isRange)

# exercise-3
# isRange = True
# result = ""
# while isRange:
#     number = input()
#     if number.isnumeric():
#         if int(number)%2 == 0:
#             result += number + ":"
#     elif number.upper() == "END":
#         isRange = False
# print(result[:-1])


# exercise-4
# text = input()
# i = 0
# result = -1
# isRange = False
# while (i+1) < len(text) and not isRange:
#     if text[-(i)].upper() + text[-(i+1)].upper() == "KK":
#         result = len(text) - (i+1)
#         isRange = True
#     i += 1
# print(result)


# exercise-5
# number = input()
# i = 0
# sum = 0
# sum1 = 0
# number1 = ""
# number2 = ""
# isNumber = False
# while i < len(number):
#     if number[i] != ";" and not isNumber and number[i].isnumeric():
#         number1 += number[i]
#     elif number[i] == ";":
#         isNumber = True
#         sum1 += 1
#     elif isNumber and number[i].isnumeric():
#         number2 += number[i]
#     i += 1
# if sum1 > 0 and len(number1) == 2 and len(number2) == 2:
#     sum = int(number1) + int(number2)
# else:
#     sum = "WRONG FORMAT"
# print(sum)
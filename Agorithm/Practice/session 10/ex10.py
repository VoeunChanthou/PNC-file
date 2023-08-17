#  exercise-1 of session 10
# text = input()
# sum = 0
# i = 0
# while (i+2) < len(text):
#     if text[i].upper() + text[i+1].upper() + text[i+2].upper() == "ABC":
#         sum += 1
#     i += 1
# print(sum)


#  exercise-2 of session 10
# number = input()
# i = 0
# result = 0
# isSeven = False
# isFound = True
# while i < len(number) and not isSeven:
#     if number[i] != "6":
#         if number[i] == number[0] and isFound: 
#             result = int(number[i])
#             isFound = False
#         else:
#             result = result * int(number[i])
#     else:
#         isSeven = True
#     i += 1
# print(result)


# exercise-3 of session 10
# number = int(input())
# result = ""
# if number > 0:
#     for i in range(number):
#         result += str(i+1) + " "
# else:
#     result = "0"
# print(result)


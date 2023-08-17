
#  exercise-1
# number = input()
# i = 0
# isSeven = True
# isFound = "False"
# while i < len(number) and isSeven:
#     if number[i] == "7":
#         isFound = "True"
#         isSeven = False
#     i += 1
# print(isFound)


# exercise-2
# number = input()
# i = 0
# isSeven = True
# isFound = "False"
# while i < len(number) and isSeven:
#     if int(number[i]) > int(6):
#         isFound = "True"
#     else:
#         isFound = "False"
#         isSeven = False
#     i += 1
# print(isFound)


# exercise-3
# number = int(input())
# text = input()
# if (number >= 1 and number <= 10) and text == "inside":
#     isFound = "True"
#     print(isFound + "\n" + "We enter " + str(number) + """ + text + """ + "and" + str(number) + "is in range of [1, 10].")
# elif (number < 1 and number > 10) and text == "outside":
#     isFound = "True"
#     print(isFound + "\n" + "We enter " + str(number) + """ + text + """ + "and" + str(number) + "is in range of [1, 10].")
# else:
#     isFound = "False"
#     print(isFound + "\n" + "We enter " + str(number) + text +  "and" + " " + str(number) + "is outside the range of [1, 10].")


# exercise-4
# number = input()
# i = 0
# isSeven = True
# isFound = "False"
# while (i+1) < len(number) and isSeven:
#     if int(number[i+1]) > int(number[0]):
#         isFound = "SORTED"
#     else:
#         isFound = "NOT SORTED"
#         isSeven = False
#     i += 1
# print(isFound)
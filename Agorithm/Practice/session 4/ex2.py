#  exercise-1
# text = "goodMorning"
# # print(text[2])
# # print(text[-2])
# # print(text[1:2])
# print(text[:4])


#  exercise-2
# text = input()
# i = 0
# isSeven = True
# result = -1
# while isSeven and i < len(text):
#     if text[i].upper() == "O":
#         result = i
#         isSeven = False
#     i += 1
# print(result)


#  exercise-3
# text = input()
# text1 = input()
# sum = 0
# for j in range(len(text)):
#     if text[j].isupper():
#         sum += 1
# for k in range(len(text1)):
#     if text[k].isupper():
#         sum += 1
# print(sum)


#  exercise-4
# text = input()
# result = 0
# i = 0
# isFound = True
# while (i+1) < len(text) and isFound:
#     if text[-(i+1)].upper() == "K":
#         result = len(text) - (i+1)
#         isFound = False
#     i += 1
# print(result)



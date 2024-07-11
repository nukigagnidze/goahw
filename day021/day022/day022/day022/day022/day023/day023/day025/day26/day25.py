#1
# def oddoreven(s):
#     if s % 2 == 0:
#         print("num is even")
#     else:
#         print("num is odd")
# oddoreven(6)


#2
# num = 0
# for x in range(11):
#     num += x
# print(num)


#3
# listt = [1,2,3,45,2,3]
# listt = sorted(listt)
# print(listt[0])

#4
# listt = [1,3,2,4,5,2]
# listt = sorted(listt)
# print(listt[-1])



#5

# def stringcount(s):
     
#      count = 0
#      for x in s:

#         if x == "a":
#              count = count + 1
#         elif x == "e":
#             count = count + 1
#         elif x == "i":
#             count = count + 1
#         elif x == "o":
#             count = count + 1
#         elif x == "u":
#             count = count + 1
#      return count

# print(stringcount("dfsrrhsi"))


#6
# name = "luka"
# print(name[::-1])



#7
# def ifis(s):
#     oi = s[::-1]
#     if oi == s:
#         return True
#     else:
#         return False
    
# print(ifis("wow"))

#8
# listt = [1,2,3,414,5]
# num = 0
# for x in range(len(listt)):
#     num += 1
# print(num)

#9
# listt = [1,2,4,3,2,1]
# new_list = []
# for x in range(len(listt)):
#     new_list.append(listt[x]*listt[x])
# print(new_list)


#10
# def sqr(s):
#     return s * s

# print(sqr(5))


#11
# def newstr(s):
#     return s.upper()

# print(newstr("newe"))


#12
# def newfunct(s):
#     return s * 0.621371

# print(newfunct(23))

#13
# def newlist(s):
#     raodenoba = 0
#     new_num = 0
#     for x in s:
#         new_num += x
#     for x in range(len(s)):
#         raodenoba += 1
#     return new_num / raodenoba
# print(newlist([2,3,4,1,2]))

#14

# while True:
#     forguess = 4
#     user = int(input("enter ur desired number to guess: "))
#     if forguess == user:
#         print("u guessed congrats :wink: ")
#         break
#     else:
#         print("try again :/")


#15
# def manual_len(s):
#     count = 0
#     for x in s:
#         count += 1
#     return count

# print(manual_len("wsdwd"))


#16
# def manual_min(s):
#     s = sorted(s)
#     return s[0]

# print(manual_min([2,4,5,3,4,5]))


#17
# def manual_max(s):
#     s = sorted(s)
#     return s[-1]
# print(manual_max([24,4,23,5]))


#18
def calculator(num1,num2,operator):
        if operator == 1:
         add = num1 + num2
         return add
        elif operator == 2:
           sub = num1 - num2
           return sub
        elif operator == 3:
           mult = num1 * num2
           return mult
        elif operator == 4:
           divide = num1 / num2
           return divide

number1 = int(input("enter first number: "))
number2 = int(input("enter second number: "))
askop = int(input("enter which operator u want to use  1 == + , 2 == - , 3 == * , 4 == /: "))
print(calculator(number1,number2,askop))
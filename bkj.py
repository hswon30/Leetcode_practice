import math

# #1
# notice how the modulo operator works here on the remainder
# nums = input()
# numlist = nums.split(" ")
# m= map(int, numlist)
# A, B, C = m
# print((A+B) % C)
# print(((A%C) + (B%C))%C)
# print((A*B)%C)
# print(((A%C) * (B%C))%C)

# 2
# need to use map smarter. Also there is a way to split words differently, such as print([*string]) which is
# called unpack method.
# num1 = input()
# num2 = input()
# numlist1 = [x for x in num1]
# numlist2 = [x for x in num2]
# one, two, three = map(int, numlist1)
# four, five, six = map(int, numlist2)
# print(int(num1)*six)
# print(int(num1)*five)
# print(int(num1)*four)
# print(int(num1)*int(num2))

# 3
# numlist = input().split(" ")
# a, b, c = map(int, numlist)
# print(a+b+c)

# 4
# dont forget to escape \, as well as ""
# import string
#
# print("\\ \"  \"\"  /\\")
# print(" )  ( ')")
# print("(  /  )")
# print(" \(__)| ")

# 5
# ok, so unpacking input in this manner can work!
# a, b = map(int, input().split(" "))
#
#
# def which_is_bigger(num1, num2):
#     return ">" if num1 > num2 else ("<" if num1 < num2 else "==")
#
#
# print(which_is_bigger(a, b))

# 6
# mathmatical expressions 윤년
# num = int(input())
# res = 0
# if((num % 4 == 0) and (num % 100 != 0)) or (num % 400 == 0):
#     res = 1
# print(res)

# 7
# using time?
import time
# hour, minute = map(int, input().split(" "))
# rettime = 1
# backward_time = 45
# hour_in_minute = 60
# # alarm = time.time(hour=hour, minute=minute-45)
# #이걸 어떻게 if-elif 없이 고칠 수 있을까?
# if minute < 45:
#     if hour == 0:
#         hour = 24-rettime
#         minute = minute+(hour_in_minute-backward_time)
#     else:
#         hour = hour - rettime
#         minute = minute+(hour_in_minute-backward_time)
#
# else:
#     minute = minute-backward_time
#
# print(f'{hour} {minute}')

# 8
# using number and if statements more effiiciently
# edge cases edge cases...
# import math
# hour, minute = map(int, input().split(" "))
# time_to_cook = int(input())
# minutes_in_hour = 60
# hours_in_day = 24
# hours_to_cook = math.floor((minute+time_to_cook)/minutes_in_hour)
# days_past = int(hour+hours_to_cook/24)
# if minute+time_to_cook >= minutes_in_hour:
#     if (hour+hours_to_cook) % hours_in_day == 0:
#         hour = 0
#     else:
#         hour = hour+hours_to_cook-hours_in_day if hour+hours_to_cook > 24 else hour+hours_to_cook
#     minute = minute + time_to_cook - (hours_to_cook*minutes_in_hour)
# else:
#     minute = minute+time_to_cook
#
# print(f'{int(hour)} {minute}')


# 9
# combining various if else cases
# one, two, three = map(int, input().split(" "))
# award = 0
# if one == two == three:
#     award = award+10000+one*1000
# elif one == two:
#     award = award+1000+one*100
# elif two == three:
#     award = award + 1000 + three * 100
# elif one == three:
#     award = award + 1000 + one * 100
# else:
#     award = award+max(one, two , three)*100
#
# print(award)

# 10
# remember params for range() function
# num_to_mult = int(input())
# for num in range(1, 10):
#     print(f'{num_to_mult} * {num} = {num_to_mult*num}')

# 11
# range statement and getting multiline inputs
#
# res = []
# for __ in range(int(input())):
#     a, b = map(int, input().split(" "))
#     res.append(str(a+b))
#
# #remember newline can be used to join str > multiple print statements without a for loop
# print('\n'.join([num for num in res]))

# 12
# with and without for loop
# remember the range function params! going from 0(default) to given n-1!!
# res = 0
# for num in range(1, int(input())+1):
#     res += num
# print(res)

# without for loop
# def addition(num):
#     if num % 2 == 0:
#         return (num*(num+1))/2
#     else:
#         return((num+1)*(num+1))/4
#
# print(addition(int(input())))

# 13 thinking critically on division/floor/ceil
# import math
# print("long "*math.floor(int(input())/4)+"int")

# 14 using sys.stdin.readline()
# first attempt
# res = []
# import sys
# n = int(sys.stdin.readline().rstrip())
# for __ in range(n):
#     (a, b) = sys.stdin.readline().split(" ")
#     b.rstrip()
#     res.append(str(int(a)+int(b)))
#
# print(("\n").join([num for num in res]))

# now lets refine with list comprehension:
# #이렇게는 안되나?
# import sys
# n = int(sys.stdin.readline().rstrip())
# res = [str(int(a) + int(b.rstrip())) for (a, b = sys.stdin.readline().split(" ")) in range(n)]
#
# print(("\n").join([num for num in res]))
# THIS SHOULD WORK

# 15
# try catch(exception) handling and while w/True + using readline
# should separate out while w/the inputs
# import sys
# res = []
# while True:
#     try:
#         (a, b) = sys.stdin.readline().split(" ")
#     except ValueError as e:
#         break
#     b.rstrip()
#     res.append(str(int(a)+int(b)))
#
# print("\n".join([num for num in res]))

# 16
# list start!
# import sys
# count = 0
# n = int(sys.stdin.readline().rstrip())
# #REMEMBER THE SPLIT METHOD WITHOUT LITERAL DECLARATION
# nums = [int(num) for num in input().split(" ")[:n]]
# #print(nums)
# match = int(sys.stdin.readline().rstrip())
# for num in nums:
#     if num == match:
#         count += 1
#
# print(count)

# import sys
# n = int(sys.stdin.readline().rstrip())
# nums = [int(num) for num in sys.stdin.readline().split(" ")[:n]]
# print(f'{min(nums)} {max(nums)}')


# 17
# string manipulation
# #be mindfull of the newline character and space that is represented as "" instead of " "
import sys

# words = [word for word in sys.stdin.readline().split(" ") if word != "" and word != '\n']
# print(words)
# print(len(words))

# 18
# checking for valid next user inputs...is this possible?
# just EOF??
# ****need to know that EOFError is raised for input() but stdin.readline() returns empty string on EOF.****
# lines = []
# import sys
# while True:
#     try:
#         a = input()
#         if a.isspace() or a == "" or a == "\n":
#             break
#         else:
#             print(a)
#
#     except EOFError:
#         break

# 19
# using list, string ascii characters and how to associate multiple string with a single int
# be careful to use correct iteration methods on list and dictionary keys


# alphabets = string.ascii_uppercase
# print(alphabets)
#
# interval = 3
# alpha_list = [alphabets[initial:initial+interval] for initial in range(0, len(alphabets), interval)]
# print(alpha_list)

# num = 3
# res = 0
# alpha_dict = {}
# alpha_list = ['ABC', 'DEF', 'GHI', "JKL", "MNO", 'PQRS', 'TUV', 'WXYZ']
# for elem in alpha_list:
#     alpha_dict[elem] = alpha_list.index(elem)+num
#
# for char in input():
#     for elem in alpha_list:
#         if char in elem:
#             res += alpha_dict[elem]
#
# print(res)


# for char in input():
#     if char in alpha_list[0]:
#         res += 3
#     elif char in alpha_list[1]:
#         res += 4
#     elif char in alpha_list[2]:
#         res += 5
#     elif char in alpha_list[3]:
#         res += 6
#     elif char in alpha_list[4]:

# nums = map(alpha_list.index, alpha_list)
# print([num for num in nums])

# for num in range():
#     key_{
#
# print(key_2, key_3)
#
# # for char in input():
#     if char in
# key_1 = 2
# key_2 = ["A", "B", "C"]
# Key_3 = ["D", "E", "F"]

# 20
# working with index ranges
# res = []
# correct_set = [1, 1, 2, 2, 2, 8]
# given_set = [int(num) for num in input().split(" ")]
# for num in range(len(correct_set)):
#     res.append(correct_set[num]-given_set[num])
#
# print(" ".join([str(num) for num in res]))

# 21
# printing rules
# always keep the index ranges in mind.
# num_lines = int(input())
# ref = 0
# for num in range(2*num_lines-1):
#     if num < num_lines-1:
#         print(" "*(num_lines-1-num)+ref*"*"+"*")
#         ref += 2
#     else:
#         print(" "*(num-(num_lines-1))+ref*"*"+"*")
#         ref -= 2


# 22
# check pelindrome
# word = input()
# if len(word) % 2 == 0:
#     if word[0:int(len(word)/2)] == word[len(word):int(len(word)/2)-1:-1]:
#         print("1")
#     else:
#         print("0")
# else:
#     if word[0:int((len(word)-1)/2)] == word[len(word):int((len(word)+1)/2)-1:-1]:
#         print("1")
#     else:
#         print("0")


# 23
# counting methods
# be careful of how to approach dictionary keys. Also know how to manipulate dictionary values as well
# word_dict = {}
# maxval = 0
# maxword = ""
# word = input()
# for char in word:
#     letter = char.lower()
#     if letter in word_dict.keys():
#         word_dict[letter] += 1
#     else:
#         word_dict[letter] = 1
#
#
# for elem in word_dict.keys():
#     if word_dict[elem] > maxval:
#         maxval = word_dict[elem]
#         maxword = elem.upper()
#
# word_dict.pop(maxword.lower())
# if maxval in word_dict.values():
#     maxword = "?"
#
# print(maxword)

# 24
# checking index of a word
# if a word reappears after even one index then it's gonna be a non-group word
# this is pretty difficult isn't it?
# remember the basic rules: if any word is preceeded by a different word that appears afterward, then its not a group word.
# `def is_word_group(word):
#     in_res = 1
#     for place in range(len(word) - 1):
#         if word[place] != word[place + 1] and word[place] in word[place + 2:]:
#             # print("not group")
#             in_res -= 1
#             break
#
#         # bcaaaab = not group
#         # b in b+2~ but b is not b+1
#
#     return in_res
#
# res = 0
# for elem in range(int(input())):
#     # print("starting on loop")
#     # print(f'on word number {elem}')
#     res += is_word_group(input())
#
# print(res)`


# 25
# thinking critically on how to calculate along multiple lists
# REMEMBER that the list.pop() removes the last element and list.pop() = returns the popped element
# also use the round function to get a rounded value
# def find_average_group(grouplist):
#     #print("grouplist is:", grouplist)
#     num_students = int(grouplist[0])
#     grouplist = grouplist[1:]
#     #print(grouplist)
#     sum = 0
#     above = 0
#
#     for student in grouplist:
#         sum += student
#     average = sum/num_students
#     #print(average)
#     for student in grouplist:
#         if student > average:
#             above += 1
#
#     return str(round((above/num_students)*100, 3))
#
# for number in range(int(input())):
#     print(find_average_group([int(num) for num in input().split(" ")])+"%")


# 26
# working with arrays
# Keep in mind of the rules for the np array
# array_one_list = []
# array_two_list = []
# import numpy as np
#
# (array_one_index, array_two_index) = input().split(" ")
# for num in range(int(array_one_index)):
#     linelist = [int(num) for num in input().split(" ")]
#     print(linelist)
#     array_one_list.append(linelist)
# for num in range(int(array_one_index)):
#     linelist = [int(num) for num in input().split(" ")]
#     print(linelist)
#     array_two_list.append(linelist)
#
# print(array_one_list)
# print(array_two_list)
# array_one = np.array(array_one_list)
# array_two = np.array(array_two_list)
# print(array_one)
# print(array_two)
# for line in (array_one+array_two):
#     print(" ".join(map(str, line)))

# or without using numpy:
# res = []
# i, j = map(int, input().split(" "))
# # print(i, j)
# array_one_list = []
# array_two_list = []
# for num in range(i):
#     linelist = [int(num) for num in input().split(" ")]
#     array_one_list.append(linelist)
#
# for num in range(i):
#     linelist = [int(num) for num in input().split(" ")]
#     array_two_list.append(linelist)
#
# # print(array_one_list, array_two_list)
#
# for row in range(i):
#     for col  in range(j):
#         res.append(array_one_list[row][col]+array_two_list[row][col])
#
# # print(res)
#
# for num in range(j):
#     res_array = res[i*num:i*(num+1)]
#     print(' '.join([str(num) for num in res_array]))


# 27
# be mindful of the indices
# be careful of the edge cases where all elements are 0!!
# local_max = 0
# row_index = 1
# col_index = 1
#
# niner_res = []
# for __ in range(9):
#     linelist = [int(num) for num in input().split(" ")]
#     niner_res.append(linelist)
#
# for row in range(9):
#     for col in range(9):
#         if niner_res[row][col] > local_max:
#             local_max = niner_res[row][col]
#             row_index = row+1
#             col_index = col+1
#
#
# print(local_max)
# print(row_index, col_index)


# 28
# Changing between decimal and other base systems.
# keep in mind that decimal is just each place^10 = len(word)-loc(char)^10. Use this for conversion.
# alpha_dict = {}
# alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# print(alpha)
# for num, char in enumerate(alpha, start=10):
#     alpha_dict[char] = num
#
# res = 0
# numeral, base = input().split(" ")
# numlength = len(numeral)
# for mult, char in enumerate(numeral, start=1):
#     #print(char)
#     if char.isalpha:
#         #print("character conversion")
#         numeral = numeral.replace(char, str(alpha_dict[char]))
#         #print("base and mult is:", base, numlength-mult)
#         res += alpha_dict[char]*(pow(int(base), numlength-mult))
#
#     else:
#         res += char*(pow(int(base), numlength-mult))
#
# print(numeral)
# print(res)

# not difficult to turn back to Nth base:
# number.replace char with number first then append it to a list, iterate through each element to change into decimal place


# 29
# getting squares that grows exponentially: 4-9-25- see the trend? its (1+2n)^2
# rules: 4^2 = 16, but 9 so 4^2 -5 for each squares
# then for n = 2 its 4^3 - 5(4) = 64-20 doesnt make sense
# 2^2 3^2 5^2 9^2 > 1+2^0 1+2^1 1+2^2 1+2^3 1+2^4
# n = 0 then 1+1 ^ 2 = 4 and n = 1 then (1+2*1)^2 = 9
# n = 2 then (1+2*2)^2 = 25
# n = 3 then (1+2*3)^2
# n = 5 then = 1089
# 0 1 2 3 4 5
# 2-3-5-9-17-33
# 4-9-25-81-
#
#
# n = int(input())
# number_of_squares = pow(1+(2*n), 2)
# print(number_of_squares)

# 30
# getting remainders
# Its important to remember the ceil, // (floor division) and floor function. In this case,
# having 0 remainder after % means that only one more climb is needed.
# if there is any more remainder then the day must progress a day further, so +2
# import sys
# import math
# climb, fall, total = map(int, sys.stdin.readline().split(" "))
#
# if total <= climb:
#     print("1")
#
# elif (total-climb) % (climb-fall) == 0:
#     print((total-climb) // (climb-fall)+1)
# else:
#     print((total-climb) // (climb-fall)+2)


# simple brute force algo
# while True:
#     days += 1
#     res = res - climb
#     if res <= 0:
#         break
#     else:
#         res = res+fall
#
# print(days)

# if-else statement again
#
# while True:
#     a, b = map(int, input().split(" "))
#     if a == 0 and b== 0:
#         break
#     else:
#         if a % b == 0:
#             print("multiple")
#         elif b % a == 0:
#             print("factor")
#         else:
#             print("neither")

# 31
# be wary of the zerodivision and list index errors
# also keep in mind nth num is not! list index n, as index starts from 0.
# res = []
# N, K = map(int, input().split())
# for num in range(1, N + 1):
#     if N % num == 0:
#         res.append(num)

# print(res)
# try:
#     print(res[K - 1])
# except:
#     print("0")


# N= int(input())
# M = int(input())
# res = []

#why does this work for 2? because 2=2 so doesn't get into the for loop
#always look at the logic twice

# 32: finding prime number
# def is_prime(number):
#     for num in range(2, number):
#         print("entering eval for num:", num)
#         if num != number and number % num == 0:
#             return None
#     return number
#
#
# print(is_prime(2))

# for num in range (60, 100):
#     if is_prime(num) != None:
#         print(is_prime(num))

#33
#integer factorization
# def integer_factorization(number):
#     res = []
#     factor = 2
#     while True:
#         if number == 1:
#             return res
#
#         if number % factor == 0:
#             number = number / factor
#             res.append(factor)
#         else:
#             factor += 1
#
# number= int(input())
# print('\n'.join([str(num) for num in integer_factorization(number)]))


#34
# #O complexity algorithms
# import math
# n = int(input())
# i = math.ceil(n/2)
# print(i)
# print("0")


#35 finding the angle of the clock minute and hour hands
import math
# hour, minute = input("Input time").split(" ")
# hr = int(hour)
# min = int(minute)
# res = 0
# if min / hr > 5:
#     res = (min * 6) - (hr * 30 + (min*(1/60)))
# elif min / hr < 5:
#     res = (hr* 30 +min*(1/60)) - (min * 6)
#
# print(res)


#36 brute-forcing filling algorithm with backtracking 50, 100, 500, 1000:
# - this can't be done greedily, use dp with memoization
# num = input("Choose the amount that needs to be divided by")
# num_div = int(num)
# div_list = [0, 5, 10, 50, 100]
# res = 0
# cross_product = [i+j for i in div_list for j in div_list if (i+j) > 0]
# while(num_div >= 0):
#     for diver in cross_product:
#         if num_div % diver == 0:
#             res += 1
#     num_div -= 5

# print(cross_product)
# print(res)

def count_combinations(amount, bills):
    memo = {}

    def helper(remaining):
        if remaining == 0:
            return 1
        if remaining < 0:
            return 0
        if remaining in memo:
            return memo[remaining]

        count = 0
        for bill in bills:
            count += helper(remaining - bill)

        print(f"recursion depth increasing {count}")

        memo[remaining] = count
        return count

    return helper(amount)


num = int(input("Choose the amount that needs to be divided by: "))
bills = [5, 10, 50, 100]


result = count_combinations(num, bills)
print(result)

#37
def to_mixed_case(name):
    # ex_text2 = "__EXAMPLE__NAME__".lower()
    # print((''.join(ex_text2.split('_'))))
    if not any(char.isalpha() for char in name):
        return ''
    result = ''.join(word.capitalize() for word in name.split('_'))
    return result[0].lower() + result[1:]

#38


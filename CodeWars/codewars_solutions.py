#ROT13

def rot13(s):
    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    trans = chars[26:]+chars[:26]
    rot_char = lambda c: trans[chars.find(c)] if chars.find(c) > -1 else c
    return ''.join(rot_char(c) for c in s)

#Odd or Even?
def oddOrEven(arr):
    return ["even","odd"][sum(arr)%2]

#Help the bookseller !

def stock_list(list_of_art, list_of_cat):
    if list_of_art:
        dict = {x: [0] for x in list_of_cat}
        lst = []

        list_filtered = [x.split() for x in list_of_art if x[0] in list_of_cat]
        for k, v in list_filtered:
            dict[k[0]].append(int(v))
        for ele in list_of_cat:
            lst.append('(' + ele + " : " + str(sum(dict[ele])) + ')')
        return ' - '.join(lst)
    return ''

#reverse words

def reverse_words(str):
    l = str.split(" ")
    str = ""
    for string in l:
        str+= string[::-1] + " "
    return(str.strip())

#reversed string

def solution(string):
    return string[::-1]

#Is this a triangle?

def is_triangle(a, b, c):
  if(a+b>c and b+c>a and c+a>b):
      return True
  else:
      return False

#Two to One

def longest(s1, s2):
    sorted_s1 = sorted(set(s1))
    sorted_s2 = sorted(set(s2))
    (sorted_s1.extend(sorted_s2))
    return ("".join(sorted(set(sorted_s1))))

#Find the stray number

def stray(arr):
    unique = set(arr)
    return list(unique)[0] if arr.count(list(unique)[0]) < arr.count(list(unique)[1]) else list(unique)[1]

#find the odd int

def find_it(seq):
    for i in set(seq):
        if seq.count(i) % 2 != 0:
            return i

#sum of odd numbers

def row_sum_odd_numbers(n):
    start = n * (n-1) + 1
    sum = 0
    end = pow(n,2) + (n-1)
    for i in range(start,end+1,2):
        sum += i
    return(sum)

#find max and min valus of list

def min(arr):
    minimum = 6674780
    for val in arr:
        if val < minimum:
            minimum = val
    return minimum

def max(arr):
    maximum = -20000
    for val in arr:
        if val > maximum:
            maximum = val
    return maximum

#consecutive strings

def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ''

    longest = index = 0
    for i in range(n):
        length = sum([len(s) for s in strarr[i: i + k]])
        if length > longest:
            longest = length
            index = i

    return ''.join(strarr[index: index + k])

#square every digit

def square_digits(num):
    return int(''.join(list(str(i*i) for i in list(map(int,str(num))))))

#regex validate pincode

import re
def validate_pin(pin):
    regnumber = re.compile(r'^([0-9]{6}|[0-9]{4})$')
    if regnumber.match(pin):
        return True
    else:
        return False

#vowel count

def getCount(inputStr):
    num_vowels = 0
    # your code here
    vowel = ('a','e','i','o','u')
    for char in (inputStr):
        if char in vowel:
            num_vowels+=1
    return num_vowels

#convert number to reversed array of digits

def digitize(n):
    return (list(map(int,list(",".join(str(n)[::-1]))[::2])))

#friend or foe

def friend(x):
    return ([word for word in x if len(word) == 4])
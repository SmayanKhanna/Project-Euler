#P Euler Problem 4. Palindrome

from random import randint

def CheckPalindrome(num):
    a = str(num) 
    dig = len(a)
    
    if dig % 2 == 0:
        half = int(dig / 2)
        part_1 = a[0:half]
        part_2 = a[half:]
        adjust = part_2[::-1]
    else:
        half = int((dig + 1)/2)
        part_1 = a[0:half]
        part_2 = a[half-1:]
        adjust = part_2[::-1]
        
    if int(part_1) == int(adjust):
        return True
    else:
        return False

def Multiple(digits):
    prod = 10
    while CheckPalindrome(prod) != True:
        a = randint(900, 999)
        b = randint(900, 999)
        prod =  a * b
    print(prod)
    print(a)
    print(b)

Multiple(10)


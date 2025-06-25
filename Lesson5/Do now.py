#6/11/2025
'''
1) Define countVowels
2) declare the index value for the position of a string
3) declare the count variable for the amount of vowels

'''


def countVowels(n):
    index = 0
    count = 0
    while index < n[index]:
        if n == 'a' or 'e' or 'i':
            count += 1
        index +=1

    return count
countVowels('hello world') 
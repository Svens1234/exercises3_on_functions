#def vol(rad):
    #return (4/3)*(3.14)*(rad**3)


#print(vol(2))


#def ran_check(num,low,high):
    #if num in range(low,high+1):
        #print('{} находится в диапазоне между {} и {} '.format(num,low,high))
    #else:
        #print('Число находится в диапазоне')


#ran_check(5,2,7)

# Если вернуть только значение boolean


#def ran_bool(num,low,high):
    #return num in range(low,high+1)


#print(ran_bool(3,1,10))


#def up_low(s):
    #d = {"upper": 0, "lower": 0}
    #for c in s:
        #if c.isupper():
            #d["upper"]+=1
        #elif c.islower():
            #d["lower"]+=1
        #else:
            #pass
    #print("Исходная строка: ", s)
    #print("Количество символов в верхнем регистре : ", d["upper"])
    #print("Количество символов в нижнем регистре : ", d["lower"])


#s = 'Hello Mr Rogers, how are you this fine Tuesday? '
#up_low(s)


#def unique_list(lst):
    #x=[]
    #for a in lst:
        #if a not in x:
            #x.append(a)
    #return x


#print(unique_list([1,1,1,1,2,2,2,2,3,3,3,4,5]))


#def multiple(numbers):
    #total=1
    #for x in numbers:
        #total*=x
    #return total


#print(multiple([1,2,3,-4]))


#def palindrome(s):
    #s=s.replace(' ', '')
    #return s == s[::-1]


#print(palindrome('nurses run'))
#print(palindrome('abcba'))


import string


def ispangram(strl, alphabet=string.ascii_lowercase):
    aplhabet = set(alphabet)
    return aplhabet <= set(strl.lower())


print(ispangram("The quick brown fox jumps over lazy dog"))
print(string.ascii_lowercase)
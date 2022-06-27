#return duplicate elements count
'''
s = 'ajinkya'
d = {}
for i in s:
    d[i] = s.count(i)

print(d)

#program to remove duplicate character from string

from collections import OrderedDict
def remove_duplicates(str1):
    return "".join(OrderedDict.fromkeys(str1))

print(remove_duplicates("ajinkya"))
print(remove_duplicates("Python is bloddy easy language"))
'''

def remove_dup(str2):
    s = set(str2)
    s = "".join(s)
    print("without order",s)
    t = ""
    for i in str2:
        if (i in t):
            pass
        else:
            t = t + i
    print("with order",t)


str2 = "Python is bloddy easy language"
remove_dup(str2)
# get the occurrence of each character of string without using inbuilt function.
s = input("enter string")
d1 = {}
for i in s:
    if i in d1:
        d1[i] = d1[i] + 1
    else:
        d1[i] = 1
print(d1)

from collections import Counter
print(Counter(s).most_common())
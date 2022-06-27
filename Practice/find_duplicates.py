s = "AJINKYAaaaaaaa"
l = []

for i in s:
    if s.count(i)>1:
        if i not in l:
            l.append(i)

print(l)
print(len(l))
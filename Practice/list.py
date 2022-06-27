#get the second largest number from list without using inbuilt function.
'''l1 = list(map(int,input("enter numbers").strip().split()))
print(l1)
mx = max(l1[0], l1[1])
print(mx)
secondmax = min(l1[0], l1[1])
print(secondmax)
n = len(l1)
for i in range(2,n):
    if l1[i]>mx:
        secondmax = mx
        mx = l1[i]
    elif l1[i]> secondmax and mx != l1[i]:
        secondmax = l1[i]

print("second highest number is",str(secondmax))


l = list(map(int, input("Enter list").strip().split()))
print(l)
mx = max(l[0],l[1])
secondmax = min(l[0],l[1])
n = len(l)
for i in range(2,n):
    if l[i]>mx:
        secondmax = mx
        mx = l[i]
    elif l[i]>secondmax and mx != l[i]:
        secondmax = l[i]
print(type(secondmax))
print(str(secondmax))'''

l = list(map(int, input("Enter list").strip().split()))
mx = max(l)
l1 = []
for i in l:
    if i != mx:
        l1.append(i)
print(max(l1))
print(sorted(l))
print(sorted(l)[-3])
print(sorted(l)[-4])
print(sorted(l1))










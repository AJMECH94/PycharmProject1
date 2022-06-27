# swapping elements in list
def swap_list(l1 , pos1, pos2):
    n = len(l1)
    temp = l1[pos1]
    l1[pos1] = l1[pos2]
    l1[pos2] = temp
    return l1

l1 = [10,20,30,40,50]
pos1 = 0
pos2 = 4

print(swap_list(l1,pos1,pos2))

def swap_list1(l,p1,p2):
    l[p1], l[p2] = l[p2], l[p1]
    return l

l = [10,20,30,40,50]
p1,p2 = 0,4
print(swap_list1(l,p1,p2))
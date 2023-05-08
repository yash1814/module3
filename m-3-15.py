#Write a Python program to get unique values from a list

l1=[2,3,4,5,2,6,77,3,45,78,77]
l2=[]

for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)

l1= [6,9,7,1,3,5,6,8,"yashuka"]

print(type(l1))
print(l1)

#string is immutable, non modifieab
l1.remove("yashuka")
print(l1)

l1.sort()
print(l1)
print(l1.pop())

l1.append(54)
print(l1)
l1.clear()
print(l1)
l1.extend([747,45,34])
print(l1)
print(l1)

l1.index(34)
print(l1)

l1[0]="yash"
print(l1)
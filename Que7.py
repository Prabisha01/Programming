#add an item in a tuple
tuple1=(1,2,3,4, 5, 6)
l1=list(tuple1)
l1.append(7)
tuple1=tuple(l1)
print(tuple1)
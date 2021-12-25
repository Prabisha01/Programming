#print a specified list after removing the fourth element
list=[1,3,2,9,7,8,9,0]
for i in list:
    if i==list[3]:
        continue
    print(i,end=" ")
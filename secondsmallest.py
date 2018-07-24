array=[ ]
x = int(input("enter the number:"))
for i in range(x):
    item=input()
    array.append(item)
    array.sort()  
print(array)
print(array[1])

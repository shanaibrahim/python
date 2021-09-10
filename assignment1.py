#1
myList = [1, 7, 3, 90, 23, 4]
print(myList)


temp = myList[-1]
myList[-1] = myList[0]
myList[0] = temp

print(myList)

#2
list=[3,8,1,9,5]
list.sort()
print(list[0])

#3
list=[1,2,3,4,5,6,7,8]
for num in list:
    if num%2==0:
        print(num)

#4
list=[1,2,3,4,5,6,7,8]
for num in list:
    if num%2!=0:
        print(num)

#5
list=[-1,2,3,-7,-5,5]
for num in list:
    if num>=0:
        print(num)

#6
list=[-1,2,3,-7,-5,5]
for num in list:
    if num<=0:
        print(num)

#7
Fahrenheit= 54  
Celsius = ((Fahrenheit-32)*5)/9  
print("Temperature in Celsius is: ");  
print(Celsius);

#8
tuple=(3,1,7,3,9,6)

print("maximum number in a tuple is:",max(tuple))
print("minimum number in a tuple is:",min(tuple))

#9
list1=[1,2,3,4]
tuple1=tuple(list1)
print(tuple1)

#10
listx=[4,5,6,7]
listx.append(8)
print(listx)

list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
list1.extend(list2)
print(list1)

print(len(list1))











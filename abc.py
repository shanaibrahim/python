#list 1)

list=[1,4,6,3,7,1]
list.insert(1,55)
print(list)

list.pop(0)
print(list)

list.append(11)
print(list)

list.sort()
print(list)

#2)

list=[10,20,2,3,15]
list.sort()
print(list)
print("largest number is:",list[-1])

#3)

list1=[3,5,1]
list2=[10,4,15]
list3=list1+list2
print(list3)
list3.sort()
print(list3)

#string 1)

str="hello"
print(str)
print(str.replace('h',''))


#string 2)

str='aabbccaaa'
print(str.replace("a","$"))

#3)

string="aaaa"
print(string.isalnum())
print(string.isalpha())
print(string.isdigit())
print(string.islower())
print(string.isupper())

#4)
a='abcd'
b='efgh'
x=b[:2]+a[2:]
y=a[:2]+b[2:]

c=x+' '+y
print(c)

#tuple 1)

tuple=(1,2,3,4,5)
print(tuple)

#2)
print(tuple[3])
#3)

#4)
print(tuple.index(1))















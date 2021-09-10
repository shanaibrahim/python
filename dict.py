dict={'name':'shana','age':22}
print(dict)
dict['place']='ksd'
print(dict)


dict1={'abc':1,'def':2}
print(dict1)
dict2={'hij':3,'klm':4}
print(dict2)
dict1.update(dict2)
print(dict1)

d={1:2,3:4,5:6,7:8}
x=input('enter the key:')
if x in d:
    print('key is present')
else:
    print('key is not present')


dict={'abc':'def',1:2,3:4}
x=dict.pop(1)
print(dict)

X={1:10,2:20}
Y={3:30,4:40}
Z={5:50,6:60}
X.update(Y)
print(X)
X.update(Z)
print(Z)

set={'abc','def','hij'}
print(set)

x=set.remove('def')
print(set)

set1={'ab','cd','ef'}
set2={'cd','xy','wv'}
set3=set1.intersection_update(set2)
print(set1)

set1={'ab','cd','ef'}
set2={'cd','xy','wv'}
set3=set1.union(set2)
print(set3)

set1={'ab','cd','ef'}
set2={'cd','xy','wv'}
set3=set1.symmetric_difference(set2)
print(set3)










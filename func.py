'''str='earth'
list=[var for var in str]
print(list)

list1=['M','na','i','ke']
list2=['y','me','is','lly']
list3=[var for var in zip(list1,list2)]
print(list3)


alist=[1,2,3,4,5,6,7]
a=[var**2 for var in alist]
print(a)


sampledict={'name':'kelly','age':25,'salary':8000,'city':'newyork'}
dict={key for key in sampledict}
print(dict)'''

'''def prime(n):
    if n>1:
        for x in range(2,n):
            if n%x==0:
                print("not prime")
                break

        else:
            print('prime')

    else:
        print("not prime")
print(prime(7))

def test_prime(n):
    if (n==1):
        print("not prime")
        
    elif (n==2):
        print("prime")
        
    else:
        for x in range(2,n):
            if(n % x==0):
                 print("notprime")
        print("prime")  
               
               

def pal(string):
    
    string1=string[::-1]
    if(string==string1):
        print("given string is pallindrome")
    else:
        print("not pallindrome")
print(pal("malayalam"))

mylist=[1,2,3,4,5]
newlist=list(filter(lambda x:x%2==0,mylist))
print(newlist)

def is_panagram(sentence):
    alp='abcdefghijklmnopqrstuvwxyz' 
    for letter in alp:             
        if letter in sentence.lower():
            return True
    return False
            
                      
    
print(is_panagram("abcd"))'''

def pangram(x):
    alp='abcdefghijklmnopqrstuvwxyz'
    if set(alp)-set(x.lower())==set([]):
        print('pangram')
    else:
        print('not pangram')
           
        

print(pangram("abcd"))

        
    

    


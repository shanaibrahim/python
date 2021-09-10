f=open('abc.txt','w')
f.write(input("enter a number:"))
f.close()

f=open('def.txt','w')
f.write("twinkle twinkle\nlittle star\nhow a wonder\nwhat you are")
f.close()

f=open('def.txt','r')
p=f.readlines()
print(p)

f=open('def.txt','r')
p=f.readline()
print(p)

f=open('def.txt','r')
count=0
for line in f:
    if line!='\n':
        count=count+1
f.close()
print(count)
        
    
    

    






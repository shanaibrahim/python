#1
'''import re
def txt(text):
    patterns="a*b$"
    if re.search(patterns,text):
        return "found a match"
    else:
        return "not matched!"
print(txt("abcg"))
print(txt("abbbb"))

#2
import re
def txt(text):
    patterns="\Arain"
    if re.search(patterns,text):
        return "found a match"
    else:
        return "not matched!"
print(txt("rainabcd"))
print(txt("abbb"))

#3
import re
def txt(text):
    patterns="^1"
    if re.search(patterns,text):
        return "found a match"
    else:
        return "not matched!"
print(txt("hfjhdg"))
print(txt("1abbb"))

#4
import re
txt="rain in spain"
x=re.findall("ai",txt)
print(x)

#5
import re
text = 'Python Exercises'
text =text.replace (" ", "_")
print(text)
text =text.replace ("_", " ")
print(text)

import re
txt="1frg4hrtj6"
x=re.split("\D+",txt)
print(x)'''






import os
import time
import re

#elimina etiquetas html
def strip_tags(value):
    return re.sub(r'<[^>]*?>', '', value)

#main
print "+----------------------------------+"
print "|             BuiltWith            |"
print "+----------------------------------+"

url = raw_input("Ingrese la url: ")
print "* Target: "+ url+"\n"
os.system('curl https://builtwith.com/'+ url+ '>temp.txt' )

f = open ('temp.txt','r')
info = f.read()
a=0
b=0
s = ""
while a!=-1 and b!=-1:
    a = info.find("<h6 class=\"card-title\">",a+1)
    b = info.find("<",a+1)
    for i in range(a+23,b):
        s = s +  info[i]
    s = s+":\n"
    c = info.find("<h2",b+1)
    c = info.find("<a",c+1)
    c = info.find(">",c+1)
    d = info.find("<",c+1)
    for i in range(c,d):
        s = s +  info[i]
    s= s+".\n"
print s
f.close()
os.system('rm temp.txt');

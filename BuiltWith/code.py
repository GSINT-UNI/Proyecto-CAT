import os
import time

#main
print "+----------------------------------+"
print "|             BuiltWith            |"
print "+----------------------------------+"

url = raw_input("Ingrese la url: ")
print "* Target: "+ url+"\n"
os.system('curl https://builtwith.com/'+ url+ '>temp.txt' )

f = open ('temp.txt','r')
info = f.read()
a = info.find("")



f.close()
os.system('rm temp.txt');

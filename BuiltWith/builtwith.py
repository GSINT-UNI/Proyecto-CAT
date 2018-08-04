import os
import time 

#main
print("+----------------------------------+")
print("|             BuiltWith            |")
print("+----------------------------------+")

url = input("Ingrese la url: ")
print("* Target: "+ url+"\n")
os.system('curl https://builtwith.com/'+url+'>temp.txt')
aux=0
lim_aux=0
f = open ('temp.txt','r')
info = f.read()
ini2=0
fin2=0
ini=0
fin=0
herramienta=""
while ini != -1:
	ini=ini+1	
	ini=info.find("<h6 class=\"card-title\">",ini)
	limite=info.find("<h6 class=\"card-title\">",ini+1)
	fin=info.find("<",ini+1)
	for a in range(ini+len("<h6 class=\"card-title\">"),fin):
		herramienta=herramienta+info[a]
	print(herramienta)
	herramienta=""
	
	
	tool=""
	if limite==-1:
		limite=len(info)				
	while ini2<limite :
		
		ini2=ini2+1	
		ini2=info.find("<a class=\"text-dark\" href=\"",ini2)
		ini2=info.find(">",ini2)
		fin2=info.find("<",ini2)
		for a in range(ini2+1,fin2):
			tool=tool+info[a]
		print("   "+tool)
		tool=""
		if info.find("<a class=\"text-dark\" href=\"",ini2)>limite or limite==len(info):
			break

os.system('rm temp.txt')

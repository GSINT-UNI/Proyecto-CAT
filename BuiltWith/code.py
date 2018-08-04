import os
import time

#main
print("+----------------------------------+")
print("|             BuiltWith            |")
print("+----------------------------------+")

url = input("Ingrese la url: ")
print("* Target: "+ url+"\n")
os.system('curl https://builtwith.com/'+url+'>temp.txt')

f = open ('temp.txt','r')
info = f.read()
ini2=0
fin2=0
ini=0
fin=0
herramienta=""
print ("\n")
print("##########################################")
print("#       HERRAMIENTAS ENCONTRADAS         #")
print("##########################################")

while ini != -1:
    ini=ini+1
    ini=info.find("<h6 class=\"card-title\">",ini)
    limite=info.find("<h6 class=\"card-title\">",ini+1)
    fin=info.find("<",ini+1)
    for a in range(ini+len("<h6 class=\"card-title\">"),fin):
        herramienta=herramienta+info[a]
    if(herramienta!=""):
        print("# "+herramienta)
    herramienta=""
    tool=""
    ini2=ini
    if limite==-1:
        limite=len(info)
    while ini2<limite:
        ini2=ini2+1
        ini2=info.find("<a class=\"text-dark\" href=\"",ini2,limite)
        ini2=info.find(">",ini2,limite)
        fin2=info.find("<",ini2,limite)
        for a in range(ini2+1,fin2):
            tool=tool+info[a]
        if(tool!=""):
            print("   *"+tool)
        if (ini2==-1):
            break

f.close()
os.system('rm temp.txt');

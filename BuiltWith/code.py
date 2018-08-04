import os
import time

#main
print("+----------------------------------+")
print("|             BuiltWith            |")
print("+----------------------------------+")

url = input("Ingrese la url: ")
print("* Target: "+ url+"\n")
os.system('curl https://builtwith.com/'+url+'>temp.txt')    #ingreso de la url a investigar

f = open ('temp.txt','r')   #se abre  un archivo temporal para guardar el codigo fuente de la pag
info = f.read()
#inicializacion de los limites de las subcadenas
ini=0   #indice inicial del Tipo de herramienta
fin=0   #indice final del Tipo de herramienta
ini2=0  #indice inicial de la herramienta en especifico
fin2=0  #indice inicial de la herramienta en especifico

print ("\n")
print("##########################################")
print("#       HERRAMIENTAS ENCONTRADAS         #")
print("##########################################")

while ini != -1:    #bulce buscar el tipo de herramientas
    ini=ini+1   #instrucción que nos permite continuar con el sig tipo de herramienta
    ini=info.find("<h6 class=\"card-title\">",ini)  #busca el titulo en especifico (tipo de herramienta)
    limite=info.find("<h6 class=\"card-title\">",ini+1) #busca el sig titulo
    fin=info.find("<",ini+1)    #fin del titulo
    herramienta=""  #cadena que indica el tipo de herramienta
    for a in range(ini+len("<h6 class=\"card-title\">"),fin):   #bucle para almacenar el nombre del tipo de herramienta
        herramienta=herramienta+info[a]
    if(herramienta!=""):
        print("# "+herramienta)

    tool="" #cadena que indica la herramienta en especifico
    ini2=ini    #inicializacion de la herramienta en especifico tomando como punto de partida el tipo de herramienta
    if limite==-1:  #si es el ultimo tipo de herramienta entonces toma el limite como el indice final del codigo fuente
        limite=len(info)
    while ini2<limite:  #bucle para encontrar las herramientas especificas
        ini2=ini2+1 #instrucción que nos permite continuar con la sig herramienta
        ini2=info.find("<a class=\"text-dark\" href=\"",ini2,limite)    #busca la herramienta usando ese patron
        ini2=info.find(">",ini2,limite) #checkpoint para saber donde comienza el nombre de la herramienta
        fin2=info.find("<",ini2,limite) #limitador de fin del nombre de la herramienta
        if (ini2==-1):  #si no encuentra más sale del bucle para buscar el sig tipo de herramienta
            break
        for a in range(ini2+1,fin2):#bucle para almacenar el nombre de la herramienta en especifico
            tool=tool+info[a]
        if(tool!=""):
            print("   *"+tool)


f.close()   #se cierra el archivo temporal
os.system('rm temp.txt')    #se elimina el archivo temporal

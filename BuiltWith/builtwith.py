import os
import time 

#main
print("+----------------------------------+")
print("|             BuiltWith            |")
print("+----------------------------------+")

url = input("Ingrese la url: ")    # ingresamos el url deseado
print("* Target: "+ url+"\n")   
os.system('curl https://builtwith.com/'+url+'>temp.txt')  # guardamos el codigo fuente en un archivo temporal temp.txt
aux=0
lim_aux=0
f = open ('temp.txt','r')
info = f.read()      # almacenamos todo el codigo fuente como un string
ini2=0    # apuntador para busqueda de herramientas específicas
fin2=0	  # delimitador para busqueda de herramientas especificas
ini=0 	 # apuntador para busqueda de herramientas generales
fin=0	 # delimitador para busqueda de herramientas generales
herramienta=""  # cadena que almacenará cada herramienta general
while ini != -1:          # en este bucle se buscan las herramientas generales
	ini=ini+1	# se empiezan a fijar los limites para la busqueda de las herramientas generales		
	ini=info.find("<h6 class=\"card-title\">",ini)         
	limite=info.find("<h6 class=\"card-title\">",ini+1)
	fin=info.find("<",ini+1)
	for a in range(ini+len("<h6 class=\"card-title\">"),fin):   # una vez que tenemos los limites, almacenamos el nombre de la herramienta general letra por letra
		herramienta=herramienta+info[a]
	print(herramienta)
	herramienta=""
	
	
	tool=""     # cadena que almacenará cada herramienta específica
	if limite==-1:    # sirve para obtener la ultima herramienta especifica de la ultima herramienta general
		limite=len(info)				
	while ini2<limite :    # en este bucle se buscan las herramientas específicas
		
		ini2=ini2+1	   # igual que en el bucle anterior, se procede a delimitar
		ini2=info.find("<a class=\"text-dark\" href=\"",ini2)
		ini2=info.find(">",ini2)
		fin2=info.find("<",ini2)
		for a in range(ini2+1,fin2):   # almacenamos el nombre de la herramienta específica
			tool=tool+info[a]
		print("   "+tool)
		tool=""
		if info.find("<a class=\"text-dark\" href=\"",ini2)>limite or limite==len(info):  # es para que no se imprime una herramienta especifica no correspondiente a una herramienta general
			break

os.system('rm temp.txt')    # eliminación del archivo temporal

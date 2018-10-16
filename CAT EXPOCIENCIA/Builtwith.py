import commands
import time

def builtwith(url):
	#main
	f1 = open ('/home/elchala/Escritorio/veremos.txt','a')
	
	print "+----------------------------------+"
	f1.write("+----------------------------------+"+"\n")
	print "|             BuiltWith            |"
	f1.write("|             BuiltWith            |"+"\n")
	print "+----------------------------------+"
	f1.write("+----------------------------------+"+"\n")


	print "* Target: "+ url+"\n"
	f1.write("* Target: "+ url+"\n")
	commands.getoutput('curl https://builtwith.com/'+url+'>BuiltWith.temp')  # guardamos el codigo fuente en un archivo temporal temp.txt
	aux=0
	lim_aux=0
	f = open ('BuiltWith.temp','r')
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
		for a in range(ini+len("<h6 class=\"card-title\">"),fin):   # una vez que tenemos los limites, almacenamos el nombre de la herramienta general letra por letra
			herramienta=herramienta+info[a]
		print herramienta
		f1.write(herramienta+"\n")
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
			print "   "+tool
			f1.write("   "+tool+"\n")
			tool=""
			if info.find("<a class=\"text-dark\" href=\"",ini2)>limite or limite==len(info):
				break
	
	f.close()
	f1.close()
	commands.getoutput('rm BuiltWith.temp')

	

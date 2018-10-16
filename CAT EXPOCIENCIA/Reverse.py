import commands
import socket
import os

def reverse(web,ips):
	f2=open("/home/elchala/Escritorio/veremos.txt","a")
	print "+----------------------------------+"
	f2.write("+----------------------------------+"+"\n")
	print "|             ReverseIP            |"
	f2.write("|             ReverseIP            |"+"\n")
	print "+----------------------------------+"
	f2.write("+----------------------------------+"+"\n\n")

	ip = socket.gethostbyname(web)

	print "La ip de "+web+" es: "+ip
	f2.write("La ip de "+web+" es: "+ip+"\n\n")
	print "  "
	f2.write("  "+"\n")
	if ip not in ips:		
		print "#########################################"
		f2.write("#########################################"+"\n")
		print "Reverse Shell, resulado de analizar la direccion "+ip
		f2.write("Reverse Shell, resulado de analizar la direccion "+"\n")
		commands.getoutput("curl http://api.hackertarget.com/reverseiplookup/?q="+ip+" > reverse.temp")

		f = open ('reverse.temp','r')#temp4.txt
		reverse = f.read()

		print "\n#########################################"
		f2.write("\n#########################################"+"\n")	
		print "Informacion Obtenida"
		f2.write("Informacion Obtenida"+"\n")	
		print "#########################################\n"
		f2.write("#########################################\n"+"\n")		
		print reverse
		for x in reverse:		
			f2.write(x)		
	else:
		print "La ip ya fue analizada"
		f2.write("La ip ya fue analizada"+"\n")		
	f2.close()
	f.close()

import commands
import os

def subdomain(web):
	f3=open("/home/elchala/Escritorio/veremos.txt","a")
	print "+----------------------------------+"
	f3.write("+----------------------------------+\n")	
	print "|             SubDomain            |"
	f3.write("|             SubDomain            |\n")		
	print "+----------------------------------+"
	f3.write("+----------------------------------+\n")			

	print "#########################################"
	f3.write("#########################################\n")			
	print "Subdominios, resulado de analizar la web "+web
	f3.write("Subdominios, resulado de analizar la web "+web+"\n")			
	commands.getoutput('curl https://api.hackertarget.com/hostsearch/?q='+web+' > SubDomain.temp')
	f = open ('SubDomain.temp','r')
	reverse = f.read()

	print "\n#########################################"
	f3.write("\n#########################################"+"\n")			
	print "Informacion Obtenida"
	f3.write("Informacion Obtenida\n")				
	print "#########################################\n"
	f3.write("#########################################"+"\n")			
	print reverse
	f3.write(reverse+"\n")			
	#os.system('rm SubDomain.temp');
	print "#########################################"
	f3.write("#########################################"+"\n")			
	f3.close()
	f.close()

# -- encoding: utf-8 --
import socket
import Nmap
import Subdomain
import Reverse
import Shodan
import Builtwith
import commands


print "▄████▄   ▄▄▄     ▄▄▄█████▓"
print "▒██▀ ▀█  ▒████▄   ▓  ██▒ ▓▒"
print "▒▓█    ▄ ▒██  ▀█▄ ▒ ▓██░ ▒░"
print "▒▓▓▄ ▄██▒░██▄▄▄▄██░ ▓██▓ ░" 
print "▒ ▓███▀ ░ ▓█   ▓██▒ ▒██▒ ░" 
print "░ ░▒ ▒  ░ ▒▒   ▓▒█░ ▒ ░░"   
print "  ░  ▒     ▒   ▒▒ ░   ░"    
print "░          ░   ▒    ░"      
print "░ ░            ░  ░"        
print "░"

x=open("/home/elchala/Escritorio/veremos.txt","a")
ips=[]
subpaginas=[]  # lista que va recopilando las paginas y subdominios

subdominios_paginas=[]
subdominios_ips=[]
dir=raw_input("Ingrese una direccion web :   ")
Subdomain.subdomain(dir)  # analizo los subdominios de la direccion
Reverse.reverse(dir,ips) # imprime el IP de la pagina e imprime las paginas asociadas a dicha ip
subpaginas.append(dir)   # insertaba la pagina inicial a la lista de paginas
ips.append(socket.gethostbyname(dir))  # insertaba la primera ip encontrada

archivo=open('SubDomain.temp','r')


for lines in archivo.readlines():
	pos=lines.find(",")
	subpaginas.append((lines[:pos]).rstrip("\n"))
	ips.append(lines[pos+1:].rstrip("\n"))				

archivo.close()
print "****APLICANDO EL REVERSE IP A LOS RESULTADOS DE Subdomain Y OBTENER LAS IP'S DE CADA UNO****"
x.write("****APLICANDO EL REVERSE IP A LOS RESULTADOS DE Subdomain Y OBTENER LAS IP'S DE CADA UNO****\n")

aux=list(set(subpaginas))
print "LAS SUBPAGINAS SON:   ", aux
for domain in aux:
	print "Analizando el subdominio  --- ",domain,"    "	
	x.write("Analizando el subdominio  --- "+domain+"    \n")	
	Reverse.reverse(str(domain),subdominios_ips)
	archivo2=open('reverse.temp','r')

	for lines in archivo2.readlines():	
		subdominios_paginas.append(lines.rstrip("\n"))
		print "ANALIZANDO EL CONTENIDO LINEA:  " + lines[:-1],
		x.write("ANALIZANDO EL CONTENIDO LINEA:  " + lines[:-1] +"\n")
		try:
			subdominios_ips.append(socket.gethostbyname(lines.rstrip("\n")))
			print "\t[CORRECTO]"
			x.write("\t[CORRECTO]\n")
		except:
			print "[NO SE PUDO OBTENER EL IP]"
			x.write("[NO SE PUDO OBTENER EL IP]\n")	
	archivo2.close()

print "################ ANALISIS DE LAS DIRECCIONES IPS ENCONTRADAS ################"
x.write("################ ANALISIS DE LAS DIRECCIONES IPS ENCONTRADAS ################\n")

print "ips de subdominios: ***** ",ips


ips=list(set(ips))
subdominios_ips=list(set(subdominios_ips))
ips.extend([element for element in subdominios_ips if element not in ips])

subpaginas=list(set(subpaginas))
subdominios_paginas=list(set(subdominios_paginas))
subpaginas.extend([element for element in subdominios_paginas if element not in subpaginas])





for ip in ips:
	print "ANALIZANDO LA DIRECCION  ",ip
	x.write("ANALIZANDO LA DIRECCION  "+ip+" con NMAP y SHODAN\n")	
	#Nmap.nmap(ip)
	#Shodan.shodan(ip)

print subpaginas

for page in subpaginas:
    

    print "ANALIZANDO LA PAGINA   ",page
    x.write("ANALIZANDO LA PAGINA   "+page+"\n")	
    try:
        Builtwith.builtwith(page)
    except:
        print "[NO SE PUDO ANALIZAR LA PAGINA]"
	x.write("[NO SE PUDO ANALIZAR LA PAGINA]\n")

x.close()	


















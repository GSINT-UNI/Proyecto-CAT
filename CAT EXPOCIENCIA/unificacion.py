import socket
import Nmap
import Subdomain
import Reverse
import Shodan
import Builtwith
import commands

ips=[]
subpaginas=[]
dir=raw_input("Ingrese una direccion web :   ")
Reverse.reverse(dir,ips)
Subdomain.subdomain(dir)
f=open('reverse.temp','r')
for linea in f.readlines():
	subpaginas.append(linea)
	f.close
	commands.getoutput('rm reverse.temp')


dir_ip=socket.gethostbyname(dir)
ips.append(dir_ip)
dir_2=dir_ip

Nmap.nmap(dir_ip)
Shodan.shodan(dir_2)

Builtwith.builtwith(dir)


print "  "
print "###############  ANALIZANDO LAS PAGINAS ANIDADAS QUE FUERON ENCONTRADAS  ###############"

for pagina in subpaginas:
	pagina=pagina.rstrip('\n')
	print "--> Analizando ",pagina,"  : "
	Builtwith.builtwith(pagina)
	Reverse.reverse(pagina,ips)
	commands.getoutput('rm reverse.temp')
	Subdomain.subdomain(pagina)
	dir_temp=socket.gethostbyname(str(pagina))
	dir_temp2=dir_temp
	if dir_temp not in ips:
		ips.append(dir_temp)
		Nmap.nmap(dir_temp)
		Shodan.shodan(dir_temp2)
	else:
		print "La ip ya fue analizada"

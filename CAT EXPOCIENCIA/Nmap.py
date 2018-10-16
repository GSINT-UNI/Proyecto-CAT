import commands
import time
import os

def nmap(ip):
    f4=open("/home/elchala/Escritorio/veremos.txt","a")
    print "#########################################"
    f4.write("#########################################\n")
    print "NMAP resulado de analizar la direccion "+ip
    f4.write("NMAP resulado de analizar la direccion "+ip+"\n")
    print ""
    f4.write("  "+"\n")
    commands.getoutput('nmap -sV '+ ip +' > Nmap.temp')
    f = open ('Nmap.temp','r')#temp2.txt
    #info = f.read()
    #print(info)
    r = 0
    for linea in f.readlines():
        if (linea[0:4] == "PORT"):
            r = 1
        if (r == 1):
            print linea,
	    f4.write(linea+"\n")
        if (linea[0:2] == "\n"):
            r = 0

    f.close()
    os.system('rm Nmap.temp');
    print "#########################################"
    f4.write("#########################################"+"\n")
    f4.close()

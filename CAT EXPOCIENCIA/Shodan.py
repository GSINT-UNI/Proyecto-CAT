import commands
import time
import os

def shodan(ip):
    f7=open("/home/elchala/Escritorio/veremos.txt","a")
    print "#########################################"
    f7.write("#########################################"+"\n")
    print "SHODAN resulado de analizar la direccion "+ip
    f7.write("SHODAN resulado de analizar la direccion "+ip+"\n")
    #200.48.22.200
    commands.getoutput('curl https://www.shodan.io/host/'+ ip +' > Shodan.temp')

    f = open ('Shodan.temp','r')#temp.txt
    info = f.read()
    #print(info)
    a = info.find("<table class=\"table\">")
    b = info.find("</table>")

    porcion = info[a:b]
    #print porcion
    #Imprimiendo informacion
    print "\n#########################################"
    f7.write("\n#########################################"+"\n")
    print "Informacion Obtenida"
    f7.write("Informacion Obtenida"+"\n")
    print "#########################################"
    f7.write("#########################################"+"\n")
    r = 0
    q = 0
    preimagen = ""
    imagen = ""
    wtech = ""

    for i in range(0,len(porcion)-1):
        if (porcion[i-4:i] == "<td>"):
            r = 1
        if (r == 1):
            if (porcion[i] != "<"):
                preimagen = preimagen + porcion[i]
            else:
                r = 0
                print preimagen+": ",
		f7.write(preimagen+": "+"\n")
                preimagen = ""

        if (porcion[i-4:i] == "<th>"):
            q = 1
        if (q == 1):
            if (porcion[i] != "<"):
                imagen = imagen + porcion[i]
            else:
                q = 0
                print imagen
		f7.write(imagen+"\n")
                imagen = ""

    #Obteniendo la seccion web tech
    a = info.find("<div class=\"http-components\">")
    b = info.find("<i class=\"fa fa-th-large\">")
    porcion2 = info[a:b]
    #print porcion2

    wtech = ""
    t = 0

    print "Tecnologias web: ",
    f7.write("Tecnologias web: "+"\n")

    for i in range(0,len(porcion2)-1):
        if (porcion2[i-2:i] == "/>"):
            r = 1
        if (r == 1):
            if (porcion2[i] != "<"):
                wtech = wtech + porcion2[i]
            else:
                r = 0
                print wtech[:-1]+", ",
	        f7.write(wtech[:-1]+", "+"\n")
                wtech = ""
    print "\b\b\b."
    f7.write("\b\b\b."+"\n")

    #Obteniendo la info de los puertos
    a = info.find("<ul class=\"services\">")
    b = info.find("<div class=\"footer muted\">")
    porcion3 = info[a:b]

    port = ""
    sport = 0
    protocol = ""
    sprotocol = 0
    state = ""
    sstate = 0
    name = ""
    sname = 0

    print "\n#########################################"
    f7.write("\n#########################################\n")
    print "Informacion sobre puertos"
    f7.write("Informacion sobre puertos\n")
    print "#########################################"
    f7.write("\n#########################################\n")	
    print "Port TCP/UDP Protocolo Servicio Version"
    f7.write("Port TCP/UDP Protocolo Servicio Version\n")	
    #print porcion3

    for i in range(0,len(porcion3)-1):
        if (porcion3[i-6:i] == "port\">"):
            sport = 1
        if (sport == 1):
            if (porcion3[i] != "<"):
                port = port + porcion3[i]
            else:
                sport = 0
                print port+ " ",
	        f7.write(port+ " "+"\n")	
                port = ""

        if (porcion3[i-10:i] == "protocol\">"):
            sprotocol = 1
        if (sprotocol == 1):
            if (porcion3[i] != "<"):
                protocol = protocol + porcion3[i]
            else:
                sprotocol = 0
                print protocol+ " ",
		f7.write(protocol+"  "+"\n")
                protocol = ""

        if (porcion3[i-7:i] == "state\">"):
            sstate = 1
        if (sstate == 1):
            if (porcion3[i] != "<"):
                state = state + porcion3[i]
            else:
                sstate = 0
                print state+ " ",
		f7.write(state+" "+"\n")
                if (porcion3.find("<h3>")):
                    print ""
		    f7.write(""+"\n")	
                state = ""
    #<h3>

        if (porcion3[i-4:i] == "<h3>"):
            sname = 1

        if (sname == 1):
            if (porcion3[i:i+5] != "</h3>"):
                name = name + porcion3[i]
            else:
                sname = 0
                if (name.find("<small>") < 0):
                    print name+ " "
		    f7.write(name+" "+"\n")
                else:
                    h = name.find("<small>")
                    e = name.find("</small>")

                    print name[0:h]+" ",
		    f7.write(name[0:h]+" "+"\n")
		    
                    print name[h+7:e]
		    f7.write(name[h+7:e]+" "+"\n")
                name = ""

    print ""
    f7.write(""+"\n")
    f.close()
    os.system('rm Shodan.temp');
    f7.close()

import sys
import os

 
def ayuda():
    ayuda = """

Parametros:

-requisitos [Instalar requeriminetos]

Uso: python3 infoIP.py <IP>

Ejemplo: python3 infoIP 194.205.140.20
            """
    print(ayuda)
        
def logo():
    logo = """
+------------------------------------------------------------+
|MMMMMMMMMMMMMMMMMMMMMMKdc,.      .,cdKMMMMMMMMMMMMMMMMMMMMMM|
|MMMMMMMMMMMMMMMMWOocccldk0KXNNNNXKOkdc:::oOWMMMMMMMMMMMMMMMM|
|MMMMMMMMMMMMMKo::d0WMWNMMMMXdWxkxXOKNXWMW0d:;lKMMMMMMMMMMMMM|
|MMMMMMMMMMXl;l0MMXWkOolXMMMNxWxOxOdOK;lxOKXMW0c,lXMMMMMMMMMM|
|MMMMMMMMK;;OMMK0koxxX0XMMMMMMMMMMMMMWWKKkOdkoMMWk';KMMMMMMMM|
|MMMMMMK;;KMNk:lk0XMMMMWNNNXXXXKXXXNNNWMMMMX0ok:kNMO,;KMMMMMM|
|MMMMMo'0MNkkkxNMMMWNNNWNNNWNWNNMWNNNNWNNNWMMMNxloOWMk.oMMMMM|
|MMMX'cWMXdOdXMMMNXXNWWNWMMNMMNNMMWMMNXWNNNNWMMM0OKx0MW;'XMMM|
|MMN.dMM0cckMMMWXWMMWXNNNNXNNlxc;0NXNNNXNMMMNXWMMMO:lKMMl.XMM|
|MW'dMM0OdKMMMNXMMMMNWMMMNNMWd0l kMNWMMMNNMMMMXNMMMKXOkMMl.WM|
|M:;MMWxkOMMMXNWWWWNXWMMMXWMMMKdWMMMXMMMWXNNWWWNNMMMkK0MMM,;M|
|O XMMx:oWMMNNMMMMWXWWNNXKNNNN:cNNNNXNNNWWKMMMMMNNMMMoOkMMK O|
|;cMMMkdOMMWXMMMMMNWMMMMNXMMMM00MMMMNNMMMMXNMMMMMXMMMOKkMMM;;|
|.OMMK:cNMMNNMMMMMXMMMMMNNMMMNOONWMMWNMMMMNXMMMMMNWMMNc:XMMx.|
| XMMMKxNMMNXWWWWWXNWWWNXOl;MX;,0W:l0XWWWWNXWWWWWXWMMNxOWMM0 |
| XMMk,MMMMNNMMMMMXMO;'.   lMMdlWMl  .';coXXMMMMMNWMMMW.xMM0 |
|.OMM: xMMMMXMMMMMNN.      lMM:.MM:       oNMMMMMXMMMWo :MMd.|
|::MNd 'kOMMNNMMMMNd       .NM. XX        ;WMMMMNWMMok. dXM,;|
|O XO'o.O KWMNNWWWW;        .X. k.        .NWWWNNMWO O,o.00 O|
|M:;Wl :K dl0MNNMMX     ;;,.;;'            KMMNWMkol.O'.kW':M|
|MW'okoc. ,0 kMWNNx    ;lol.;,.            dNNMMx O. ;xxkc'WM|
|MMN.oc.cl:N' ONWW:    o;,;,...            cWWNk ,Xdd:.oc.NMM|
|MMMN,:k;  ':. xcl;         :;:c.          ,lcd .:. .:O,'XMMM|
|MMMMMd'OXccc;'.do          .:l;dcll;:      dd',:lclNk.oMMMMM|
|MMMMMMX:,xc..,;::;          :,.c:o:',    .;::;,..lx';KMMMMMM|
|MMMMMMMMK;,kKl:odxdol.       .,.;co.  :lodxdo:oKx';KMMMMMMMM|
|MMMMMMMMMMXl,ccc,.  .        .lcdl,   ..  .,cc:'lXMMMMMMMMMM|
|MMMMMMMMMMMMMKo;:o0Nd        .ocl'    xMNOo;;oKMMMMMMMMMMMMM|
|MMMMMMMMMMMMMMMMW0o:'         c:.     .;:oOWMMMMMMMMMMMMMMMM|
|MMMMMMMMMMMMMMMMMMMMMM0o;.        .;o0WMMMMMMMMMMMMMMMMMMMMM|
+------------------------------------------------------------+
                    ANONYMOUS IBEROAMERICA"""
    if __name__ == "__main__":
        print(logo)

def localizar():
    try:
        try:
            argumento = sys.argv[1]
            logo()
            if argumento == "-requisitos":
                requisitos()
        except IndexError:
            ayuda()
    
        try:
            try:
                import urllib3
                import requests
                import json

                url = "http://ipinfo.io/{0}/json".format(str(argumento))

                http = urllib3.PoolManager()

                conexion = http.request("GET", url)

                datos = requests.get(url).json()

                IP=datos['ip']
                org=datos['org']
                city = datos['city']
                country=datos['country']
                region=datos['region']

                print("\nDetalles de {0}\n".format(IP))
                print("Region: {3}\nPais: {2}\nCiudad: {1}\nISP:{0}".format(org, city, country, region))
                
            except KeyError:
                print("Ingresa una IP valida")

            
        except UnboundLocalError:
            os.sys.exit()       
    except KeyboardInterrupt:
        print("\nEl conocimiento es libre\n")

def requisitos():
    os.system("apt-get install python3-pip")
    os.system("pip3 install urllib3")
    os.system("pip3 install request")
    os.system("pip3 install json")

if __name__ == "__main__":
    localizar()

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html= urlopen('http://www.google.com')
    print("Okay")
except HTTPError as e:
    print(e)    
    #Devolve null,executa um break ou algum outro 'Plano B'
except URLError as e:
    print("Servidor ou url não existe")

else:
    #Opcional
    #O programa continua.

#HTTP ERROR
#Se um código de erro HTTP for devolvido.o programa agora exibirá o erro
#E não executará o resto do programa que está na intrução else.

#URL ERROR
#Se o servidor não for encontrado,isso quer dizer que não foi possível acessar
#nenhum servidor.url está incorreta ou servidor fora do ar.
#URLOPEN lançará um URlERROR.

#ATTRIBUTE ERROR
#Tentar acessar uma tag que não existe devolverá objeto none,e resultará no lançamento de um AttributeError.
#Criamos uma função getTittle que devolve o título da pagina,ou um objeto None caso tenha havido algum problema para obtê-lo

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from webbrowser import get
from bs4 import BeautifulSoup

def getTittle(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        tittle =bs.body.h1
    except AttributeError as e:
        return None
    return tittle


tittle= getTittle('http://www.google.com')
if tittle == None:
    print("Title não encontrada")
else:
    print(tittle)

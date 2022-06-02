#pip install bs4

from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('http://www.pythonscraping.com/pages/page1.html')
bs =BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)


A função URLOPEN está sendo importada a função HTML.



READ() é chamada para obter o conteúdo html da página.
È o texto HTML no qual o objeto se baseia.
Além de string de texto,também pode usar diretamente o objeto de arquivo devolvido
por URLOPEN,sem precisar chamar.read():
bs = BeautifulSoup(html,'html.parser')

.parser = especificasr o parser que queremos que o BS4 use para criar esse objeto.
na maioria dos casos,o parser escolhido não fará diferença.
html.parser é um parser incluído no python 3.
Outros: lmxl,html5lib.
  A própria velocidade da rede quase sempre será o principal gargalo.

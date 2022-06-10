from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html.parser')
for child in bs.find('table', {'id': 'giftList'}).descendants:
    print(child


# Capitulo 1 vimos como navegar em arvore em uma única direção:
#Ex: bs.tag.subTag.outraSubTag

# Vamos agora ver como navegar para cima,para os lados e na diagonal em árvores HTML.
    
#.CHILDREN
#Se quiser encontrar somente os descendentes que sejam filhos
#.DESCENDANTS
#Se fôssemos escrevê-lo no lugar de children(),aproximadamente duas dúzias de tags.

          
#IRMÃOS
#next_siblings().
          #Esse código tem como saída todas as linhas de produtos da tabela,exceto a primeira linha 
          #com os títulos.
          #(next) próximos irmãos.
          #Solução: bs.find('table', {'id': 'giftList'}).tr

#previous_siblings().
          #Muitas vezes pode ser útil se houver uma tag facilmente selecionável no final de uma lista de tags
          #irmãs que você queira obter.
 
          #next_subling() e previous_sibling().
           #Devolvem uma única tag,em vez de devolver uma lista delas.
  
          
          
#Pais
#.parents() e .parent()

#É provável que precisará encontrar pais de tags com menos frequência do que
#terá que encontrar seus filhos e irmãos.
#Em geral começamos com tags de nível mais alto e,em seguida,descobrimos como
#descer para outros níveis até alcançar a porção exata de dados que queremos.

#1- A tag imagem com src':'../img/gifts/img1.jpg é inicialmente selecionada.
#2- Selecionamos o pai dessa tag(nesse caso,é a tag TD)
#3- Selecionamos a previous_sibling da tag TD(nesse caso é a tag TD que contém o
# valor do produto em dólar.)
#4- selecionamos o texto nessa tag: "R$15,00".
          
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html.parser')
#for child in bs.find('table', {'id': 'giftList'}).children:
for child in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(child)

          
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.find('img',{'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())



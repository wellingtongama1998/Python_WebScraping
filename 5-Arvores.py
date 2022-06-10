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
          #Solução: for child in bs.find('table', {'id': 'giftList'}).tr:

#previous_siblings().
          #Muitas vezes pode ser útil se houver uma tag facilmente selecionável no final de uma lista de tags
          #irmãs que você queira obter.
 
          #next_subling() e previous_sibling().
           #Devolvem uma única tag,em vez de devolver uma lista delas.
          
          
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html.parser')
#for child in bs.find('table', {'id': 'giftList'}).children:
for child in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(child)

          

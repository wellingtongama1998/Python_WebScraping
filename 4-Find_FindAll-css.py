from urllib.request import urlopen
from bs4 import BeautifulSoup


html=urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs= BeautifulSoup(html.read(),'html.parser')
namelist =bs.findAll('span',{'class':'green'})
for name in namelist:
    print(name)
    

#CLASS GREEN    
#Praticamente todo site que você encontrar conterá folhas de estilo.
#O surgimento do css foi extremamente vantajoso para os web scrapers.
#web scrapers podem separar facilmente essas tags de acordo com a classe;Ex obetr todos os textos vermelhos,mas não os textos em vermelhos.

#Como o CSS depende desses atributos de identificação para estilizar adequadamente os site,é quase certo que esses atributos de classe ID
#sejam abundantes na maioria dos sites modernos.

#GET_TEXT()
#Remove todas as tags do documento com o qual você está trabalhando e devolve uma string Unicode contendo somente o texto.
#Ex:Se você estiver trabalhando com um bloco de texto grande,contendo muitos hyperlinks,parágrafos e outras tags,tudo isso será removido,
#e estará um de texto sem tags.
#É muito mais fácil encontrar o que você procura em um objeto BeautifulSoup do que em um bloco de texto.
#Chamar .get_text() deve ser sempre a sua última tarefa,imediatamente antes de exibir,armazenar ou manipular os dados finais.
#Em geral,você deve se esforçar ao máximo para tentar preservar a estrutura de tags de um documento.

#FIND() FINDALL()
#Duas funções do BeautifulSoup que provavelmente serão mais usadas.
#find_all(tag, attributes, recursive, text, limit, keywords)
#find(tag, attributes, recursive, text, keywords)
#É bem provavel que,em 95% do tempo,somente os dois primeiros argumwentos serão necessarios: tag e attributes.
#TAG
#ex: .find_all(['h1','h2','h3','h4','h5','h6']) nome de uma tag como string,ou até mesmo uma lista python de nomes de tags definidos como strings.

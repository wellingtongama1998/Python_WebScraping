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
# nome de uma tag como string,ou até mesmo uma lista python de nomes de tags definidos como strings.
#ex: .find_all(['h1','h2','h3','h4','h5','h6'])

#ATTRIBUTES
#Aceita um dicionario python de atributos e faz a correspondência com tags que contenham qualquer um desses atributos.
#ex: .find_all('span',{'class':{'green','red'}})

#TEXT
#É peculiar por fazer a correspondência com base no conteúdo textual das tags.
#Se quiser encontrar o número de vezes que "the prince" está cercado por tags na página.
#Ex: nameList = bs.find_all(text='the prince')
#    print(len(namelist))

#LIMIT
#É usado somente no método FIND_ALL com um limite igual a 1.
#Esse parâmetro pode ser definido se você estiver apenas em obter os primeiros x itens da página.

#KEYWORD
#Permite selecionar tags que contenham um atributo ou um conjunto de atributos específicos.
#EX: title= bs.find_all(id='title',class_='text')
#Devolve a primeira tag com a palavra "text" no atributo class_ e "title" no atributo id.
#Uma linha como essa talvez não seja particulamente útil,e deveria ser equivalente a:
# title= bs.find(id='title')

#AGUMENTOS NOMEADOS E "CLASS"
#O argumento keyword pode ser útil em algumas situações,etretanto,ele é tecnicamente redundante como um recurso
#do BeautifulSoup.
#Tenha em mente que tudo que puder ser feito com keyword também poderá ser feito com técnicas discutidas
#mais adiante com "expressões regulares" e "Expressões lambda"

#Você pode deparar com problemas ao usar KEYWORD, se estiver procurando atributo CLASS,pois CLASS é uma palavra
#reservada protegida em Python,ou seja,ela não pode ser usada como uma variável ou como nome de argumento
#Soulução: como alterniva ,CLASS pode ser usada entre aspas:
           #bs.find_all('', {'class':'green'})
#Se tivermos uma lista de tags longa,poderemos acabar com muita informação indesejada.
#O argumento KEYWORD permite acrescentar um filtro 'e'.

#
         



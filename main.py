# coding: utf-8
def cookies(cool):
    sleep(1)
    cool.find_element_by_id('cookie-notice-ok-button').click()

#import dw as dw
from selenium import webdriver                   #Webdriver navegador
from time import sleep                           
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select #Blioteca select



##CONTAS##
conta1="wellingtongama2010@hotmail.com"

##CONTAS##

#INICIO SELECIONAR CONTA
resp = "N"
while resp.upper() == "N":

    print("ANUNCIO JOGOS DE PS3 EM MIDIA DIGITAL\n"
          "Selecione a conta: ")
    print("CONTA: [1]",conta1)
    print()
    sconta=int(input("SELECIONE A CONTA: "))
    preco=float(input("Qual o preço ? R$"))
    print()
    print('conta:',conta1)
    print('Preço R$',preco)
    print("Deseja continuar ? ")

    resp =input("Tecle [N] para NÃO / qualquer caractere para SIM: ")
#INICIO SELECIONAR CONTA


##TITULO E DESCRIÇÂO##
##INPUT
titulo=("Jogos de PS3 originais")
descricao=(""""
Jogos Originais  para PS3

Os jogos ficam armazenado no seu ps3

Dúvidas ?.
-Chama no CHAT
WhatsApp:(82)98712-5149
""")
##TITULO E DESCRIÇÂO##
##INPUT

#Selenium


#nav=webdriver.Chrome(executable_path="C:\Users\welli\Downloads\chromedriver.exe")
nav =webdriver.Chrome() #Inicio Brower
nav.maximize_window()
nav.get('https://conta.olx.com.br/acesso?returnToToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJodHRwczovL2NvbnRhLm9seC5jb20uYnIvYW51bmNpb3MiLCJpYXQiOjE2NDA4MjUzMzA5NDN9.r9T7eenM4PAI0LeskAtDo_v8fY7hXoVm_cAZ3ALUxss')

#Cookies aceitar
cookies(nav)

if sconta==1:
    ##LOGIN##
    #E-mail
    nav.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/form/div[1]/div[2]/input').send_keys('wellingtongama2010@hotmail.com')
    #Senha
    nav.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/form/div[2]/div[2]/div/div/input').send_keys('######')
    #Submit
    nav.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/form/button').click()
    sleep(5)
    ##LOGIN##
else:
    pass


#Entrar no Formulario do Anuncio
nav.get('https://www2.olx.com.br/desapega')
sleep(3)

##ANUNCIO##
#Titulo Anuncio
nav.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div/div[1]/div[1]/div[1]/input').send_keys(titulo)
sleep(0.5)
#Descrição
nav.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div/div[1]/div[1]/div[2]/textarea').send_keys(descricao)
sleep(0.5)

#Categoria do anuncio
nav.find_element_by_link_text('Eletrônicos e celulares').click()
#Subcategoria
nav.find_element_by_link_text('Videogames').click()

#Tipo
#Select
sleep(0.5)
select = Select(nav.find_element_by_name('videogame_type'))
select.select_by_visible_text("Jogos")
#Modelo
select = Select(nav.find_element_by_name('videogame_model'))
select.select_by_visible_text('Playstation 3')

#Preço
nav.find_element_by_id('price').send_keys(preco)
#Upload imagem
nav.find_element_by_class_name('box__field').send_keys('C:\img\imagem1.jpg')
nav.find_element_by_class_name('box__field').send_keys('C:\img\imagem2.jpg')
nav.find_element_by_class_name('box__field').send_keys('C:\img\imagem3.jpg')
nav.find_element_by_class_name('box__field').send_keys('C:\img\imagem4.jpg')
nav.find_element_by_class_name('box__field').send_keys('C:\img\imagem5.jpg')
nav.find_element_by_class_name('box__field').send_keys('C:\img\imagem6.jpg')


#Mostar número de telefone ?
###BeautifulSoup###

#.page_source
#Tira um print dela tirando o html dela
page_content = nav.page_source
#Transferir para BeautifulSoup
sleep(1)
site = BeautifulSoup(page_content, 'html.parser')
sleep(1)
###BeautifulSoup###

#Mostar número de telefone ?

numero=site.find('div',attrs={'class','user-info__phone'})
tel=numero.text.split(' ')
print("Ocultar este número ?")
print("(82)",tel[1],tel[2])
mostrarnumero=str(input('[S] /[N]: ')).upper()
if mostrarnumero =='S':
    nav.find_element_by_id('phone_hidden').click()
else:
    pass

#Mostar número de telefone ?

nav.find_element_by_id('ad_insertion_submit_button').click()
sleep(2)
#nav.find_element_by_partial_link_text('Desativar OLX Pay').click()

import requests
#Código de Status
#Cabecalho
#Conteúdo

response = requests.get('https://rpcs3.net')

print("Status code: ", response.status_code)
print(" HEADER ")
print(response.headers)

print()
print()
#print("CONTENT")
#print(response.content)

#OU

from urllib.request import urlopen

html = urlopen('https://google.com')
print(html.read())

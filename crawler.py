import requests
from bs4 import BeautifulSoup

page = requests.get("https://eproc.trf2.jus.br/eproc/externo_controlador.php?acao=processo_consulta_publica")

site = BeautifulSoup(page.content, 'html.parser')

consultas = site.find_all('div', attrs={'id' :'divInfraAreaDados'})

print(consultas)
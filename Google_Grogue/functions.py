import streamlit as st
from bs4 import BeautifulSoup
from multiprocessing import Queue
from urllib.request import Request, urlopen
import random
import re
import pytest



class ScrawlingGrogue:
    def scrawlinglist(list_url):
        try:
            for url in list_url:
                try:
                    req  = Request(url)
                    html_page = urlopen(req)
                    soup = BeautifulSoup(html_page, "html.parser")
                except:
                    continue
                else:
                    links = []
                    for link in soup.findAll('a'):
                        links.append(link.get('href'))
                final = []
                for link in links:
                    try:
                        if re.findall("^https", link):
                            final.append(link)
                    except:
                        continue
                return final
        except:
            return []
        else:
            return []
            
    def recommendation(lista):
        end_list = random.choices(lista, k=20)
        fila = Queue()
        [fila.put(n) for n in end_list]
        while not fila.empty():
            try:
                req = Request(fila.get())
                page_request = urlopen(req)
                pg = BeautifulSoup(page_request, "html.parser").find('title')
                st.write(f'Titulo da página : {pg.text}')
                st.write(f'Link da página : {fila.get()}')
                st.write('---'*9)
                pass
            except:
                st.write('Titulo da página não encontrado!')
                st.write(f'Link da página : {fila.get()}')
                st.write('---'*9)
                pass

    def descproject():
        st.markdown('# Google Grogue ')
        st.write("   *Projeto Final do Curso: PYTHON PRO - MENTORAMA*")
        st.image("https://voxnews.com.br/wp-content/uploads/2021/04/logomarca_mentorama-741x394.png", width=700)
        st.markdown(""" 
            ##### 

            *Esta aplicação, projeto, realiza a busca de todas as urls na página web desejada.
            Assim, obtendo mais urls dentro da lista de urls já obtidas, tendo essa operação repetida em 5 vezes.
            Dessa forma, é obtido uma lista final, aonde é recomendado 10 links de forma aleatoria.*
        """)
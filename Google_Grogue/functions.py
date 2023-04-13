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
        st.image("https://voxnews.com.br/wp-content/uploads/2021/04/logomarca_mentorama-741x394.png", width=700)
        st.markdown(""" 
            - *Desenvolvimento de uma interface web onde o usuário possa informar uma URL*
            - *Desenvolvimento de um Crawler que, à partir desta primeira URL, seja capaz de identificar todos os links dentro da página e acessar cada um deles*
            - *Para cada link acessado, deve se repetir o processo, acessando o link e identificando todas as URLs contidas nele para serem acessadas* 
            - *Este processo deve se repetir até, pelo menos, 5 níveis*
            - *Implementação de um algoritmo para ordenar os dez resultados mais relevantes*
        """)
        st.markdown('Acomoanhe a contrução do projeto, do início, em meu GitHub')
        st.write('https://github.com/GaabrielCoosta/Google_Grogue')

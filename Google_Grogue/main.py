import streamlit as st 
from functions import ScrawlingGrogue
import pytest 


st.set_page_config(
    page_title="Google Grogue",
    page_icon=":lupa",
    layout="centered",
    initial_sidebar_state="expanded"
)

def main_page():
    st.markdown("# Google Grogue :mag_right:")
    st.write('')
    st.image("https://media.giphy.com/media/cWVlY0EeQZOrm/giphy.gif", width=600)
    st.write("""
    Developed by Gabriel Andrade
    """)
    st.write('https://github.com/GaabrielCoosta/Google_Grogue')

def desc_project():
    ScrawlingGrogue.descproject()

def source_url():
    st.markdown('# Google Grogue 🔎')
    st.write('')
    try:
        url = st.text_input('Digite uma URL para buscar:  ')
    except:
        st.error('Digite uma URL valida')
    else:
        try:
            data_1 = ScrawlingGrogue.scrawlinglist([url])
            data_2 = ScrawlingGrogue.scrawlinglist(data_1)
            data_3 = ScrawlingGrogue.scrawlinglist(data_2)
            data_4 = ScrawlingGrogue.scrawlinglist(data_3)
            data_5 = ScrawlingGrogue.scrawlinglist(data_4)
            data_6 = ScrawlingGrogue.scrawlinglist(data_5)
            if type(data_1) is None:
                data_1 = [url]
            if type(data_2) is None:
                data_2 = [url]
            if type(data_3) is None:
                data_3 = [url]
            if type(data_4) is None:
                data_4 = [url]
            if type(data_5) is None:
                data_5 = [url]
            if type(data_6) is None:
                data_6 = [url]
            end = data_1 + data_2 + data_3 + data_4 + data_5 + data_6
            ScrawlingGrogue.recommendation(end)
        except:
            st.error('Digite uma URL valida!')

pages = {"Pagina Inicial": main_page, "Descrição do Projeto": desc_project, "Buscar URL": source_url}

selected_page = st.sidebar.selectbox("Selecione a pagina!", pages.keys())
pages[selected_page]()

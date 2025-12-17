import streamlit as st

st.title("Site teste da Escola de Programação - By Luiz Gabriel")

# titulo
st.header("Bem-vindo!")

st.subheader("1ª Seção")
st.write("Conteúdo da 1ª seção")

st.subheader("2ª Seção")
st.write("Conteúdo da 2ª seção")

# textos em markdown
st.markdown("""---""")
st.markdown("# Titulo em markdown")
st.markdown("Conteúdo em **markdown**")

st.markdown("""
            Lista de tarefas:
            1. Primeiro passo
            2. Segundo passo
            """)

# usando html 
st.markdown("### HTML")

html_code = """
    <h1 style = 'color: blue;'> Esse é um cabeçalho azul </h1>
    <p style = 'color: purple;'> Esse é um parágrafo </p>
"""

st.markdown(html_code, unsafe_allow_html= True)

import streamlit as st

st.set_page_config(layout="wide", page_title= "Tutorial de Formulário")

st.title("Techschool 2025 - Tutorial Streamlit - Formulário")

st.header("Preencha o formulário abaixo")

st.markdown("""--- """)

nome = st.text_input("Informe seu nome:", placeholder= "Preencha com o seu nome")

idade = st.number_input("Informe sua idade:",  min_value=8, max_value=18, step = 1)

data_de_nascimento = st.date_input("Data de nascimento:", format= "DD/MM/YYYY")

hora_atual= st.time_input("Selecione a hora", step = 60)

cor_perfil = st.color_picker("Selecione a cor do perfil:")

html_code = """
    <h1 style='color: {}'> Essa é a cor que você escolheu para o seu perfil</h1>
""".format(cor_perfil)

st.write("Nome: ", nome)


st.markdown(html_code, unsafe_allow_html= True)


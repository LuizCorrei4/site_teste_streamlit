import streamlit as st

st.set_page_config(layout="wide", page_title= "Tutorial de Formulário")

st.title("Techschool 2025 - Tutorial Streamlit - Formulário")

st.header("Preencha o formulário abaixo")

st.markdown("""--- """)

with st.form("formCadastro"):
    nome = st.text_input("Informe seu nome:", placeholder= "Preencha com o seu nome")

    idade = st.number_input("Informe sua idade:",  min_value=8, max_value=18, step = 1)

    data_de_nascimento = st.date_input("Data de nascimento:", format= "DD/MM/YYYY")

    hora_atual= st.time_input("Selecione a hora", step = 60)

    cor_perfil = st.color_picker("Selecione a cor do perfil:")

    btnFormCadastro = st.form_submit_button("Cadastrar")

    if btnFormCadastro:
        if not nome:
            st.error("Preencha o nome!")
        elif len(nome) <=3:
            st.error("O nome precisa ter pelo menos 3 letras")
        else:
            st.write("Nome: ", nome)
            st.write("Idade: ", idade)
            st.write("Data de Nascimento: ", data_de_nascimento)
            st.write("Hora Atual: ", hora_atual)


html_code = """
    <h1 style='color: {}'> Essa é a cor que você escolheu para o seu perfil</h1>
""".format(cor_perfil)



st.markdown(html_code, unsafe_allow_html= True)


import streamlit as st 
# from streamlit_option_menu import option_menu

st.title("Tutorial de Imagens")
st.image("img/img_3_meninas.jpeg")

# colocando imagens na mesma linha
colunas = st.columns(3)

colunas[0] = st.image("img/like_insta.jpeg")
colunas[1] = st.image("img/like_insta.jpeg")
colunas[2] = st.image("img/like_insta.jpeg")

st.file_uploader("Escolha uma imagem", type = ["jpg", "jpeg", "gif", "png"])

"""

# CORREÇÃO 1: Atribuímos o menu a uma variável chamada 'tipo_de_menu'.
tipo_de_menu = option_menu(
    menu_title="Para participar de nosso site logue ou se cadastre!",
    options=["Logar", "Cadastrar"], 
    icons=["house", "envelope"],
    menu_icon="alien",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#FAF2F2"},
        "icon": {"color": "blue", "font-size": "25px"},
        "nav-link": {
            "font-size": "25px",
            "text-align": "left",
            "margin": "0px",
            "color": "black"
        },
        "nav-link-selected": {"background-color": "#CACBFC"}
    }
)

# CORREÇÃO 2: Verificamos a variável 'tipo_de_menu' e usamos "Logar" com L maiúsculo (antes estava l minúsculo, o que não condiz com options dentro da função "option_menu")
if tipo_de_menu == "Logar":
    with st.form("formlogar"):
        nome = st.text_input("Nome:", placeholder="Informe seu nome...")
        Usuario = st.text_input("Usuario:", placeholder="Informe seu usuario...")
        btnLogarUsuario = st.form_submit_button("Logar", use_container_width=True)

    if btnLogarUsuario:
        st.success("Voce clicou no botão de logar")

# CORREÇÃO 3: Verificamos a variável 'tipo_de_menu' aqui também mas para a opção de Cadastrar
if tipo_de_menu == "Cadastrar":
    with st.form("formfirebase"):
        nome = st.text_input("Nome :", placeholder="infome seu nome...")
        apelido = st.text_input("Apelido:", placeholder="Informe seu apelido...")
        idade = st.number_input("Idade:", step=1, min_value=8, max_value=100)
        email = st.text_input("Email:", placeholder="Informe seu email...", type="password")
        btncadastrar = st.form_submit_button("Cadastrar", use_container_width=True)

    if btncadastrar:
        st.success("Você escolheu se cadastrar")


        """
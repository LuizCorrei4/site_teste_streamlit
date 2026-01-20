import streamlit as st 
# from streamlit_option_menu import option_menu

st.title("Tutorial de Imagens")
st.image("img/img_3_meninas.jpeg")

# colocando imagens na mesma linha
colunas = st.columns(3)

colunas[0] = st.image("img/like_insta.jpeg")

st.file_uploader("Escolha uma imagem", type = ["jpg", "jpeg", "gif", "png"])
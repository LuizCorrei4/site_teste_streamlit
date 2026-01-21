import requests 
import streamlit as st
from streamlit_lottie import st_lottie 

def carregar_animacao(url: str):
    requisicao = requests.get(url)
    if requisicao.status_code != 200:
        return None
    return requisicao.json()

url_animacao = "https://lottie.host/bc1a4201-796b-415f-83f6-0c6d00eef264/eAW1cOrMIu.json"

animacaoChat = carregar_animacao(url_animacao)

st_lottie(animacaoChat, key= "animacaoChat")


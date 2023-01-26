import streamlit as st

# Criando uma função para o login
def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Entrar"):
        if username == "admin" and password == "admin":
            st.success("Login realizado com sucesso!")
        else:
            st.error("Usuário ou senha inválidos")

# Adicionando a função no layout da página
st.set_page_config(page_title="Plataforma de Login", page_icon=":guardsman:", layout="wide")
login()


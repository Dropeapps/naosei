import streamlit as st
import hashlib

login = st.text_input("Insira o login")
senha = st.text_input("Insira a senha", type='password')
cadastrar = st.button("Cadastrar")

def criptografar(senha):
    senha_criptografada = hashlib.sha256(senha.encode()).hexdigest()
    return senha_criptografada

if cadastrar:
    senha_criptografada = criptografar(senha)
    usuarios = {}
    usuarios[login] = senha_criptografada
    st.success("Usuário cadastrado com sucesso!")

login_entrar = st.text_input("Insira o login")
senha_entrar = st.text_input("Insira a senha", type='password')
entrar = st.button("Entrar")

if entrar:
    senha_digitada = criptografar(senha_entrar)
    if login_entrar in usuarios and usuarios[login_entrar] == senha_digitada:
        st.success("Login realizado com sucesso!")
    else:



import random
import streamlit as st
import pandas as pd
import numpy as np
import csv as cv


st.title("Formulário de Inscrição de alunos")
dados_de_alunos=[]
novo_aluno=[]
Nomes=[]
Moradas=[]
Numeros=[]
Contactos=[]
numero = random.randint(1, 1000)
def PesquisaB(numero):

    if numero in Pesquisa:
        st.title("Resultado da Pesquisa")
        st.title('Numero:',Numero)
        st.title('Nome',Nome)




Pesquisa = st.sidebar.text_input("Pesquisa por numero de Aluno")
button = st.sidebar.button("Pesquise Por Nome de Aluno", on_click=PesquisaB, args=(numero))

menu = ["Menu", "Pesquisa" ,"Academia", "Image",]
choice = st.selectbox("Selecione uma Opção", menu)

def menu():



    if choice == "Menu":
        st.header("Dados Pessoais")

        col1, col2 = st.columns(2)
        with col1:
            st.header("Número de Aluno")
        with col2:
            st.header(numero)
        Nome = st.text_input("Nome Completo")
        Nomes.append(Nome)
        st.write(Nome)



        Morada = st.text_input("Morada")
        st.text(Morada)
        Contacto = st.text_input("Contacto")
        Contactos.append(Contacto)
        col1, col2 = st.columns(2)
        with col1:
            turma = st.multiselect(label=("Selecione uma Disciplina"),options=["Ciências da Vida","Código Digital","Ciências Fisico Quimicas"])
        with col2:
            Idade = st.text_input("Idade")
        numeroaluno = st.header(numero)
        Numeros.append(numeroaluno)
        Button = st.button("Adicionar aluno", key='add')
        if Button == True:
            novo_aluno = ({"Número": [Numeros], "Nome": [Nome], "Morada": [Morada], "Contacto": [Contacto]})
            dados_de_alunos.append(novo_aluno)

            df = pd.DataFrame(dados_de_alunos, columns=["Numero", "Nome", "Morada"])

            df.to_csv("Lista_de_Alunos2.csv", sep=",")
            st.success("Aluno Adicionado com Sucesso")

        else:
            data = [{'Numero': [numero], 'Aluno': [Nomes], 'Morada': [Morada],}]
            df2 = pd.DataFrame(data={'Numero': [numero], 'Aluno': [Nomes], 'Morada': [Morada],})
            # Alteração de Teste na Criação do CSV

            df.append(df2)
            df.to_csv("Lista_de_Alunos2.csv", sep=";")
            st.dataframe(df, width=700)

        articles = pd.read_csv('Lista_de_Alunos.csv' ,sep=",")
        st.dataframe(articles, width=700)

    if choice == "Pesquisa":
        Pesquisa = st.text_input("Pesquisa por numero de Aluno", key="submit")
        clicked = st.button("Pesquise Por Nome de Aluno", args=(numero), key="Submit2")
        df = pd.read_csv('Lista_de_Alunos.csv', sep=",")
        #st.dataframe(articles, width=700)
        if clicked == True:
            for Pesquisa in Numeros:
                    st.title("Resultado da Pesquisa")
                    st.title(Nomes, Numero, Morada)
            df = pd.read_csv('Lista_de_Alunos.csv', sep=",")
            st.dataframe(df, width=700)



    if choice == "Academia":
        soma = 0
        Lista = [11, 16, 19, 18]
        num = 0
        st.header("Percurso Académico")
        Disciplina1 = st.multiselect(label=("Selecione uma Disciplina"),options=["Matemática", "Turma de Engenharia","Ciências da Vida","Código Digital","Ciências Fisico Quimicas"])
        st.write(Disciplina1)

        Notas = st.number_input("Introduza a Avaliação", min_value=5)

        for notas in Lista:
            soma += notas/ len(Lista)

        for notas in Lista:

            st.write(" Aprovado ", notas)

        if soma >= 15:
            st.write(" Aprovado com aproveitamento nota:", soma)
        else:
            st.write(" Aprovado ", soma )

    if choice == "Image":
        st.image("/Users/paulomonteiro/PycharmProjects/Formulário_Alunos/button2.png")
        st.markdown('<a name="menu"></a>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            # uploader de imagem
            st.header('Upload da imagem')
            uploaded_file = st.file_uploader("Escolha uma imagem...", type=["jpg", "jpeg", "png", "csv", "GIF", "gif"])

        with col2:
            st.header('Fotografia do Aluno')
            st.image(uploaded_file)

        if uploaded_file is True:
                # carregando a imagem
                img = st.image.load_img(uploaded_file, target_size=(125, 125))

                # exibindo a imagem
                st.image(img, caption='Imagem carregada', use_column_width=True)
#def option_menu(choice):

    #if choice == "menu":
            #st.text("Deseja adicionar ao carrinho")
            #st.number_input("Introduza Quantidade")



        if st.button("Adicionar ao carrinho"):
            st.markdown("[ir para secção](#menu)")
        html = f"<a href='{menu}'><img src='data:/Users/paulomonteiro/PycharmProjects/Formulário_Alunos/button2.png/png;base64,{choice == Menu}'></a>"
        st.markdown(html, unsafe_allow_html=True)

menu()

        # pré-processamento da imagem
        #x = image.img_to_array(img)
        #x = np.expand_dims(x, axis=0)
        #x = preprocess_input(x)


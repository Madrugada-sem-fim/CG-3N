import streamlit as st
import pandas as pd                 # CRIAÇÃO DA DATAFRAMES (TABELAS)
import numpy as np                  # OPERAÇÕES ALGÉBRICAS
from st_aggrid import AgGrid
from random import random
#import math as mt                   # FUNÇÕES MATEMÁTICAS
#import statistics as stt             # Importantes sobre médias, medianas, desvio padrao https://www.youtube.com/watch?v=Ztft4ggLPdg
#from typing import Type             # Plotar resultados com o grafico deitado
#import altair as alt                #plotar graficos mais simples
import seaborn as sns             # Apresentação de um grafico com mapa de calor
import matplotlib.pyplot as plt   # Plotar o resultado em gráficos 
#import plotly.express as px       # Plotar o resultado em grafico como o matplotlib
#import graphviz as graphviz        # Fluxo na forma de Grafo
import io
from scipy.stats import norm
#from scipy import stats


st.set_page_config(page_title="CRITIC-GRA-3N (CG-3N)",page_icon="inicio_site.png",layout="centered")
with open("escondendo o nome streamlit.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)

#with open("teste_botao.css") as f:
#    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)
# st.markdown("<h1 style = 'text-align: center;'>web Scraper</h1>", unsafe_allow_html=True)


#st.graphviz_chart('''
#    digraph {
#        Big_shark -> Tuna
#        Tuna -> Mackerel
#        Mackerel -> Small_fishes
#        Small_fishes -> Shrimp
#    }
#''')


def set_bg_hack_url():
#    '''
#    A function to unpack an image from url and set as bg.
#    Returns
#    -------
#    The background.
#    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://i.ibb.co/SdGtNMp/CRITIC-GRA-3-N-site-1700-800-px-11.png");
             
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
#https://media.istockphoto.com/vectors/vector-abstract-technology-innovation-clean-design-background-vector-id477203456?k=6&m=477203456&s=170667a&w=0&h=50PEVTWD6elGqLRjGm1nb74tEjkx2pP-MwgB9b5RRvQ=
set_bg_hack_url()


st.sidebar.image('critic-gra-3n.jpeg', use_column_width = 'always')
st.image('2critic-gra-3n.jpeg', use_column_width = 'always')

st.sidebar.markdown('# :house: **Menu**')
paginas = ['Home', 'Cálculo', 'Sobre', 'Autores']
pagina = st.sidebar.selectbox('Escolha uma página:', paginas, key='lista_paginas')

if 'numero_alternativa' not in st.session_state: st.session_state['numero_alternativa']= 0       #Colocado pelo LORRAN =-=-=-=-=-=-=-=-=- 
if 'numero_criterio' not in st.session_state: st.session_state['numero_criterio'] = 0
if 'coeficiente' not in st.session_state: st.session_state['coeficiente'] = 0
if 'botao_inclusao_da_matriz' not in st.session_state: st.session_state['botao_inclusao_da_matriz'] = 0
if 'nome_trabalho' not in st.session_state: st.session_state['nome_trabalho'] = 0
if 'inicio_calculo' not in st.session_state: st.session_state['inicio_calculo'] = 0

st.sidebar.write('')
st.sidebar.write('')
st.sidebar.markdown("**Para mais métodos e softwares acesse:** ")
st.sidebar.markdown("'Casa da Pesquisa Operacional' - [Youtube](https://www.youtube.com/c/CasadaPesquisaOperacional)")
st.sidebar.image('Casa da Pesquisa.jpeg', caption='Casa da Pesquisa Operacional')


if pagina == 'Home':
    st.markdown('## Bem vindo ao software *Gratuito* para apoio a tomada de decisão CRITIC-GRA-3N. ')
    '''

    #### O Site foi desenvolvido para que possa auxiliar o tomador de decisão de uma forma simples, contudo poderosa, além de totalmente gratuita.
       
    ##### Buscamos cumprir com os seguintes tópicos: 
    - Ser uma ferramenta online ~~PAGA~~ Totalmente Gratuita
    - Ser um site totalmente intuitivo
    - Simplicidade ao incluir os dados
    - Apresentação detalhada dos resultados
    

    #### Para que possa iniciar a inclusão dos seus dados e realizar os calculos para o seu problema entre na página "Cálculo" a esquerda.

    '''
  
if pagina == 'Cálculo':
    '''### Você precisará entrar com os dados desejados de seu problema para que se possa obter um resultado.'''
    st.markdown('#### Para iniciar os calculos, inclua o nome que será utilizado para o seu Trabalho:')
    with st.form(key="inicio"):
        trabalho = st.text_input('Nome do Trabalho:')
        botao_iniciar = st.form_submit_button('Iniciar')
    if botao_iniciar:
        st.session_state.nome_trabalho = trabalho
    if st.session_state.nome_trabalho != 0:
        st.success(f'O nome escolhido para o trabalho foi: {st.session_state.nome_trabalho}')
      
    st.write('')  
    st.markdown("<h3 style = 'text-align: center;'>Insira o número de Alternativas do problema e os seus respectivos nomes:</h3>", unsafe_allow_html=True)
    lista_alternativas = []
    col1, col2 =st.columns([1,3])
    #st.session_state['numero_alternativa']=[]
    #numero_alternativa = 0
    with col1:
        with st.form(key = 'Form1'):
            n_alternativas = st.number_input('Numero de Alternativas:', 2, 100, step=1, key=0)
            botao_alternativa = st.form_submit_button('Confirmar o número de Alternativas.')
            if botao_alternativa:
                #numero_alternativa = 1
                st.session_state.numero_alternativa += 1
    if st.session_state.numero_alternativa == 0:
        st.write('')
    else:                           
        with col2:
            i=1
            for a in range(n_alternativas):
                #i=1
                alternativa = st.text_input(f'Adicione o nome da Alternativa A{i}: ', key = i)
                i+=1
                lista_alternativas.append(alternativa)
            #st.write(lista_alternativas)
    #st.write(n_alternativas)
    
    #n_alternativas = 10                  # retirar isso aqui  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    #lista_alternativas = ['a1','a2','a3','a4','a5','a6','a7','a8','a9','a10']    # retirar isso aqui  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    #st.write(n_alternativas)                # retirar isso aqui  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    #st.write(lista_alternativas)             # retirar isso aqui  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    st.write('')
    st.write('')

    if st.session_state.numero_alternativa == 0:
        st.write('')
    else:
        st.markdown("<h3 style = 'text-align: center;'>Nesse momento será necessário incluir três itens:</h3>", unsafe_allow_html=True)
        '''
        - 1 - O número de Critérios do problema;
        - 2 - Seus respectivos nomes; e
        - 3 - Informar se o Critério é monotónico de Custo (C) ou monotónico de Lucro (L).
        '''

        #Obs.:
        #      Critério monotônico de Custo = Quanto maior for o valor, pior será para Alternativa.
        #      Critério monotônico de Lucro = Quanto maior for o valor, melhor será para Alternativa.'''
        st.write('Obs.:') 
        st.write('Critério monotônico de Custo = Quanto maior for o valor, pior será para Alternativa.') 
        st.write('Critério monotônico de Lucro = Quanto maior for o valor, melhor será para Alternativa.') 
        st.write('Os nomes dos Critérios deverão ser distintos.')
        st.write('')
        lista_criterios = []
        id_criterio = []
        col1, col2 = st.columns([1,3])
    #numero_criterio = 0
    if st.session_state.numero_alternativa == 0:
        st.write('')
    else:
        with col1:
                with st.form(key = 'Form2'):
                    n_criterios = st.number_input('Numero de Critérios:', 2, 100, step=1, key=0)
                    botao_criterio = st.form_submit_button('Confirmar o número de Critérios.')
                    if botao_criterio:
                        #numero_criterio = 1
                        st.session_state.numero_criterio += 1
    if st.session_state.numero_criterio == 0:
        st.write('')
    else:
        with col2:
            y=1
            for a in range(n_criterios):
                criterios = st.text_input(f'Adicione o nome do Critério C{y}: ', key = {y+100})
                ID = st.text_input(f'Informar se o Critério C{y} é Monotônico de Lucro (L) ou Custo (C): ', 
                                    key = {y+200}, 
                                    max_chars = 1, 
                                    help = 'Escolha "L" ou "C".', 
                                    placeholder ='L ou C' ).upper()
                if ID not in 'LClc':
                    st.error('Entre com a Letra "L" para Lucro ou "C" para Custo !!!')
                #while ID not in 'LC':
                #    st.error('Entre com a Letra "L" para Lucro ou "C" para Custo !!! ')
                #    ID = st.text_input(f'Informar se o Critério C{y} é Monotônico de Lucro (L) ou Custo (C): ', key = {y+200}).upper()
                y+=1
                lista_criterios.append(criterios)
                id_criterio.append(ID)
            #st.write(lista_criterios)
            #st.write(id_criterio)
        st.session_state.coeficiente = 1
        #lista_criterios = ['c1','c2','c3','c4','c5','c6']      # retirar isso aqui  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        #n_criterios = 6                     # retirar isso aqui  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        #id_criterio = ['C','C','C','L','L','L']            # retirar isso aqui  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        #st.write(lista_criterios)
        #st.write(id_criterio)
        #st.write(n_criterios)
    
    if st.session_state.coeficiente == 1:
        st.markdown("<h3 style = 'text-align: center;'>Coeficiente de Distinção</h3>", unsafe_allow_html=True)
        with st.form(key = 'Form3'):
                coeficiente_dist = st.slider('Insira o Valor do Coeficiente de Distinção:', 
                                            min_value=0.10, 
                                            max_value=1.00, 
                                            value=0.87, 
                                            step=0.01, key=0)
                '''
                #### OBS.:
                - O Coeficiente de Distinção tem por objetivo controlar o afastamento entre os valores das Alternativas ao final do processo.
                - Quanto maior o valor do Coeficiente de Distinção, maior será a distancia entre os valores das Alternativas.
                - Valor sugerido para o Coeficiente de Distinção é de 0.87
            '''
                botao_coeficiente = st.form_submit_button('Confirmar o valor do Coeficiente de Distinção.')
                if botao_coeficiente:
                    st.session_state.botao_inclusao_da_matriz = 1
        

        #df2 = st.dataframe(np.zeros((n_alternativas,n_criterios)))                                # um teste para travar o programa e nao permitir ele rodar ate o usuario apertar o botao_inclusao_matriz
        if st.session_state.botao_inclusao_da_matriz == 1:      #lista_criterios[-1] is not "":                               #verificar se é "" ou None
            st.write('A matriz de decisão é:')
            matrix = np.zeros((n_alternativas,n_criterios))
            df = pd.DataFrame(matrix,index = lista_alternativas,columns=lista_criterios)
            #st.session_state.store_d = df.to_dict()     # esse aqui foi do LORRAN  =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            st.dataframe(data=df)
            
            with st.form(key = 'Form4'):
                st.markdown("<h3 style = 'text-align: center;'>Inserção dos Valores</h3>", unsafe_allow_html=True)
                
                '''
                - Insira o valor de cada Alternativa para cada Critério;
                - Após a inserção de cada valor deverá ser pressionado a tecla "Enter" 
                - Os valores "não inteiros" deverão ser inseridos com Ponto. Exemplo: "10.5", "6.3" etc.  
                - Os valores inseridos poderão ser conferidos na Matriz de Decisao que se segue, após clicar no botão "Confirmar os valores inseridos". '''

                ag = AgGrid(df, editable=True, height=200, layout="centered")
                #ag = AgGrid(df, editable=st.session_state.edit, height=200)
                df2 = ag['data']
                

                #st.write('Os valores inseridos poderão ser conferidos na Matriz de Decisao que se segue, após clicar no botão:', layout="centered")
                botao_inclusao_matriz = st.form_submit_button('Confirmar os valores inseridos.')
                df2.index = lista_alternativas
                st.dataframe(df2)
                matriz = np.array(df2) #st.dataframe['data']     #Teste para retirar os valores da matriz
                #st.write(matriz)
                #matriz = [[1,2,3,4,5,6],                  # retirar isso aqui  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                #[12,11,10,9,8,7],                           # retirar isso aqui  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                #[13,14,15,16,17,18],                       # retirar isso aqui  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                #[24,23,22,21,20,19],                       # retirar isso aqui  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                #[25,26,27,28,29,30],                    # retirar isso aqui  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                #[36,35,34,33,32,31],                    # retirar isso aqui  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                #[37,38,39,40,41,42],                    # retirar isso aqui  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                #[48,47,46,45,44,43],                     # retirar isso aqui  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                #[49,50,51,52,53,54],                     # retirar isso aqui  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                #[60,59,58,57,56,55]]                     # retirar isso aqui  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                if botao_inclusao_matriz:
                    st.session_state.inicio_calculo = 1
#===============================================================================================
#===============================================================================================
                                #INICIO DOS CALCULOS
#===============================================================================================
#===============================================================================================
        if st.session_state.inicio_calculo == 1:
            soma_valores_inseridos = df2.sum()
            soma_total = soma_valores_inseridos.sum()
            if soma_total <= (n_alternativas * n_criterios):
                st.error(f'Preencha a Matriz Decisão com os valores do Trabalho "{trabalho}" ')
            else:

        #if df2.iloc[(n_alternativas-1), (n_criterios-1)] is not "0.0000":
            #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--================-=-=-=-=-=-=-
            #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--================-=-=-=-=-=-=-
                                            # Nenhum desses dados são mostrados
            #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--================-=-=-=-=-=-=-
            #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--================-=-=-=-=-=-=-                                            
            #=-=-=-=-=-=-=-=-=- VALORES MAX E MIN DE CADA CRITÉRIO =-=-=-=--=---=-=#
                lista_valormax = []
                lista_valormin = []
                valor_maxcoluna = -9999999 
                valor_mincoluna = 999999999
                for C in range(n_criterios):
                    for L in range(n_alternativas):
                        if matriz[L][C] > valor_maxcoluna:
                            valor_maxcoluna = matriz [L][C]
                    lista_valormax.append(valor_maxcoluna)
                    valor_maxcoluna = -9999999
                    for L in range(n_alternativas):
                        if matriz[L][C] < valor_mincoluna:
                            valor_mincoluna = matriz[L][C]
                    lista_valormin.append(valor_mincoluna)
                    valor_mincoluna = 99999999        

                    #st.write(f'O valor máximo do Critério {lista_criterios[C]} é {lista_valormax[C]}')
                    #st.write(f'O valor minimo do Critério {lista_criterios[C]} é {lista_valormin[C]}')

                #st.write(f'''Valor do vetor dos valores MAX dos Critérios: {lista_valormax}''')
                #st.write(f'''Valor do vetor dos valores MIN dos Critérios: {lista_valormin}''')
                #=-=--=-=-=-=-=-=- Apresentação da Matriz Normalizada =-=-=-=---=--=-=-=-#
                matriz_n_t = []
                matriz_n = []
                for C in range(n_criterios):
                    normal = []
                    normalizar = float(0)
                    if id_criterio[C] == 'L':               # Maximizando
                        for L in range(n_alternativas):
                            normalizar = abs((matriz[L][C]-lista_valormin[C])/(lista_valormax[C]-lista_valormin[C])) 
                            normal.append(normalizar)
                        matriz_n_t.append(normal)
                    else:
                        if id_criterio[C] == 'C':
                            for L in range(n_alternativas):          # Minimizando
                                normalizar = abs((matriz[L][C]-lista_valormax[C])/(lista_valormin[C]-lista_valormax[C]))
                                normal.append(normalizar)     
                            matriz_n_t.append(normal)

                matriz_n = np.transpose(matriz_n_t)
                #st.write('matriz transposta matriz_n', matriz_n, 'essa mesmo matriz_n')
                #matriz_print = pd.DataFrame(data=matriz_n_t, index=lista_alternativas, columns=lista_criterios)
                
                # IMPRIMINDO A MATRIZ USANDO O PANDAS
                teste_1 = pd.DataFrame(data=matriz, index=lista_alternativas, columns=lista_criterios)
                #st.write('matriz teste_1', teste_1, 'matriz teste_1')
                # IMPRIMINDO A MATRIZ USANDO O PANDAS
                teste_2 = pd.DataFrame(data=matriz_n, index=lista_alternativas, columns=lista_criterios)
                #st.write('matriz_teste_2', teste_2, 'matriz teste_2')

                # =-=--=-=-=-=-=--= Coeficiente de Correlação entre os atributos (Pearson - [-1,1]). =-=--=-=-=-=--
                # =-=-=-=-=-=-  (-1, correlação inversar; 1, correlação direta; e 0 não possui correlação =-=-=-=-=-=-
                #import seaborn as sns #Apresentação de um grafico com mapa de calor
                correl = pd.DataFrame(data=matriz_n, index=lista_alternativas, columns=lista_criterios).corr()
                #mapa_calor = sns.heatmap(correl, annot=True, vmin=-1, vmax=1, cmap='coolwarm')

                # Grafico de correlção
                fig_correl, ax = plt.subplots(figsize=(5, 5))
                sns.heatmap(correl, annot=True, vmin=-1, vmax=1, cmap='Blues')
                ax.set_title('Correlação dos Critérios')
                fig_correl.tight_layout()
                
                # =-=-=-=-=-=-=-- Matriz (1 - Correlação) e vetor Soma dos critérios. =-=-=-=-=-=-=-=-
                um_menos_correl = (1 - correl)
                soma_correl = um_menos_correl.sum()
                                
                #=-=-=-=-=-=-=-=-=-= Desvio Padrão sobre a matriz normalizada =-=-=-=-=-=-=-
                matriz_print = pd.DataFrame(data=matriz_n, index=lista_alternativas, columns=lista_criterios)
                desvio = matriz_print.std()
                            
                #=-=-=-=-=-=-=-=-=-=- Indice C =-=-=-=-==-=-=-=--=-
                indice_c = soma_correl * desvio
                soma_indice_c = indice_c.sum()

                #=-=-=-=-=-=-=-=-=-=-=- Cálculo do Peso =-==-=-=-=-=-=--
                #==================================================================================
                #==================================================================================
                #==================================================================================
                #===== Calculando o Peso ========
                peso = indice_c / soma_indice_c
                
                #===== Imprimindo o Gráfico ========
                altura = []             # valor que está no eixo x
                for i in peso.values:
                    altura.append(i)
                posicao = []
                for i in range(0,10,1): 
                    posicao.append(i)

                L = ['Ordenação dos Pesos']
                x = lista_criterios
                y = peso.values
                df_peso = pd.DataFrame(data = y, index = x, columns = L)

                fig_peso, ax = plt.subplots(figsize=(8,6))
                            
                #criando o gráfico de barras horizontais
                ax = sns.barplot(y=df_peso.index, x=df_peso['Ordenação dos Pesos'], ax=ax, palette='YlOrRd_r') #Para inverter a ordem das cores basta você substituir o sufixo " d " de " GnBu_d " pelo sufixo " r ", ficando então " GnBu_r ".
                #YlOrRd
                #PuBu
                #YlGn
                #GnBu

                #link para ver cores do gráfico: https://chrisalbon.com/code/python/data_visualization/seaborn_color_palettes/

                sns.set_style('white')  #colocando um fundo branco no gráfico
                ax.set_title("Valores dos Pesos", fontdict={'fontsize':15}) #adicionando título
                ax.set_xlabel('Valores', fontdict={'fontsize':14}) #mudando e nome e tamanho do label x
                ax.set_ylabel('Critérios', fontdict={'fontsize':14}) #mudando tamanho do label eixo y
                ax.tick_params(labelsize=14) #mudando tamanho dos labels dos ticks
                ax.spines['bottom'].set_linewidth(2.5) #aumentando espessura linha inferior

                for axis in ['top', 'right', 'left']: #remoção dos outros três axis
                    ax.spines[axis].set_color(None)

                ax.tick_params(axis='x', labelleft=False, left=None) #remoção dos ticks

                #colocando rótulo no gráfico
                rotulo_grafico2 = peso.values 
                for index, value in enumerate(peso): 
                    plt.text(value, index, 
                            str(round(value,4)))

                #otimizar espaço da figure
                fig_peso.tight_layout()
                
    #============================================================================================
    #============================================================================================
    #============================================================================================
    #============================================================================================
    #============================================================================================


                #=-=-=-=-=--=- Grey Relational Analysis =-=-=-=--=-=-=
                #=-=-=-=-=-- Inicio da Ordenação das Alternativas =--==-=-=-=-=--=-
                #=-=-=-=-=-=- CRTIC-GRA-3N (1ª Normalização) =-=-=-=-=--

                y = peso.values

                #=-=-=-=-=- Selecionar os Vetores MAX e MIN da Matriz criada - GRA =-==-=-=-=-=-
                #VALORES MAX E MIN DE CADA CRITÉRIO
                lista_valormax_1 = []
                lista_valormin_1 = []
                valor_maxcoluna = -9999999 
                valor_mincoluna = 999999999
                for C in range(n_criterios):
                    for L in range(n_alternativas):
                        if matriz[L][C] > valor_maxcoluna:
                            valor_maxcoluna = matriz [L][C]
                    lista_valormax_1.append(valor_maxcoluna)
                    valor_maxcoluna = -9999999
                    for L in range(n_alternativas):
                        if matriz[L][C] < valor_mincoluna:
                            valor_mincoluna = matriz[L][C]
                    lista_valormin_1.append(valor_mincoluna)
                    valor_mincoluna = 99999999        

                #=-=-=-=-=-=-===- Normalização da MATRIZ =-=-=-==--
                teste_2 = pd.DataFrame(data=matriz_n, index=lista_alternativas, columns=lista_criterios)

                #=-=-=-=-=- Matriz Sequencia de Desvios - GRA =-=-===-=-
                #=-=-=-=-=- Faz a comparação da matriz normalizada com uma matriz de Referencia [1,1,1...1]=-=-=--
                matriz_seq_des = 1 - matriz_n
                matriz_seq_des_pd = pd.DataFrame(matriz_seq_des, index=lista_alternativas, columns=lista_criterios)

                #=-=-=-=-=-= Apresentação dos valores MAX e MIN da Matriz Sequencia de Desvio - GRA =-=-=-=--
                lista_valormax_seq = pd.DataFrame(matriz_seq_des, columns=lista_criterios).max()
                lista_valormin_seq = pd.DataFrame(matriz_seq_des, index=lista_alternativas, columns=lista_criterios).min()
                
                #=-=-=-=-=-===- Coeficiente Relacional Cinza (Última Matriz) =-=-=-=-=-=-
                matriz_coe =[]
                matriz_coe_t=[]
                lista_valormin_seq_array = np.array(lista_valormin_seq)
                lista_valormax_seq_array = np.array(lista_valormax_seq)
                for C in range(n_criterios):
                    normal_coe = []
                    normalizar = float(0)
                    for L in range(n_alternativas):
                        normalizar = ((lista_valormin_seq_array[C] + coeficiente_dist*lista_valormax_seq_array[C])/(matriz_seq_des[L][C] + coeficiente_dist*lista_valormax_seq_array[C])) 
                        normal_coe.append(normalizar)
                    matriz_coe_t.append(normal_coe)
                matriz_coe = np.transpose(matriz_coe_t)
                matriz_coe_pd = pd.DataFrame(data=matriz_coe, index=lista_alternativas, columns=lista_criterios)

                #=-=-=-=-=-=-= Grade Relacional Cinza (uma única coluna) - GRA =-=-=-=-=-=-
                matriz_grad_t = []
                matriz_grad = []
                for C in range(n_criterios):
                    grade=[]
                    normal = float(0)
                    for L in range(n_alternativas):
                        normal = peso[C]*matriz_coe[L][C]
                        grade.append(normal)
                    matriz_grad_t.append(grade)
                matriz_grad = np.transpose(matriz_grad_t)

                #'Matriz ponderada !!'
                pd.DataFrame(matriz_grad, index=lista_alternativas, columns=lista_criterios)
                
                # Coluna Soma da Matriz Ponderada - Matriz GRADE (uma unica coluna "grade")
                grade_relat=[]
                grade=[]
                for L in range(n_alternativas):
                    soma=float(0)
                    for C in range(n_criterios):
                        soma = soma + matriz_grad[L][C]
                    grade.append(soma)
                    soma = float(0)
                grade_relat = np.transpose(grade)

                y = ['GRA']
                resultado = pd.DataFrame(data=grade_relat, index=lista_alternativas, columns=y)
                #'Resultado do GRA sem estar ordem crescente:'
                sort_resultado = resultado.sort_values(by=y, ascending=False)
                #'resultado usando sort para ordenar:'

                # criando uma linha com os numeros de 1 a "n" para incluir no final da serie sort_resultado
                ord=[]
                valor=0
                for i in range(n_alternativas):
                    valor = i+1
                    ord.append(valor)

                
                final = sort_resultado.assign(Ordenação = ord)

                #=-=-=-=-=--= Transformando listas das Alternativas e dos Critérios em Dicionarios - GRA =-=-=-=-=-=
                dic = dict(zip(lista_alternativas, grade))              #gerou um dicionario juntando duas listas
                
                import operator                                                                 
                sorteddict = sorted(dic.items(), key=operator.itemgetter(1), reverse = True)  # Ordena em ordem decrescente gerando tuplas
                
                from collections import defaultdict                                           # Tiro a Tupla e transformo em dicionario com valor em lista
                #test_list = [(1, 'gfg'), (1, 'is'), (2, 'best'), (3, 'for'), (4, 'CS')] 
                print("The original list is : " + str(sorteddict)) 
                res = defaultdict(list) 
                for i, j in sorteddict: 
                    res[i].append(j) 
                #print("The merged dictionary is : " + str(dict(res)))
                
                criterio_eixo_grafico = res.keys()                        # Recebendo as chaves de um dicionário
                criterio_eixo_grafico = list(criterio_eixo_grafico)         # Transformando as chaves recebidos em uma lista
                print(criterio_eixo_grafico)
                
                dados_grafico = res.values()                      # Recebendo os valores de um dicionário
                dados_grafico = list(dados_grafico)        # Transformando os valores recebidos em uma lista (de listas)
                
                lista_final = []
                for i in range(n_alternativas):
                #  for c in range(numero_alternativas):
                    valor = dados_grafico[i][0]
                    lista_final.append(valor)

                #=======================================================================================
                #======================================================================================
                # =--=-=-=-=-=-=--=-=- PLOTAGEM DOS RESULTADOS GRA (CRITIC-GRA) =-=-=-=-=-=-=-=-=-=-==-=
                altura = [] # valor que está no eixo x
                for i in lista_final:
                    altura.append(i)
                posicao = []
                for i in range(0,10,1): 
                    posicao.append(i)

                L = ['Ordenação']
                x = criterio_eixo_grafico
                y = lista_final
                df_GRA = pd.DataFrame(data = y, index = x, columns = L)

                fig_GRA, ax = plt.subplots(figsize=(8,6))
                #Grafico de Barras Horizontais
                ax = sns.barplot(y=df_GRA.index, x=df_GRA['Ordenação'], ax=ax, palette='GnBu_r') #Para inverter a ordem das cores basta você substituir o sufixo " d " de " GnBu_d " pelo sufixo " r ", ficando então " GnBu_r ".
                #YlOrRd
                #PuBu
                #YlGn
                #GnBu
                #link para ver cores do gráfico: https://chrisalbon.com/code/python/data_visualization/seaborn_color_palettes/

                ax.set_facecolor("white")
                ax.set_title("Ordenação das Alternativas: CRITIC-GRA", fontdict={'fontsize':16}) #adicionando título
                ax.set_xlabel('Valores', fontdict={'fontsize':14}) #mudando e nome e tamanho do label x
                ax.set_ylabel('Alternativas', fontdict={'fontsize':14}) #mudando tamanho do label eixo y
                ax.tick_params(labelsize=14) #mudando tamanho dos labels dos ticks
                ax.spines['bottom'].set_linewidth(2.5) #aumentando espessura linha inferior

                plt.grid(False)          #tirar as linhas Brancas da grade

                for axis in ['top', 'right', 'left']: #remoção dos outros três axis
                    ax.spines[axis].set_color(None)

                ax.tick_params(axis='x', labelleft=False, left=None) #remoção dos ticks

                #colocando rótulo no gráfico
                rotulo_grafico2 = lista_final 
                for index, value in enumerate(lista_final): 
                    plt.text(value, index, 
                            str(round(value,4)))

                #otimizar espaço da figure
                fig_GRA.tight_layout()

    #============================================================================================
    #============================================================================================
    #============================================================================================
    #============================================================================================
    #============================================================================================
    
                #=-=-=-=-=-=- Inicio da Segunda Ordenação =-=-==-==-=-=-=-=-=-=-=-=-
                #=-=-=-=-=-=-= GRA + 2ªNormalização =-=-=-==-=-=-=-=--=--=-=-=-=-=-=
                # =-=-==-=-=-- Para Segunda Ordenação será realizado a 2ªNormalização e será rodado todo o método GRA novamente.
                # =-=-=-=-===- A 2ª Normalização é feita atraves da distribuição normal dos valores de alternativa com os critérios

                matriz_sinal = []
                for L in range(n_alternativas):
                    matriz_inic_sinal = []
                    for C in range(n_criterios):
                        if id_criterio[C] in ('C', 'c'):
                            valor = matriz[L][C] * (-1)
                            matriz_inic_sinal.append(valor)
                        if id_criterio[C] in ('L', 'l'):
                            valor = matriz[L][C]
                            matriz_inic_sinal.append(valor)
                    matriz_sinal.append(matriz_inic_sinal)
                
                # Transformando a matriz em Dataframe e tirando a média dos critérios
                matriz_sinal_pd = pd.DataFrame(matriz_sinal, index = lista_alternativas, columns = lista_criterios)
                med_matriz_sinal = matriz_sinal_pd.mean()
                
                # Calculando o desvio padrão 
                des_matriz_sinal = matriz_sinal_pd.std()
        
                dis_normal = []
                x=0
                for L in range(n_alternativas):
                    dist_nor=[]
                    for C in range(n_criterios):
                        x = matriz_sinal[L][C]
                        valor = norm.cdf(x, loc= med_matriz_sinal[C], scale = des_matriz_sinal[C])
                        dist_nor.append(valor)
                    dis_normal.append(dist_nor)
                Ç = pd.DataFrame(dis_normal, index= lista_alternativas, columns= lista_criterios)

                #=-=-=-=-=-==--= Matriz Sequencia de Desvios =-=-=-==-=---==
                #=--==-=-=Faz a comparação da matriz normalizada com uma matriz de Referencia [1,1,1...1]=-=-=--==-
                #=-=-=-=-=-=-=-==-=- GRA com 2ª Normalização =-==-=-=-=-==-=-
                dis_normal_pd = pd.DataFrame(dis_normal, index=lista_alternativas, columns = lista_criterios)
                matriz_seq_des_2n = 1 - dis_normal_pd

                #=-=-=-=-=-=-==- Apresentação dos valores MAX e MIN da Matriz Sequencia de Desvio =--=-=-=-=-
                #=-=-=-=-=-=-=-=-=-   GRA + 2ª Normalização   =-=-=-=-=-=-=-=-=-=-=-=-==-
                
                lista_max2n = matriz_seq_des_2n.max()
                lista_min2n = matriz_seq_des_2n.min()

                #=-=-=-=-=-=-=-=- Coeficiente Relacional Cinza (Última Matriz) =-=-=-=-=-=-
                #=-=-=-=-=--===-   GRA + 2ª Normalização =-=-==-===-=-=-
                base_cal = pd.DataFrame(matriz_sinal, index= lista_alternativas, columns = lista_criterios)
                matriz_coe_2n = base_cal
                for L in range(n_alternativas):
                    for C in range(n_criterios):
                        x = ((lista_min2n[C] + coeficiente_dist*lista_max2n[C])/(matriz_seq_des_2n.iloc[L,C] + coeficiente_dist*lista_max2n[C]))
                        matriz_coe_2n.iloc[L,C] = x

                #=-=-=-=-==-=-=-=-=- Grade Relacional Cinza (uma única coluna) =-=-=-=-=-=-=-=
                #=-=-=-=-=-==-=-=-  GRA + 2ª Normalização =-=-==-=-=-=-=--
                #====================================================================
                # Matriz Ponderada com a Segunda Normalização: 

                base_cal = pd.DataFrame(matriz_sinal, index= lista_alternativas, columns = lista_criterios)
                matriz_grad_2n = base_cal

                for L in range(n_alternativas):
                    for C in range(n_criterios):
                        x = peso[C]*matriz_coe_2n.iloc[L,C]
                        matriz_grad_2n.iloc[L,C] = x

                #st.write('Matriz Ponderada com a Segunda Normalização(matriz_grad_2n): ', matriz_grad_2n)
                
                #====================================================================
                # Criação da Grade Relational Cinza
                grade_relat_2n = matriz_grad_2n.sum(axis=1)

                resultado_2n = pd.DataFrame(grade_relat_2n, index = lista_alternativas, columns = ['GRA + 2ª Normalização'])
                #'grande_relat_2n é a coluna soma da matriz_grad_2n: '
                #'resultado_2n uma coluna trocando o nome GRA + 2º Normalização: '
                
                #=-=--=-=-=- Ordenando os resultados em ordem Decrescente =-=-=-=-=--
                
                print('Ordenação Decrescente dos Resultados')
                sort_resultado_2n = resultado_2n.sort_values(by=['GRA + 2ª Normalização'], ascending=False)
                #'resultado com a ordenação dos valores: '

                # criando uma linha com os numeros de 1 a "n" para incluir no final da serie sort_resultado
                ord_2=[]
                valor=0
                for i in range(n_alternativas):
                    valor = i+1
                    ord_2.append(valor)
                
                final_2n = sort_resultado_2n.assign(Ordenação = ord_2)              # .assign() inclui uma coluna com o nome sendo o primeiro item dentro do parenteses.

                #=-=-=-=-=-=-=- Transformando listas das Alternativas e dos Critérios em Dicionarios =-=-=-=-=-=-=
                #=--=-=-=-=-=-=-  GRA + 2ª Normalização =-=-=-=-=-=-==-=-
                dic_2n = dict(zip(lista_alternativas, grade_relat_2n))              #gerou um dicionario juntando duas listas a lista alternativas e a grade relational(uma coluna)

                #'Gerando dicionário !!', dic_2n)
                
                import operator                                                                 
                sorteddict_2n = sorted(dic_2n.items(), key=operator.itemgetter(1), reverse = True)  # Ordena em ordem decrescente gerando tuplas
                #'Dicionario em ordem decrescente!!', sorteddict_2n)
                

                #'Tirando as Tuplas !!')
                from collections import defaultdict                                           # Tiro a Tupla e transformo em dicionario com valor em lista
                #test_list = [(1, 'gfg'), (1, 'is'), (2, 'best'), (3, 'for'), (4, 'CS')] 
                #"The original list is : " + str(sorteddict_2n)) 
                res_2n = defaultdict(list) 
                for i, j in sorteddict_2n: 
                    res_2n[i].append(j) 
                #"The merged dictionary is : " + str(dict(res_2n)))
                
                criterio_eixo_grafico_2n = res_2n.keys()                        # Recebendo as chaves de um dicionário
                criterio_eixo_grafico_2n = list(criterio_eixo_grafico_2n)         # Transformando as chaves recebidos em uma lista
                #'Itens na ordem decrescente !!!', criterio_eixo_grafico_2n)
                
                dados_grafico_2n = res_2n.values()                      # Recebendo os valores de um dicionário
                dados_grafico_2n = list(dados_grafico_2n)        # Transformando os valores recebidos em uma lista (de listas)
                #'Valores em ordem decrescente!!!', dados_grafico_2n)

                lista_final_2n = []
                for i in range(n_alternativas):
                #  for c in range(numero_alternativas):
                    valor = dados_grafico_2n[i][0]
                    lista_final_2n.append(valor)
                #valores na ordem decrescente !!!', lista_final_2n)

                #===================================================================================
                #===================================================================================
                #===================================================================================
                #=-=-=-=-=-=-=-=-=- PLOTAGEM DOS RESULTADOS =-=--=-=-==-
                #=-=-=-=-=-=-=--  GRA + 2ª Normalização =-=--==-==-=-
                altura = [] # valor que está no eixo x
                for i in lista_final_2n:
                    altura.append(i)
                posicao = []
                for i in range(0,10,1): 
                    posicao.append(i)

                L = ['Ordenação']
                x = criterio_eixo_grafico_2n
                y = lista_final_2n
                df_GRA2N = pd.DataFrame(data = y, index = x, columns = L)

                fig_GRA2N, ax = plt.subplots(figsize=(8,6))
                
                #criando o gráfico de barras horizontais
                ax = sns.barplot(y=df_GRA2N.index, x=df_GRA2N['Ordenação'], ax=ax, palette='GnBu_r') #Para inverter a ordem das cores basta você substituir o sufixo " d " de " GnBu_d " pelo sufixo " r ", ficando então " GnBu_r ".
                #YlOrRd
                #PuBu
                #YlGn
                #GnBu
                #link para ver cores do gráfico: https://chrisalbon.com/code/python/data_visualization/seaborn_color_palettes/

                ax.set_facecolor("white")
                ax.set_title("Ordenação das Alternativas: CRITIC-GRA-2ªNormalização", fontdict={'fontsize':16}) #adicionando título
                ax.set_xlabel('Valores', fontdict={'fontsize':14}) #mudando e nome e tamanho do label x
                ax.set_ylabel('Alternativas', fontdict={'fontsize':14}) #mudando tamanho do label eixo y
                ax.tick_params(labelsize=14) #mudando tamanho dos labels dos ticks
                ax.spines['bottom'].set_linewidth(2.5) #aumentando espessura linha inferior

                plt.grid(False)          #tirar as linhas Brancas da grade

                for axis in ['top', 'right', 'left']: #remoção dos outros três axis
                    ax.spines[axis].set_color(None)

                ax.tick_params(axis='x', labelleft=False, left=None) #remoção dos ticks

                #colocando rótulo no gráfico
                rotulo_grafico2 = lista_final_2n 
                for index, value in enumerate(lista_final_2n): 
                    plt.text(value, index, 
                            str(round(value,4)))

                #otimizar espaço da figure
                fig_GRA2N.tight_layout()

    #============================================================================================
    #============================================================================================
    #============================================================================================
    #============================================================================================
    #============================================================================================

                #=-=-=-=- Inicio da Terceira Ordenação : =-=-==-==-=-=-
                #=-==-=-=-  2ªNormalização + CRITIC =-=-=-=-=-=-=--=-
                # =-=-=-=- Para Terceira Ordenação será utilizado a 2ªNormalização e será ponderado com o peso calculado pelo CRITIC.
                #=-=-=-=-=- A 2ª Normalização é feita atraves da distribuição normal dos valores de alternativa com os critérios

                dist_normal_pd = pd.DataFrame(dis_normal, index= lista_alternativas, columns= lista_criterios)
                
                #==================================================================
                # Matriz Ponderada com a Segunda Normalização: 

                base_cal = pd.DataFrame(matriz_sinal, index= lista_alternativas, columns = lista_criterios)
                matriz_grad_3n = base_cal

                for L in range(n_alternativas):
                    for C in range(n_criterios):
                        x = peso[C]*dist_normal_pd.iloc[L,C]
                        matriz_grad_3n.iloc[L,C] = x

                #====================================================================
                # Matriz GRADE Relacional Cinza (UNICA COLUNA)
                grade_relat_3n = matriz_grad_3n.sum(axis=1)
                
                #====================================================================
                # Resultado trocando a coluna para o nome da Ordenação
                resultado_3n = pd.DataFrame(grade_relat_3n, index=lista_alternativas, columns = ['2ª Normalização + CRITIC'])
                
                # =========================================================================
                # Ordenando os resultados em ordem Decrescente
                sort_resultado_3n = resultado_3n.sort_values(by=['2ª Normalização + CRITIC'], ascending=False)
                        
                #==========================================================================
                # criando uma linha com os numeros de 1 a "n" para incluir no final da serie sort_resultado
                ord_3n=[]
                valor=0
                for i in range(n_alternativas):
                    valor = i+1
                    ord_3n.append(valor)
                
                final_3n = sort_resultado_3n.assign(Ordenação = ord_3n)              # .assign() inclui uma coluna com o nome sendo o primeiro item dentro do parenteses.
                

                #=-=-=-=-==-=-=- Transformando listas das Alternativas e dos Critérios em Dicionarios =-=-=-=--==
                #=-=-=-=-==-=-=  2ª Normalização + CRITIC =-=-=-=--===-
                dic_3n = dict(zip(lista_alternativas, grade_relat_3n))              #gerou um dicionario juntando duas listas a lista alternativas e a grade relational(uma coluna)
                #'Gerando dicionário !!', dic_3n)
                            
                import operator                                                                 
                sorteddict_3n = sorted(dic_3n.items(), key=operator.itemgetter(1), reverse = True)  # Ordena em ordem decrescente gerando tuplas
                #'Dicionario em ordem decrescente !!', sorteddict_3n)
                
                #'Tirando as Tuplas !!')
                from collections import defaultdict                                           # Tiro a Tupla e transformo em dicionario com valor em lista
                #test_list = [(1, 'gfg'), (1, 'is'), (2, 'best'), (3, 'for'), (4, 'CS')] 
                #"The original list is : " + str(sorteddict_3n)) 
                res_3n = defaultdict(list) 
                for i, j in sorteddict_3n: 
                    res_3n[i].append(j) 
                #"The merged dictionary is : " + str(dict(res_3n)))
                            
                criterio_eixo_grafico_3n = res_3n.keys()                        # Recebendo as chaves de um dicionário
                criterio_eixo_grafico_3n = list(criterio_eixo_grafico_3n)         # Transformando as chaves recebidos em uma lista
                
                
                dados_grafico_3n = res_3n.values()                      # Recebendo os valores de um dicionário
                dados_grafico_3n = list(dados_grafico_3n)        # Transformando os valores recebidos em uma lista (de listas)
                

                lista_final_3n = []
                for i in range(n_alternativas):
                #  for c in range(numero_alternativas):
                    valor = dados_grafico_3n[i][0]
                    lista_final_3n.append(valor)
                

                #===================================================================================
                #===================================================================================
                #===================================================================================
                #=-=-=-=--=-=- PLOTAGEM DOS RESULTADOS (terceiro grafico) =-=-=-=-=-=-==-
                #=-=-=-=-=-==-=-=-=-=-  2ª Normalização + CRITIC   =--==-=-=-=-=-=-
                altura = [] # valor que está no eixo x
                for i in lista_final_3n:
                    altura.append(i)
                posicao = []
                for i in range(0,10,1): 
                    posicao.append(i)

                L = ['Ordenação']
                x = criterio_eixo_grafico_3n
                y = lista_final_3n
                df_GRA3N = pd.DataFrame(data = y, index = x, columns = L)

                fig_GRA3N, ax = plt.subplots(figsize=(8,6))
                #criando o gráfico de barras horizontais
                ax = sns.barplot(y=df_GRA3N.index, x=df_GRA3N['Ordenação'], ax=ax, palette='GnBu_r') #Para inverter a ordem das cores basta você substituir o sufixo " d " de " GnBu_d " pelo sufixo " r ", ficando então " GnBu_r ".
                #YlOrRd
                #PuBu
                #YlGn
                #GnBu
                #link para ver cores do gráfico: https://chrisalbon.com/code/python/data_visualization/seaborn_color_palettes/
                
                ax.set_facecolor("white")
                ax.set_title("Ordenação das Alternativas: 2ªNormlização - CRITIC", fontdict={'fontsize':15}) #adicionando título
                ax.set_xlabel('Valores', fontdict={'fontsize':14}) #mudando e nome e tamanho do label x
                ax.set_ylabel('Alternativas', fontdict={'fontsize':14}) #mudando tamanho do label eixo y
                ax.tick_params(labelsize=14) #mudando tamanho dos labels dos ticks
                ax.spines['bottom'].set_linewidth(2.5) #aumentando espessura linha inferior

                plt.grid(False)          #tirar as linhas Brancas da grade

                for axis in ['top', 'right', 'left']: #remoção dos outros três axis
                    ax.spines[axis].set_color(None)

                ax.tick_params(axis='x', labelleft=False, left=None) #remoção dos ticks

                #colocando rótulo no gráfico
                rotulo_grafico2 = lista_final_3n 
                for index, value in enumerate(lista_final_3n): 
                    plt.text(value, index, 
                            str(round(value,4)))

                #otimizar espaço da figure
                fig_GRA3N.tight_layout()
                
    #============================================================================================
    #============================================================================================
    #============================================================================================
    #============================================================================================
    #============================================================================================

                #=-=-=-=-=-=-=-=- Normalização dos Resultados das Três primeiras ordenações =--=-=-=-=-=-=-
                #=-=-=-=-=--==-=-=-    É calculado a normalização para cada ordenação =-=-==-==-=-=-=--=-=
                # Normalização da primeira Ordenação ============================================================
                resultado = pd.DataFrame(grade_relat, index=lista_alternativas, columns = ['CRITIC + GRA'])
                normaliza_1 = resultado/resultado.sum()
        
                # Normalização da segunda Ordenação ============================================================
                resultado_2n = pd.DataFrame(grade_relat_2n, index=lista_alternativas, columns = ['GRA + 2ª Normalização'])
                normaliza_2 = resultado_2n/resultado_2n.sum()

                # Normalização da Terceira Ordenação ============================================================
                resultado_3n = pd.DataFrame(grade_relat_3n, index=lista_alternativas, columns = ['2ª Normalização + CRITIC'])
                normaliza_3 = resultado_3n/resultado_3n.sum()
                
                #=-=-=-=-=-=-=-=- Inicio Quarta Ordenação - Média Aritmética dos Valores Calculados =-=-=-=-=-=-
                # ======== ////// ========= Média Aritmética Normalizada -> 4_ord ============= //////// ==================
                media_n = []
                for L in range(n_alternativas):
                    valor = (normaliza_1.iloc[L,0] + normaliza_2.iloc[L,0] + normaliza_3.iloc[L,0])/3
                    media_n.append(valor)

                resultado_n_4n = pd.DataFrame(media_n, index = lista_alternativas, columns = ['4ª Ordenação - Média aritmética dos valores normalizados '])
            
                # =========== ////// ============== Ordenando os resulatados da média normalizada ============= //////// ==================
                sort_resultado_n_4n = resultado_n_4n.sort_values(by=['4ª Ordenação - Média aritmética dos valores normalizados '], ascending=False)
                
                #==========================================================================
                # criando uma linha com os numeros de 1 a "n" para incluir no final da serie sort_resultado
                ord_4n=[]
                valor=0
                for i in range(n_alternativas):
                    valor = i+1
                    ord_4n.append(valor)
                
                # ================= impressão do resultado ===========================
                final_n_4n = sort_resultado_n_4n.assign(Ordenação = ord_4n)

                #=-=-=-=- Transformando listas das Alternativas e dos Critérios em Dicionarios =-=-=-=-
                #=-=-=-=-=-=-=-==-=-=- Média dos Valores calculados -> 4_ord =-=-=-=-=-=-=--
                # ================ /////// ================  Dicionário dos valores Normalizados  =====================  ////////  ====================
                dic_n_4n = dict(zip(lista_alternativas, media_n))              #gerou um dicionario juntando duas listas a lista alternativas e a grade relational(uma coluna)
                #'Gerando dicionário !!', dic_n_4n)
                
                import operator                                                                 
                sorteddict_n_4n = sorted(dic_n_4n.items(), key=operator.itemgetter(1), reverse = True)  # Ordena em ordem decrescente gerando tuplas
                #'Dicionario em ordem decrescente !!', sorteddict_n_4n)
                
                #'Tirando as Tuplas !!')
                from collections import defaultdict                                           # Tiro a Tupla e transformo em dicionario com valor em lista 
                #"The original list is : " + str(sorteddict_n_4n)) 
                res_n_4n = defaultdict(list) 
                for i, j in sorteddict_n_4n: 
                    res_n_4n[i].append(j) 
                #"The merged dictionary is : " + str(dict(res_n_4n)))
                
                criterio_eixo_grafico_n_4n = res_n_4n.keys()                        # Recebendo as chaves de um dicionário
                criterio_eixo_grafico_n_4n = list(criterio_eixo_grafico_n_4n)         # Transformando as chaves recebidos em uma lista
                #'Itens na ordem decrescente !!!', criterio_eixo_grafico_n_4n)
                
                dados_grafico_n_4n = res_n_4n.values()                      # Recebendo os valores de um dicionário
                dados_grafico_n_4n = list(dados_grafico_n_4n)        # Transformando os valores recebidos em uma lista (de listas)
                #'Valores na ordem descrecente: ', dados_grafico_2n)

                lista_final_n_4n = []
                for i in range(n_alternativas):
                #  for c in range(numero_alternativas):
                    valor = dados_grafico_n_4n[i][0]
                    lista_final_n_4n.append(valor)
                #'Resultado final da Quarta Ordenação na ordem decrescente !!!',

                #================================================================================
                #================================================================================
                #================================================================================
                #=-=-=-=-=-=-=- PLOTAGEM DOS RESULTADOS =--==-=-=-==--=-=-=-=--
                #=--=--=-=-=-=-=-  Média dos Valores calculados -> 4_ord =-=--=-=-=-=-=-
                altura = [] # valor que está no eixo x
                for i in lista_final_n_4n:
                    altura.append(i)
                posicao = []
                for i in range(0,10,1): 
                    posicao.append(i)

                L = ['Ordenação']
                x = criterio_eixo_grafico_n_4n
                y = lista_final_n_4n
                df_GRA4N = pd.DataFrame(data = y, index = x, columns = L)

                fig_GRA4N, ax = plt.subplots(figsize=(8,6))
                #criando o gráfico de barras horizontais
                ax = sns.barplot(y=df_GRA4N.index, x=df_GRA4N['Ordenação'], ax=ax, palette='GnBu_r') #Para inverter a ordem das cores basta você substituir o sufixo " d " de " GnBu_d " pelo sufixo " r ", ficando então " GnBu_r ".
                #YlOrRd
                #PuBu
                #YlGn
                #GnBu
                #link para ver cores do gráfico: https://chrisalbon.com/code/python/data_visualization/seaborn_color_palettes/

                ax.set_facecolor("white")
                ax.set_title("Ordenação das Alternativas: Média Aritmética das três primeiras Ordenações", fontdict={'fontsize':15}) #adicionando título
                ax.set_xlabel('Valores', fontdict={'fontsize':14}) #mudando e nome e tamanho do label x
                ax.set_ylabel('Alternativas', fontdict={'fontsize':14}) #mudando tamanho do label eixo y
                ax.tick_params(labelsize=14) #mudando tamanho dos labels dos ticks
                ax.spines['bottom'].set_linewidth(2.5) #aumentando espessura linha inferior
                plt.grid(False)          #tirar as linhas Brancas da grade

                for axis in ['top', 'right', 'left']: #remoção dos outros três axis
                    ax.spines[axis].set_color(None)
                ax.tick_params(axis='x', labelleft=False, left=None) #remoção dos ticks

                #colocando rótulo no gráfico
                rotulo_grafico2 = lista_final_n_4n 
                for index, value in enumerate(lista_final_n_4n): 
                    plt.text(value, index, 
                            str(round(value,4)))

                #otimizar espaço da figure
                fig_GRA4N.tight_layout()

    #============================================================================================
    #============================================================================================
    #============================================================================================
    #============================================================================================
    #============================================================================================
                # ========== ////// ========= Média Geométrica Normalizada -> 5_ord ============= //////// ==================
                media_g_n = []
                for L in range(n_alternativas):
                    valor = (normaliza_1.iloc[L,0] * normaliza_2.iloc[L,0] * normaliza_3.iloc[L,0])**(1/3)
                    media_g_n.append(valor)

                resultado_n_5n = pd.DataFrame(media_g_n, index = lista_alternativas, columns = ['5ª Ordenação - Média Geométrica dos valores normalizados '])
                
                # =========== ////// ============== Ordenando os resulatados da média normalizada ============= //////// ==================
                sort_resultado_n_5n = resultado_n_5n.sort_values(by= ['5ª Ordenação - Média Geométrica dos valores normalizados '], ascending=False)
                
                #==========================================================================
                # criando uma linha com os numeros de 1 a "n" para incluir no final da serie sort_resultado
                ord_5n=[]
                valor=0
                for i in range(n_alternativas):
                    valor = i+1
                    ord_5n.append(valor)

                # ================= impressão do resultado ===========================

                
                final_n_5n = sort_resultado_n_5n.assign(Ordenação = ord_5n)
                #st.write('Resultado final das ordenações: ', final_n_5n)

                #=-=-=-=-=-=-=-=- Transformando listas das Alternativas e dos Critérios em Dicionarios =-=-=-=-==-=-=-
                # ======== /////// ======== Média dos Valores calculados - VALORES NORMALIZADOS ======================== /////////// ===================
                dic_n_5n = dict(zip(lista_alternativas, media_g_n))              #gerou um dicionario juntando duas listas a lista alternativas e a grade relational(uma coluna)
                #'Gerando dicionário Normalizado quinta Ordenação !!', dic_n_5n)
                

                print('Dicionario normalizado em ordem decrescente !!')
                import operator                                                                 
                sorteddict_n_5n = sorted(dic_n_5n.items(), key=operator.itemgetter(1), reverse = True)  # Ordena em ordem decrescente gerando tuplas
                #'Dicionario normalizado em ordem decrescente !!', sorteddict_n_5n)
                
                #'Tirando as Tuplas !!')
                from collections import defaultdict                                           # Tiro a Tupla e transformo em dicionario com valor em lista
                #"The original list is : " + str(sorteddict_n_5n)) 
                res_n_5n = defaultdict(list) 
                for i, j in sorteddict_n_5n: 
                    res_n_5n[i].append(j) 
                #"The merged dictionary is : " + str(dict(res_n_5n)))
                
                criterio_eixo_grafico_n_5n = res_n_5n.keys()                        # Recebendo as chaves de um dicionário
                criterio_eixo_grafico_n_5n = list(criterio_eixo_grafico_n_5n)         # Transformando as chaves recebidos em uma lista
                #'Itens na ordem decrescente !!!',
                
                dados_grafico_n_5n = res_n_5n.values()                      # Recebendo os valores de um dicionário
                dados_grafico_n_5n = list(dados_grafico_n_5n)        # Transformando os valores recebidos em uma lista (de listas)

                lista_final_n_5n = []
                for i in range(n_alternativas):
                #  for c in range(numero_alternativas):
                    valor = dados_grafico_n_5n[i][0]
                    lista_final_n_5n.append(valor)
                #'Valores normalizados na ordem decrescente !!!'

                #==================================================================================
                #==================================================================================
                #==================================================================================
                #=-=-=-=-=-=-=-=-==-=--==- PLOTAGEM DOS RESULTADOS =-=--=-=-=-=-=-=-=-=-=-=--==-
                #=-=-=-=-=-=-=-=-=-= Média Geométrica dos Valores calculados -> 5_ord =-=-=--=-=-=-=-=-=-=-=--=
                altura = [] # valor que está no eixo x
                for i in lista_final_n_5n:
                    altura.append(i)
                posicao = []
                for i in range(0,10,1): 
                    posicao.append(i)

                L = ['Ordenação']
                x = criterio_eixo_grafico_n_5n
                y = lista_final_n_5n
                df_GRA5N = pd.DataFrame(data = y, index = x, columns = L)

                fig_GRA5N, ax = plt.subplots(figsize=(8,6))
                #criando o gráfico de barras horizontais
                ax = sns.barplot(y=df_GRA5N.index, x=df_GRA5N['Ordenação'], ax=ax, palette='GnBu_r') #Para inverter a ordem das cores basta você substituir o sufixo " d " de " GnBu_d " pelo sufixo " r ", ficando então " GnBu_r ".
                #YlOrRd
                #PuBu
                #YlGn
                #GnBu
                #link para ver cores do gráfico: https://chrisalbon.com/code/python/data_visualization/seaborn_color_palettes/
                sns.set_style('white')  #colocando um fundo branco no gráfico
                ax.set_title("Ordenação das Alternativas: Média Geométrica das três primeiras Ordenações", fontdict={'fontsize':15}) #adicionando título
                ax.set_xlabel('Valores', fontdict={'fontsize':14}) #mudando e nome e tamanho do label x
                ax.set_ylabel('Alternativas', fontdict={'fontsize':14}) #mudando tamanho do label eixo y
                ax.tick_params(labelsize=14) #mudando tamanho dos labels dos ticks
                ax.spines['bottom'].set_linewidth(2.5) #aumentando espessura linha inferior
                plt.grid(False)          #tirar as linhas Brancas da grade

                for axis in ['top', 'right', 'left']: #remoção dos outros três axis
                    ax.spines[axis].set_color(None)
                ax.tick_params(axis='x', labelleft=False, left=None) #remoção dos ticks

                #colocando rótulo no gráfico
                rotulo_grafico2 = lista_final_n_5n 
                for index, value in enumerate(lista_final_n_5n): 
                    plt.text(value, index, 
                            str(round(value,4)))

                #otimizar espaço da figure
                fig_GRA5N.tight_layout()
    #=========================================================================================
    #=========================================================================================
    #=========================================================================================
    #=========================================================================================

                #=-=-=--=-=--==-=--= Apresentando todos os valores (NORMALIZADOS) em um único DataFrame =-=---=-=--=-
                #=-=--=-=-=-=-=-=--==-=-=-=-=-=-=-=-=- Resultado Finais Normalizados =--=-=-=-=--==-=--=
                Resultado_final_n = final.assign(Res_2 = criterio_eixo_grafico_2n, GRA_2N = lista_final_2n, Ord_2 = ord_2,
                                Res_3 = criterio_eixo_grafico_3n, Peso_2N = lista_final_3n, Ord_3 = ord_3n,
                                Res_4 = criterio_eixo_grafico_n_4n, Média_Ar = lista_final_n_4n, Ord_4 = ord_4n,
                                Res_5 = criterio_eixo_grafico_n_5n, Média_Geo = lista_final_n_5n, Ord_5 = ord_5n)#, allow_duplicates=False)          #ordenação = ord_4n, carlota = '5' )
                #st.write('DataFrame com todos os resultados Compilados:', Resultado_final_n)
                
                st.write('')
                st.write('')
                st.write('')
                st.write('')
                col1, col2, col3 = st.columns([1,2,1])
                with col2:
                    if st.session_state.botao_inclusao_da_matriz == 0:
                        st.write('Após incluir todos os valores para matriz, click no botâo: "Confirmar os valores inseridos."')
                    else:
                        st.markdown("<h3 style = 'text-align: center;'>Escolha 'Sim' para calcular o resultado:</h3>", unsafe_allow_html=True)
                        resultado_selectbox = st.selectbox('', ['Sim', 'Não'], key='resultado_selebox1', index=1)
                        st.write('')
                if resultado_selectbox == 'Sim':
                    st.write('')
                    st.markdown(f"<h2 style = 'text-align: center;'>Resultados Obtidos para o Trabalho:</h2>", unsafe_allow_html=True)
                    st.markdown(f"<h2 style = 'text-align: center;'>'{trabalho}'</h2>", unsafe_allow_html=True)
                    f'''
                    #### A seguir vc encontrará as abas com os resultados obtidos pelo método, na seguinte distribuição:
                    - Etapa 1 - Os valores relacioanos ao Método CRITIC - Peso dos Critérios;
                    - Etapa 2 - Primeira Ordenação - O resultado da ordenação do método CRITIC-GRA;
                    - Etapa 3 - Segunda Ordenação  - O resultado da ordenação do método CRITIC-GRA - 2ª Normalização;
                    - Etapa 4 - Terceira Ordenação - O resultado da ordenação do ponderação da 2ª Normalização com CRITIC;
                    - Etapa 5 - Quarta Ordenação   - O resultado da Média Aritmética das três primeiras ordenações normalizadas;
                    - Etapa 6 - Quinta Ordenação   - O resultado da Média Gométrica das três primeiras ordenações normalizadas;
                    - Gráficos dos resultados - Apresenta todos os Gráficos para o peso e ordenações; e
                    - Resultado - Apresenta uma matriz com a junção dos cinco resultados para facilitar na compreenção.
                    '''
                    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([ 
                                                    "📊 Etapa 1",
                                                    "📊 Etapa 2",
                                                    "📊 Etapa 3", 
                                                    "📊 Etapa 4",
                                                    "📊 Etapa 5",
                                                    "📊 Etapa 6",                                                                                                
                                                    "📈 Gráficos dos Resultados", 
                                                    "💻 Resultado"])
                    with tab1:
                        #'''### Nessa página é apresentado os valores dos pesos e seu respectivo grafico.''' 
                        st.markdown(f"<h2 style = 'text-align: center;'>Valores relacioanos ao Método CRITIC - Peso dos Critérios</h2>", unsafe_allow_html=True)
                        with st.expander('Matriz inicial utilizada:'):
                            st.write(df2)
                        #st.write('Matriz inicial utilizada: ', df2)
                        df_lista_max = pd.DataFrame(lista_valormax, index = lista_criterios, columns = ['Valores Máximos por Critério'])
                        with st.expander('Valor do vetor dos valores MAX dos Critérios:'):
                            st.write(df_lista_max)
                        #st.write('Valor do vetor dos valores MAX dos Critérios:', df_lista_max)
                        df_lista_min = pd.DataFrame(lista_valormin, index = lista_criterios, columns = ['Valores Mínimos por Critério'])
                        with st.expander('Valor do vetor dos valores MIN dos Critérios:'):
                            st.write(df_lista_min)
                        #st.write('Valor do vetor dos valores MIN dos Critérios:', df_lista_min)
                        with st.expander('Matriz Normalizada:'):
                            st.write(teste_2)
                        #st.write('Matriz Normalizada:', teste_2)
                        with st.expander('Matriz Correlação:'):
                            st.write(correl)
                        #st.write('Matriz Correlação:', correl)
                        with st.expander('Gráfico da Correlação dos Critérios'):
                            st.pyplot(fig_correl)
                        #st.write('Matriz um menos Matriz Correlação', um_menos_correl)
                        with st.expander('Matriz um menos Matriz Correlação:'):
                            st.write(um_menos_correl)
                        #st.write('Coluna Soma da Matriz Um Menos Correlação:', soma_correl)
                        with st.expander('Coluna Soma da Matriz Um Menos Correlação:'):
                            st.write(soma_correl)
                        
                        #st.write('Desvio Padrão sobre a Matriz Normalizada:', desvio)
                        with st.expander('Desvio Padrão sobre a Matriz Normalizada:'):
                            st.write(desvio)
                        #st.write('Índice C:', indice_c)
                        with st.expander('Índice C:'):
                            st.write(indice_c)
                        #st.write('Soma dos valores do Índice C:', soma_indice_c)
                        with st.expander('Soma dos valores do Índice C:'):
                            st.write(soma_indice_c)
                        st.markdown("<h3 style = 'text-align: center;'>Resultado do Peso dos Critérios:</h3>", unsafe_allow_html=True)
                        col1, col2, col3 = st.columns([1,2,1])
                        peso_nome = pd.DataFrame(peso, columns = ['Peso Critérios'])
                        col2.write(peso_nome)
                        with st.expander('Gráfico do Peso dos Critérios'):
                            st.pyplot(fig_peso)
                    
                        peso_excel = io.BytesIO()
                        # Create a Pandas Excel writer using XlsxWriter as the engine.
                        with pd.ExcelWriter(peso_excel, engine='xlsxwriter') as writer:
                            # Write each dataframe to a different worksheet.
                            peso_nome.to_excel(writer, sheet_name='Resultado Peso dos Critérios')
                            df2.to_excel(writer, sheet_name='Matriz inicial utilizada')
                            df_lista_max.to_excel(writer, sheet_name='Matriz inicial utilizada', startrow = n_alternativas + 4)
                            df_lista_min.to_excel(writer, sheet_name='Matriz inicial utilizada', startrow = n_alternativas + 4, startcol = 6)
                            teste_2.to_excel(writer, sheet_name='Matriz Normalizada')
                            correl.to_excel(writer, sheet_name='Matriz Correlação')
                            um_menos_correl.to_excel(writer, sheet_name='Um menos Matriz Correlação')
                            soma_correl.to_excel(writer, sheet_name='Soma Matriz Um Menos Correl')
                            desvio.to_excel(writer, sheet_name='Desvio Padrão Matriz Normal')
                            indice_c.to_excel(writer, sheet_name='Índice C')
                            soma_indice_c = pd.DataFrame([soma_indice_c], index = ['Somatório'], columns = ['Soma Índice C'])
                            soma_indice_c.to_excel(writer, sheet_name='Índice C', startrow = n_criterios + 3)

                            # Close the Pandas Excel writer and output the Excel file to the buffer
                            writer.save()
                            st.markdown("<h3 style = 'text-align: center;'>Para Baixar todas as Matrizes, em um só documento, clique no botão:</h3>", unsafe_allow_html=True)
                            col1, col2, col3 = st.columns(3)
                            with col2:
                                st.download_button(
                                label="Peso Critérios  Download",
                                data=peso_excel,
                                file_name=f"Trabalho '{trabalho}'_Pesos Critérios.xlsx",
                                mime="application/vnd.ms-excel"
                                )

                            st.write('')

                    with tab2:
                        st.markdown(f"<h2 style = 'text-align: center;'>Resultado da ordenação do método CRITIC-GRA</h2>", unsafe_allow_html=True)
                        #'''### Nessa página é apresentado, detalhadamente, os DataFrame utilizados para cálcular o peso e as Ordenações das Alternativas para cada método. '''
                        with st.expander('Matriz inicial utilizada:'):
                            st.write(df2)
                        #st.write('Matriz inicial utilizada: ', df2)
                        #st.write('')
                        with st.expander('Valor do Coeficiente de Distinção:'):
                            st.write(coeficiente_dist)
                        #st.write('Valor do Coeficiente de Distinção: ', coeficiente_dist)
                        #st.write('')
                        df_lista_max_1 = pd.DataFrame(lista_valormax_1, index = lista_criterios, columns = ['Valores Máximos por Critério'])
                        with st.expander('Valor do vetor dos valores MAX dos Critérios:'):
                            st.write(df_lista_max_1)
                        #st.write('Valor do vetor dos valores MAX dos Critérios:', df_lista_max_1)
                        #st.write('')
                        df_lista_min_1 = pd.DataFrame(lista_valormin_1, index = lista_criterios, columns = ['Valores Mínimos por Critério'])
                        with st.expander('Valor do vetor dos valores MIN dos Critérios:'):
                            st.write(df_lista_min_1)
                        #st.write('Valor do vetor dos valores MIN dos Critérios:', df_lista_min_1)
                        #st.write('')
                        with st.expander('Matriz Normalizada:'):
                            st.write(teste_2)
                        #st.write('Matriz Normalizada:', teste_2)
                        #st.write('')
                        df_matriz_seq_desvio = pd.DataFrame(matriz_seq_des, index=lista_alternativas, columns=lista_criterios)
                        with st.expander('Matriz Sequência de Desvios:'):
                            st.write(df_matriz_seq_desvio)
                        #st.write('Matriz Sequência de Desvios: ', df_matriz_seq_desvio)
                        #st.write('')
                        df_lista_valor_max_seq = pd.DataFrame(matriz_seq_des, columns=lista_criterios).max()
                        df_lista_valor_max_seq = pd.DataFrame(df_lista_valor_max_seq, columns = ['Valores MÁX'])
                        with st.expander('Valor do vetor dos valores MAX dos Critérios da Matriz Sequência de Desvio:'):
                            st.write(df_lista_valor_max_seq)
                        #st.write('Valor do vetor dos valores MAX dos Critérios da Matriz Sequência de Desvio:', df_lista_valor_max_seq)
                        #st.write('')
                        df_lista_valor_min_seq = pd.DataFrame(matriz_seq_des, columns=lista_criterios).min()
                        df_lista_valor_min_seq = pd.DataFrame(df_lista_valor_min_seq, columns = ['Valores MIN'])
                        with st.expander('Valor do vetor dos valores MIN dos Critérios da Matriz Sequência de Desvio:'):
                            st.write(df_lista_valor_min_seq)
                        #st.write('Valor do vetor dos valores MIN dos Critérios da Matriz Sequência de Desvio:', df_lista_valor_min_seq)
                        #st.write('')
                        df_matriz_coe = pd.DataFrame(data=matriz_coe, index=lista_alternativas, columns=lista_criterios)
                        col1, col2 = st.columns([3,1])
                        with col1:
                            #st.write('Coeficiente Relacional Cinza: ', df_matriz_coe)
                            with st.expander('Coeficiente Relacional Cinza:'):
                                st.write(df_matriz_coe)
                        with col2:
                            #st.write('Peso dos Critérios:', peso)
                            with st.expander('Peso dos Critérios:'):
                                st.write(peso)
                            with st.expander('Gráfico do Peso dos Critérios'):
                                st.pyplot(fig_peso)
                        #st.write('Matriz Ponderada: ', matriz_grad)
                        df_matriz_grad = pd.DataFrame(matriz_grad, index = lista_alternativas, columns = lista_criterios)
                        with st.expander('Matriz Ponderada:'):
                                st.write(df_matriz_grad)
                    # df_matriz_grad = pd.DataFrame(matriz_grad, index=lista_alternativas, columns=lista_criterios)
                    # st.write('Grade Relacional Cinza:', df_matriz_grad)
                        with st.expander('GRADE RELACIONAL CINZA:'):
                                st.write(resultado)
                        #st.write('GRADE RELACIONAL CINZA :', resultado)
                        st.markdown("<h3 style = 'text-align: center;'>Primeira Ordenação - Resultado CRITIC-GRA:</h3>", unsafe_allow_html=True)
                        col1, col2, col3 = st.columns([1,3,1])
                        col2.write(final)
                        with st.expander('Grafico das Alternatvas pelo 1º Método - CRITIC-GRA:'):
                            st.pyplot(fig_GRA)
                        #st.write('Primeira Ordenação - Resultado CRITIC-GRA: ', final)
                        
                        GRA_excel = io.BytesIO()
                        # Create a Pandas Excel writer using XlsxWriter as the engine.
                        with pd.ExcelWriter(GRA_excel, engine='xlsxwriter') as writer:
                            # Write each dataframe to a different worksheet.
                            final.to_excel(writer, sheet_name='Primeira Ordenação-CRITIC-GRA')
                            df2.to_excel(writer, sheet_name='Matriz inicial utilizada')
                            df_lista_max_1.to_excel(writer, sheet_name='Matriz inicial utilizada', startrow = n_alternativas + 4)
                            df_lista_min_1.to_excel(writer, sheet_name='Matriz inicial utilizada', startrow = n_alternativas + 4, startcol = 6)
                            teste_2.to_excel(writer, sheet_name='Matriz Normalizada')
                            df_matriz_seq_desvio.to_excel(writer, sheet_name='Matriz Sequência de Desvios')
                            df_lista_valor_max_seq.to_excel(writer, sheet_name='Matriz Sequência de Desvios', startrow = n_alternativas + 4)
                            df_lista_valor_min_seq.to_excel(writer, sheet_name='Matriz Sequência de Desvios', startrow = n_alternativas + 4, startcol = 7)
                            coeficiente_dist = pd.DataFrame([coeficiente_dist], index = ['Valor'], columns = ['Coeficiente de Distinção'])
                            coeficiente_dist.to_excel(writer, sheet_name='Matriz Sequência de Desvios', startrow = n_alternativas + 4, startcol = 4)
                            df_matriz_coe.to_excel(writer, sheet_name='Matriz Ponderada')
                            #peso.columns('Peso Critérios')
                            peso_nome.to_excel(writer, sheet_name='Matriz Ponderada', startcol= n_criterios + 2 )
                            df_matriz_grad.to_excel(writer, sheet_name='Matriz Ponderada', startrow = n_alternativas + 4)
                            resultado.to_excel(writer, sheet_name='GRADE RELACIONAL CINZA')
                            
                            # Close the Pandas Excel writer and output the Excel file to the buffer
                            writer.save()
                            st.markdown("<h3 style = 'text-align: center;'>Para Baixar todas as Matrizes, em um só documento, clique no botão:</h3>", unsafe_allow_html=True)
                            col1, col2, col3 = st.columns(3)
                            with col2:
                                st.download_button(
                                label="Primeira Ordenação  Download",
                                data=GRA_excel,
                                file_name=f"Trabalho '{trabalho}'_Primeira Ordenação.xlsx",
                                mime="application/vnd.ms-excel"
                                )

                            st.write('')

                    with tab3:
                        st.markdown(f"<h2 style = 'text-align: center;'>Resultado da ordenação do método CRITIC-GRA - 2ª Normalização</h2>", unsafe_allow_html=True)
                        st.write('OBS.:')
                        st.write('Para Segunda Ordenação será realizado a 2ªNormalização e será rodado todo o método GRA novamente.')
                        st.write('')
                        st.write('')
                        with st.expander('Matriz inicial utilizada para 2Normalização com valores negativos para Critérios com indicativo de Custo:'):
                            st.write(matriz_sinal_pd)
                        #st.write('Matriz inicial utilizada para 2Normalização com valores negativos para Critérios com indicativo de Custo: ', matriz_sinal_pd)
                        with st.expander('Calculando a Média dos Critérios:'):
                            med_matriz_sinal = pd.DataFrame(med_matriz_sinal, columns = ['Média dos critérios'])
                            st.write(med_matriz_sinal)
                        #st.write('Calculando a Média dos Critérios:', med_matriz_sinal)
                        with st.expander('Calculando o Desvio Padrão:'):
                            des_matriz_sinal = pd.DataFrame(des_matriz_sinal, columns = ['Desvio Padrão dos Critérios'])
                            st.write(des_matriz_sinal)
                        #st.write('Calculando o Desvio Padrão:', des_matriz_sinal)
                        with st.expander('Segunda Normalização = Distribuição Normal para cada item Xij'):
                            st.write(Ç)
                        #st.write('Segunda Normalização = Distribuição Normal para cada item Xij', Ç)
                        with st.expander('Matriz Sequência de Desvios 2ª Normalização:'):
                            st.write(matriz_seq_des_2n)
                        #st.write('Matriz Sequência de Desvios 2ª Normalização: ', matriz_seq_des_2n)
                        with st.expander('Valor do vetor dos valores MAX dos Critérios da Matriz Sequência de Desvio'):
                            lista_max2n = pd.DataFrame(lista_max2n, columns = ['Valores MAX'])
                            st.write(lista_max2n)
                        #st.write('Valor do vetor dos valores MAX dos Critérios da Matriz Sequência de Desvio', lista_max2n)
                        with st.expander('Valor do vetor dos valores MIN dos Critérios da Matriz Sequência de Desvio'):
                            lista_min2n = pd.DataFrame(lista_min2n, columns = ['Valores MIN'])
                            st.write(lista_min2n)
                        #st.write('Valor do vetor dos valores MIN dos Critérios da Matriz Sequência de Desvio', lista_min2n)
                        col1, col2 = st.columns([2,1])
                        with col1:
                            with st.expander('Coeficiente Relacional Cinza 2ª Normalização:'):
                                st.write(matriz_coe_2n)
                            #st.write('Coeficiente Relacional Cinza 2ª Normalização:', matriz_coe_2n)
                        with col2:
                            with st.expander('Peso dos Critérios:'):
                                st.write(peso)
                            with st.expander('Gráfico do Peso dos Critérios:'):
                                st.write(fig_peso)
                            #st.write('Peso dos Critérios:', peso)
                        with st.expander('Matriz Ponderada com a Segunda Normalização:'):
                            st.write(matriz_grad_2n)
                        #st.write('Matriz Ponderada com a Segunda Normalização:', matriz_grad_2n)
                        with st.expander('GRADE RELACIONAL CINZA - 2ª Normalização:'):
                            st.write(resultado_2n)
                        #st.write('GRADE RELACIONAL CINZA - 2ª Normalização:', resultado_2n)
                        st.markdown("<h3 style = 'text-align: center;'>Segunda Ordenação - Resultado CRITIC-GRA:</h3>", unsafe_allow_html=True)
                        col1, col2, col3 = st.columns([1,3,1])
                        col2.write(final_2n)
                        with st.expander('Grafico das Alternatvas pelo 2º Método - CRITIC-GRA - 2ª Normalização:'):
                            st.pyplot(fig_GRA2N)
                        #st.write('Segunda Ordenação - Resultado CRITIC-GRA: ', final_2n)
                        
                        GRA2N_excel = io.BytesIO()
                        # Create a Pandas Excel writer using XlsxWriter as the engine.
                        with pd.ExcelWriter(GRA2N_excel, engine='xlsxwriter') as writer:
                            # Write each dataframe to a different worksheet.
                            final_2n.to_excel(writer, sheet_name='Segunda Ordenação-CRITIC-GRA')
                            matriz_sinal_pd.to_excel(writer, sheet_name='Matriz inicial valores neg')
                            med_matriz_sinal.columns = ['Média dos Critérios']
                            med_matriz_sinal.to_excel(writer, sheet_name='Matriz inicial valores neg', startrow = n_alternativas + 4)
                            des_matriz_sinal.columns = ['Desvio Padrão']
                            des_matriz_sinal.to_excel(writer, sheet_name='Matriz inicial valores neg', startrow = n_alternativas + 4, startcol = 6)
                            Ç.to_excel(writer, sheet_name='2ª Normalização = Distrib Norm')
                            matriz_seq_des_2n.to_excel(writer, sheet_name='Matriz Seq de Desvios 2ª Norm')
                            lista_max2n.to_excel(writer, sheet_name='Matriz Seq de Desvios 2ª Norm', startrow = n_alternativas + 4)
                            lista_min2n.to_excel(writer, sheet_name='Matriz Seq de Desvios 2ª Norm', startrow = n_alternativas + 4, startcol = 7)
                            coeficiente_dist.to_excel(writer, sheet_name='Matriz Seq de Desvios 2ª Norm', startrow = n_alternativas + 4, startcol = 4)
                            matriz_coe_2n.to_excel(writer, sheet_name='Matriz Ponderada 2ª Norm')
                            peso_nome.to_excel(writer, sheet_name='Matriz Ponderada 2ª Norm', startcol= n_criterios + 2 )
                            matriz_grad_2n.to_excel(writer, sheet_name='Matriz Ponderada 2ª Norm', startrow = n_alternativas + 4)
                            resultado_2n.to_excel(writer, sheet_name='GRADE RELACIONAL CINZA')
                            
                            # Close the Pandas Excel writer and output the Excel file to the buffer
                            writer.save()
                            st.markdown("<h3 style = 'text-align: center;'>Para Baixar todas as Matrizes, em um só documento, clique no botão:</h3>", unsafe_allow_html=True)
                            col1, col2, col3 = st.columns(3)
                            with col2:
                                st.download_button(
                                label="Segunda Ordenação  Download",
                                data=GRA2N_excel,
                                file_name=f"Trabalho '{trabalho}'_Segunda Ordenação.xlsx",
                                mime="application/vnd.ms-excel"
                                )
                            st.write('')

                    with tab4:
                        st.markdown(f"<h2 style = 'text-align: center;'>Resultado da ordenação da ponderação da 2ª Normalização com CRITIC</h2>", unsafe_allow_html=True)
                        #tab2.subheader("Método 2Normalização com CRITIC")
                        st.write('OBS.:')
                        st.write('Para Terceira Ordenação será utilizado a 2ªNormalização e será ponderado com o peso calculado pelo CRITIC')
                        st.write('')
                        with st.expander('Matriz inicial utilizada para 2Normalização com valores negativos para Critérios com indicativo de Custo:'):
                            st.write(matriz_sinal_pd)
                        #st.write('Matriz inicial utilizada para 2Normalização com valores negativos para Critérios com indicativo de Custo: ', matriz_sinal_pd)
                        col1, col2 = st.columns([3,1])
                        with col1:
                            with st.expander('Matriz Normalizada com a 2ª Normalização:'):
                                st.write(dist_normal_pd)
                            #st.write('Matriz Normalizada com a 2ª Normalização: ', dist_normal_pd)
                        with col2:
                            with st.expander('Peso dos Critérios:'):
                                st.write(peso)
                            with st.expander('Gráfico do Peso dos Critérios:'):
                                st.write(fig_peso)
                            #st.write('Peso dos Critérios:', peso)
                        with st.expander('Matriz Ponderada com a Segunda Normalização:'):
                                st.write(matriz_grad_3n)
                        #st.write('Matriz Ponderada com a Segunda Normalização:: ', matriz_grad_3n)
                        with st.expander('GRADE RELACIONAL CINZA - 2ª Normalização:'):
                                st.write(resultado_3n)
                        #st.write('GRADE RELACIONAL CINZA - 2ª Normalização:', resultado_3n)
                        st.markdown("<h3 style = 'text-align: center;'>Terceira Ordenação - Resultado 2ªNormalização com CRITIC:</h3>", unsafe_allow_html=True)
                        col1, col2, col3 = st.columns([1,3,1])
                        col2.write(final_3n)
                        with st.expander('Grafico das Alternatvas pelo 3º Método - 2ªNormalização com CRITIC:'):
                            st.pyplot(fig_GRA3N)
                        #st.write('Terceira Ordenação - Resultado 2ªNormalização com CRITIC: ', final_3n)

                        GRA3N_excel = io.BytesIO()
                        # Create a Pandas Excel writer using XlsxWriter as the engine.
                        with pd.ExcelWriter(GRA3N_excel, engine='xlsxwriter') as writer:
                            # Write each dataframe to a different worksheet.
                            final_3n.to_excel(writer, sheet_name='3ª Ordenação-2ªNormal-CRITIC')
                            matriz_sinal_pd.to_excel(writer, sheet_name='Matriz inicial valores neg')
                            dist_normal_pd.to_excel(writer, sheet_name='Matriz 2ª Normalização')
                            dist_normal_pd.to_excel(writer, sheet_name='Matriz Ponderada 3ª Ord')
                            peso_nome.to_excel(writer, sheet_name='Matriz Ponderada 3ª Ord', startcol= n_criterios + 2 )
                            matriz_grad_3n.to_excel(writer, sheet_name='Matriz Ponderada 3ª Ord', startrow = n_alternativas + 4)
                            resultado_3n.to_excel(writer, sheet_name='GRADE RELACIONAL CINZA')
                            
                            # Close the Pandas Excel writer and output the Excel file to the buffer
                            writer.save()
                            st.markdown("<h3 style = 'text-align: center;'>Para Baixar todas as Matrizes, em um só documento, clique no botão:</h3>", unsafe_allow_html=True)
                            col1, col2, col3 = st.columns(3)
                            with col2:
                                st.download_button(
                                label="Terceira Ordenação  Download",
                                data=GRA3N_excel,
                                file_name=f"Trabalho '{trabalho}'_Terceira Ordenação.xlsx",
                                mime="application/vnd.ms-excel"
                                )
                            st.write('')

                    with tab5:
                        st.markdown(f"<h2 style = 'text-align: center;'>Média Aritmética das três primeiras ordenações normalizadas</h2>", unsafe_allow_html=True)
                        #tab2.subheader("Média Aritmética das três primeiras ordenações normalizadas")
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            with st.expander('1ª Ordenação:'):
                                st.write(resultado)
                            with st.expander('Normalização da 1ª Ordenação:'):
                                st.write(normaliza_1)
                            #st.write('1ª Ordenação:', resultado)
                            #st.write('Normalização da 1ª Ordenação', normaliza_1) 
                        with col2:
                            with st.expander('2ª Ordenação:'):
                                st.write(resultado_2n)
                            with st.expander('Normalização da 2ª Ordenação:'):
                                st.write(normaliza_2)
                            #st.write('2ª Ordenação:', resultado_2n)
                            #st.write('Normalização da 2ª Ordenação', normaliza_2)
                        with col3:
                            with st.expander('3ª Ordenação:'):
                                st.write(resultado_3n)
                            with st.expander('Normalização da 3ª Ordenação:'):
                                st.write(normaliza_3)
                            #st.write('3ª Ordenação:', resultado_3n)
                            #st.write('')
                            #st.write('Normalização da 3ª Ordenação', normaliza_3)
                        with st.expander('Média Aritmética das alternativas Normalizadas:'):
                                st.write(resultado_n_4n)
                        #st.write('Média Aritmética das alternativas Normalizadas:', resultado_n_4n)
                        st.markdown("<h3 style = 'text-align: center;'>Quarta Ordenação - Resultado Média Aritmética:</h3>", unsafe_allow_html=True)
                        col1, col2, col3 = st.columns([1,3,1])
                        col2.write(final_n_4n)
                        with st.expander('Grafico das Alternatvas pelo 4º Método - Média Aritmética:'):
                            st.pyplot(fig_GRA4N)
                        #st.write('Ordenação Decrescente dos Resultados da 4ª Ordenação:', final_n_4n)
                        
                        GRA4N_excel = io.BytesIO()
                        # Create a Pandas Excel writer using XlsxWriter as the engine.
                        with pd.ExcelWriter(GRA4N_excel, engine='xlsxwriter') as writer:
                            # Write each dataframe to a different worksheet.
                            final_n_4n.to_excel(writer, sheet_name='4ª Ordenação-Média Aritmética')
                            resultado.to_excel(writer, sheet_name='Normalização 3 primeiras Ord')
                            normaliza_1.to_excel(writer, sheet_name='Normalização 3 primeiras Ord', startrow = n_alternativas + 3)
                            resultado_2n.to_excel(writer, sheet_name='Normalização 3 primeiras Ord', startcol = 4)
                            normaliza_2.to_excel(writer, sheet_name='Normalização 3 primeiras Ord', startrow = n_alternativas + 3, startcol = 4)
                            resultado_3n.to_excel(writer, sheet_name='Normalização 3 primeiras Ord', startcol = 8)
                            normaliza_3.to_excel(writer, sheet_name='Normalização 3 primeiras Ord', startrow = n_alternativas + 3, startcol = 8)
                            resultado_n_4n.to_excel(writer, sheet_name='Média Aritmética das Alt')
                                                    
                            # Close the Pandas Excel writer and output the Excel file to the buffer
                            writer.save()
                            st.markdown("<h3 style = 'text-align: center;'>Para Baixar todas as Matrizes, em um só documento, clique no botão:</h3>", unsafe_allow_html=True)
                            col1, col2, col3 = st.columns(3)
                            with col2:
                                st.download_button(
                                label="Quarta Ordenação  Download",
                                data=GRA4N_excel,
                                file_name=f"Trabalho '{trabalho}'_Quarta Ordenação.xlsx",
                                mime="application/vnd.ms-excel"
                                )
                            st.write('')

                    with tab6:
                        st.markdown(f"<h2 style = 'text-align: center;'>Média Geométrica das três primeiras ordenações normalizadas</h2>", unsafe_allow_html=True)
                        #tab2.subheader("Média Aritmética das três primeiras ordenações normalizadas")
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            with st.expander('1ª Ordenação:'):
                                st.write(resultado)
                            with st.expander('Normalização da 1ª Ordenação:'):
                                st.write(normaliza_1)
                            #st.write('1ª Ordenação:', resultado)
                            #st.write('')
                            #st.write('Normalização da 1ª Ordenação', normaliza_1) 
                        with col2:
                            with st.expander('2ª Ordenação:'):
                                st.write(resultado_2n)
                            with st.expander('Normalização da 2ª Ordenação:'):
                                st.write(normaliza_2)
                            #st.write('2ª Ordenação:', resultado_2n)
                            #st.write('')
                            #st.write('Normalização da 2ª Ordenação', normaliza_2)
                        with col3:
                            with st.expander('3ª Ordenação:'):
                                st.write(resultado_3n)
                            with st.expander('Normalização da 3ª Ordenação:'):
                                st.write(normaliza_3)
                        with st.expander('Média Geométrica das alternativas Normalizadas::'):
                                st.write(resultado_n_5n)
                        st.markdown("<h3 style = 'text-align: center;'>Quinta Ordenação - Resultado Média Geométrica:</h3>", unsafe_allow_html=True)
                        col1, col2, col3 = st.columns([1,3,1])
                        col2.write(final_n_5n)
                        with st.expander('Grafico das Alternatvas pelo 5º Método - Média Geométrica:'):
                            st.pyplot(fig_GRA5N)

                        GRA5N_excel = io.BytesIO()
                        # Create a Pandas Excel writer using XlsxWriter as the engine.
                        with pd.ExcelWriter(GRA5N_excel, engine='xlsxwriter') as writer:
                            # Write each dataframe to a different worksheet.
                            final_n_5n.to_excel(writer, sheet_name='5ª Ordenação-Média Geométrica')
                            resultado.to_excel(writer, sheet_name='Normalização 3 primeiras Ord')
                            normaliza_1.to_excel(writer, sheet_name='Normalização 3 primeiras Ord', startrow = n_alternativas + 3)
                            resultado_2n.to_excel(writer, sheet_name='Normalização 3 primeiras Ord', startcol = 4)
                            normaliza_2.to_excel(writer, sheet_name='Normalização 3 primeiras Ord', startrow = n_alternativas + 3, startcol = 4)
                            resultado_3n.to_excel(writer, sheet_name='Normalização 3 primeiras Ord', startcol = 8)
                            normaliza_3.to_excel(writer, sheet_name='Normalização 3 primeiras Ord', startrow = n_alternativas + 3, startcol = 8)
                            resultado_n_5n.to_excel(writer, sheet_name='Média Geométrica das Alt')
                                                    
                            # Close the Pandas Excel writer and output the Excel file to the buffer
                            writer.save()
                            st.markdown("<h3 style = 'text-align: center;'>Para Baixar todas as Matrizes, em um só documento, clique no botão:</h3>", unsafe_allow_html=True)
                            col1, col2, col3 = st.columns(3)
                            with col2:
                                st.download_button(
                                label="Quinta Ordenação  Download",
                                data=GRA5N_excel,
                                file_name=f"Trabalho '{trabalho}'_Quinta Ordenação.xlsx",
                                mime="application/vnd.ms-excel"
                                )
                            st.write('')
            
                    with tab7:        
                        st.markdown(f"<h2 style = 'text-align: center;'>Apresentação Gráfica dos Resultados</h2>", unsafe_allow_html=True)
                        #'''### Nessa página é apresentado os gráficos das Ordenações para cada operação.''' 
                        #tab3.subheader('Nessa página é apresentado os gráficos das Ordenações para cada operação')
                        #st.write('Obs.:')
                        #st.write('Caso deseje guardar a imagem do gráfico, apenas click nos tres pontos ao lado e acesse a o item download.')
                        with st.expander('Grafico da Correlação dos Criterios:'):
                            st.pyplot(fig_correl)
                        with st.expander('Grafico dos Pesos dos Critérios:'):
                            st.pyplot(fig_peso)
                        with st.expander('Grafico das Alternatvas pelo 1º Método - CRITIC-GRA:'):
                            st.pyplot(fig_GRA)
                        with st.expander('Grafico das Alternatvas pelo 2º Método - CRITIC-GRA (2Normalização):'):
                            st.pyplot(fig_GRA2N)
                        with st.expander('Grafico das Alternatvas pelo 3º Método - 2ºNormal-CRITIC:'):
                            st.pyplot(fig_GRA3N)
                        with st.expander('Grafico das Alternatvas pelo 4º Método - Média Aritmética:'):
                            st.pyplot(fig_GRA4N)
                        with st.expander('Grafico das Alternatvas pelo 5º Método - Média Geométrica:'):
                            st.pyplot(fig_GRA5N)

                    with tab8:
                        st.markdown(f"<h2 style = 'text-align: center;'>DataFrame com todos os resultados Compilados, para o Tabralho '{trabalho}':</h2>", unsafe_allow_html=True)
                        #tab4.subheader(f'DataFrame com todos os resultados Compilados, para o Tabralho {trabalho}:')
                        st.write(Resultado_final_n)
                        #col1, col2, col3 = st.columns([1,2,1])
                        #with col2:
                        
                        GRA6N_excel = io.BytesIO()
                        # Create a Pandas Excel writer using XlsxWriter as the engine.
                        with pd.ExcelWriter(GRA6N_excel, engine='xlsxwriter') as writer:
                            # Write each dataframe to a different worksheet.
                            Resultado_final_n.to_excel(writer, sheet_name='Resultados Compilados')
                                                                            
                            # Close the Pandas Excel writer and output the Excel file to the buffer
                            writer.save()
                            st.markdown("<h3 style = 'text-align: center;'>Para Baixar o Resultado Compilado das Ordenações, em um só documento, clique no botão:</h3>", unsafe_allow_html=True)
                            col1, col2, col3 = st.columns(3)
                            with col2:
                                st.download_button(
                                label="Resultados Compilados  Download",
                                data=GRA6N_excel,
                                file_name=f"Trabalho '{trabalho}'_Resultados Compilados.xlsx",
                                mime="application/vnd.ms-excel"
                                )
                            st.write('')
                        st.balloons()

if pagina == 'Sobre':
    ''' #### Esse método é utlizado para dar apoio ao tomador de decisão gerando peso, pelo "CRiteria Importance Through Intercriteria Correlation" (CRTIC), para cada critério escolhido, em seguida ordena as alternativas, pelo "Grey Relational Analysis" (GRA), utilizando três normalizações diferentes no processo. 

    Ao final, será entregue cinco ordenações seguindo a sequência:
    - 1ª - CRITIC-GRA;
    - 2ª - CRITIC-GRA com a 2ªNormalização;
    - 3ª - Ponderação da Matriz normalizada com a 2ªNormalização e o peso;
    - 4ª - Média Aritmética das três primeiras ordenações Normalizadas; e
    - 5ª - Média Geométrica das três primeiras ordenações Normalizadas. 
    '''

    #### Para cumprir o método CRITIC-GRA-3N, serão executadas algumas etapas, são elas:
    st.markdown(f"<h3 style = 'text-align: center;'>Para cumprir o método CRITIC-GRA-3N, serão executadas algumas etapas, são elas:</h3>", unsafe_allow_html=True)
    '''
    - 1º Definição da Matriz de Decisão;
    - 2º Definir os critérios monotônicos de Custo e de Lucro;
    - 3º Aplicar o método CRITIC para obtenção dos pesos dos critérios;
    - 4º Aplicar o método GRA para obter a primeira ordenação;
    - 5º Aplicar o método GRA com a segunda normalização, utilizando os pesos gerados pelo método CRITIC, obtendo a segunda ordenação;
    - 6º Utilizar a soma dos produtos da matriz gerada pela segunda normalização com os pesos gerados pelo método CRITIC, obtendo a terceira ordenação;
    - 7º Normalizar as três primeiras ordenações, com a terceira normalização, e ao final realizar a Média Aritmética para cada alternativa;
    - 8º Normalizar as três primeiras ordenações, com a terceira normalização, e ao final realizar a Média Geométrica para cada alternativa.
    '''
    
    st.markdown(f"<h3 style = 'text-align: center;'>Para Citar este site:</h3>", unsafe_allow_html=True)
    st.markdown(f"<h6 style = 'text-align: center;'>Almeida, Isaque David Pereira; Hermogenes, Lucas Ramon dos Santos; Gomes, Carlos Francisco Simões.; Santos, Marcos dos. \nCRITIC-GRA-3N (CG-3N) For Decision Making (v1), Universidade Federal Fluminense, Niterói, Rio de Janeiro, 2022.</h6>", unsafe_allow_html=True)
    st.write('')
    st.markdown(" ##### Caso deseje adquirir conteúdo de qualidade sobre dezenas de outros métodos para apoio a tomada de decisão, aprendendo passo-a-passo como utiliza-los, acesse: ")
    st.markdown(" #### *Casa da Pesquisa Operacional* - [Youtube](https://www.youtube.com/c/CasadaPesquisaOperacional)")


if pagina == 'Autores':
    st.markdown(f"<h2 style = 'text-align: center;'>Os desenvolvedores do Site são:</h2>", unsafe_allow_html=True)
    st.write('')
    st.markdown(' #### ✔️ Isaque David Pereira de Almeida')
    st.markdown("📜 [Currículo Lattes](http://lattes.cnpq.br/4334402971349874)")
    st.markdown("🖥️ [Researshgate](https://www.researchgate.net/profile/Isaque-Almeida)")
    st.markdown("💻 [Linkedin](https://www.linkedin.com/in/isaque-d-4954ba1b1/)")
    st.write('')

    st.markdown(' #### ✔️ Lucas Ramon dos Santos Hermogenes')
    st.markdown("📜 [Currículo Lattes](http://lattes.cnpq.br/9679408116975910)")
    st.markdown("🖥️ [Researchgate](https://www.researchgate.net/profile/Lucas-Ramon-Dos-Santos-Hermogenes)")
    st.markdown("💻 [Linkedin](https://www.linkedin.com/in/lramon/)")
    st.write('')    

    st.markdown(' #### ✔️ Prof. DSc. Marcos dos Santos')
    st.markdown("📜 [Currículo Lattes](http://lattes.cnpq.br/5534398558592175)")
    st.markdown("🖥️ [Researshgate](https://www.researchgate.net/profile/Marcos-Santos-85)")
    st.markdown("💻 [Linkedin](https://www.linkedin.com/in/profmarcosdossantos/)")
    #imagem = st.image('https://www.youtube.com/s/desktop/70ea5db2/img/favicon_32x32.png') 
    st.markdown(" **Casa da Pesquisa Operacional** - [YouTube](https://www.youtube.com/c/CasadaPesquisaOperacional)")

    st.markdown(' #### ✔️ Prof. DSc. Carlos Francisco Simões Gomes')
    st.markdown("📜 [Currículo Lattes](http://lattes.cnpq.br/7509084995553647)")
    st.markdown("🖥️ [Researshgate](https://www.researchgate.net/profile/Carlos-Francisco-Gomes)")
    st.markdown("💻 [Linkedin](https://www.linkedin.com/in/carlos-francisco-sim%C3%B5es-gomes-7284a3b/)")


st.write('')
st.image('imagem rodape.jpeg', caption='Para Citar: Almeida, Isaque David Pereira; Hermogenes, Lucas Ramon dos Santos; Gomes, Carlos Francisco Simões.; Santos, Marcos dos. \nCRITIC-GRA-3N (CG-3N) For Decision Making (v1), Universidade Federal Fluminense, Niterói, Rio de Janeiro, 2022.')

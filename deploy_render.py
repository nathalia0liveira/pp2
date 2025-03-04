# -*- coding: utf-8 -*-
"""deploy.render

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15_ahKKb0Lmfk1qsHV3LxWuZcqKh2hAJ4
"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import pickle
# import numpy as np
# from sklearn.linear_model import LinearRegression
# from sklearn.datasets import load_boston
# 
# # Carregar o dataset (substitua pelo seu dataset)
# data = load_boston()
# X = data.data
# y = data.target
# 
# # Treinar o modelo
# model = LinearRegression()
# model.fit(X, y)
# 
# # Função para fazer previsões
# def predict(inputs):
#     prediction = model.predict([inputs])
#     return prediction
# 
# # Interface Streamlit
# st.title('Previsão de Desempenho Acadêmico')
# st.write('Insira as características do aluno para prever seu desempenho')
# 
# input_values = []
# for i in range(X.shape[1]):
#     input_values.append(st.slider(f"Valor da característica {i+1}", min_value=float(X[:, i].min()), max_value=float(X[:, i].max()), value=float(X[:, i].mean())))
# 
# if st.button('Fazer Previsão'):
#     result = predict(input_values)
#     st.write(f'Previsão de Desempenho: {result[0]:.2f}')
#
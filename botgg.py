# -*- coding: utf-8 -*-
"""Bot

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OhQ15Dj3WwISrv6u_CecbmTe127uwwUd
"""

import streamlit as st
from transformers import pipeline, set_seed

def load_generate():
    gen = pipeline('text-generation', model='openai-gpt')
    set_seed(42)
    return gen

generator = load_generate()

st.title('Бот для дополнения текста')
text = st.text_area("Место для записи начала текста", height=100, max_chars=50)

num_sequences = st.slider(
    "Количество предложений:",
    min_value=1,
    max_value=10
)

len_sequences = st.slider(
    "Длина предложений:",
    min_value=10,
    max_value=100
)

button_add = st.button('Дополнить текст')

if button_add:
    st.write('**Варианты продолжения текста :**')
    if(len(text) > 0): 
        result = generator(text, max_length=len_sequences, num_return_sequences=num_sequences)
        for elem in result:
            st.write(elem['generated_text'])
    else:
        st.write("Вы не ввели текст")


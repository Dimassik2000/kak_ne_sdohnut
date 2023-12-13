import streamlit as st
from transformers import pipeline, set_seed

def load_generate():
    gen = pipeline('text-generation', model='openai-gpt')
    set_seed(42)
    return gen

generator = load_generate()

st.title('Бот для дополнения теста')
text = st.text_area("Место для записи начала текста", height=100)

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
    result = generator(text, max_length=len_sequences, num_return_sequences=num_sequences)
    for elem in result:
        st.write(elem['generated_text'])


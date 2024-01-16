import streamlit as st
from botgg import load_generate

def test_root():
  app = st.empty()
  assert app.title == "Бот для дополнения текста"

def test_generate_text():
  app = st.empty()
  text = "Это тест"
  num_sequences = 2
  len_sequences = 10
  result = load_generate(text, len_sequences, num_sequences)
  assert len(result) == num_sequences
  for elem in result:
    assert isinstance(elem, dict)
    assert "generated_text" in elem
    assert isinstance(elem["generated_text"], str)
    assert len(elem["generated_text"]) <= len_sequences

def test_generate_text_length():
  app = st.empty()
  text = "Это тест"
  num_sequences = 2
  len_sequences = 10
  result = load_generate(text, len_sequences, num_sequences)
  for elem in result:
    assert len(elem["generated_text"]) <= len_sequences

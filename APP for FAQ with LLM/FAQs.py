#1. Import libraries

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import streamlit as st
import pandas as pd
import numpy as np

# 2. Set a title

st.title('Generador de FAQs:')

# 3. Create variable

llm = OpenAI(
    temperature=0.1,
    model_name='gpt-3.5-turbo',
    openai_api_key = "Insert here an API-key",
    max_tokens=150
)

template =  """
Eres un experto formulador de preguntas frecuentes (FAQ), genera un listado de preguntas frecuentes para el siguiente tema específico: {topic}. Enuméralas en un top 10
"""

# 4. Create an input box
question = st.text_input("Escribe el tema:")

topic = question

# 5. Create an answer
answer = llm(template.format(topic=topic))

# 6. print in Streamlit
st.write(answer)

# to test run in console: streamlit run FAQs.py
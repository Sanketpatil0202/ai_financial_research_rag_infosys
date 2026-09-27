import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from src.rag import final_response

from src.rag import final_response


st.title("AI Financial Research Assistant")
st.write("Ask questions about Infosys annual reports.")

question = st.text_input(
    "Enter your financial question:"
)

if question:
    response = final_response(question)
    st.write(response)
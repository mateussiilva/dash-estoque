import streamlit as st
import pandas as pd

data = pd.DataFrame(pd.read_csv("data.csv"))

estoque,impressao, paineis = st.tabs(["Estoque","Impressao","Paineis"])

with estoque:
    st.header("Area de estoque de materias")
    st.table(data)
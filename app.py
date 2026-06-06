import streamlit as st
import pandas as pd

st.title("ロシア語単語帳")

df = pd.read_csv("3言語2.csv")

st.write(df)

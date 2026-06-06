import streamlit as st
import pandas as pd

df = pd.read_csv("3言語2.csv")

st.write(df.columns.tolist())

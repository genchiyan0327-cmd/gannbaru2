import streamlit as st
import pandas as pd

st.title("ロシア語単語帳")

df = pd.read_csv("3言語2.csv")

for _, row in df.iterrows():
    with st.expander(row["Русский"]):
        st.write(f"🇩🇪 {row['Deutsch']}")
        st.write(f"🇺🇸 {row['English']}")

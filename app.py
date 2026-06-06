import streamlit as st
import pandas as pd

st.title("ロシア語単語帳")

# CSV読み込み
df = pd.read_csv("3言語2.csv")

# 列名の余計なスペースを削除
df.columns = df.columns.str.strip()

# 検索
search = st.text_input("🔍 検索")

if search:
    df = df[
        df["Русский"].astype(str).str.contains(search, case=False, na=False)
        | df["Deutsch"].astype(str).str.contains(search, case=False, na=False)
        | df["English"].astype(str).str.contains(search, case=False, na=False)
    ]

# 単語一覧
for _, row in df.iterrows():
    with st.expander(row["Русский"]):
        st.write(f"🇩🇪 {row['Deutsch']}")
        st.write(f"🇺🇸 {row['English']}")

import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO

st.title("ロシア語単語帳")

# CSV読み込み
df = pd.read_csv("3言語2.csv")

# 列名の余計なスペースを削除
df.columns = df.columns.str.strip()

# 音声作成
def make_audio(text):
    tts = gTTS(text=str(text), lang="ru")
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp

# 検索
search = st.text_input("🔍 検索")

if search:
    df = df[
        df["Русский"].astype(str).str.contains(search, case=False, na=False)
        | df["Deutsch"].astype(str).str.contains(search, case=False, na=False)
        | df["English"].astype(str).str.contains(search, case=False, na=False)
    ]

# ページ設定
page_size = 50
total_pages = max(1, (len(df) - 1) // page_size + 1)

if "page" not in st.session_state:
    st.session_state.page = 1

if search:
    st.session_state.page = 1

page = max(1, min(st.session_state.page, total_pages))
st.session_state.page = page

start = (page - 1) * page_size
end = start + page_size

# 単語表示
for _, row in df.iloc[start:end].iterrows():

    with st.expander(f"{row['Русский']} 🔊"):

        st.audio(make_audio(row["Русский"]))

        st.write(f"🇩🇪 {row['Deutsch']}")
        st.write(f"🇺🇸 {row['English']}")

st.divider()

# ページ送り
col_prev, col_nums, col_next = st.columns([1, 5, 1])

with col_prev:
    if page > 1:
        if st.button("◀"):
            st.session_state.page -= 1
            st.rerun()

with col_nums:
    start_num = max(1, page - 2)
    end_num = min(total_pages, page + 2)

    cols = st.columns(end_num - start_num + 1)

    for i, p in enumerate(range(start_num, end_num + 1)):
        label = f"[{p}]" if p == page else str(p)

        with cols[i]:
            if st.button(label, key=f"page_{p}"):
                st.session_state.page = p
                st.rerun()

with col_next:
    if page < total_pages:
        if st.button("▶"):
            st.session_state.page += 1
            st.rerun()

st.caption(f"ページ {page} / {total_pages}")

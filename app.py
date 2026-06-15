import streamlit as st
from groq import Groq
import pdfplumber

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def load_pdf(path: str) -> str:
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def chat(messages: list) -> str:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
    )
    return response.choices[0].message.content

SYSTEM_PROMPT = """あなたは会社の規定に関する質問に答えるAIアシスタントです。
提供された規定の内容のみを根拠に、丁寧に回答してください。
規定に該当する情報がない場合は「規定に記載がないため、担当者にお問い合わせください」と答えてください。
日本語で回答してください。"""

pdf_text = load_pdf("company_rules.pdf")

st.title("🤖 AI-FAQ")
st.caption("社内規定サポート窓口")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("例：有給休暇は何日もらえますか？"):
    user_content = f"質問：{prompt}\n\n【社内規定全文】\n{pdf_text}\n\n上記の規定を参考に回答してください。"

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("考え中..."):
            full_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + \
                [{"role": "user", "content": user_content}]
            response = chat(full_messages)
        st.write(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
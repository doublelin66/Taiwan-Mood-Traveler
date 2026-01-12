import streamlit as st
import google.generativeai as genai

st.title("2026 台灣情緒旅人 🇹🇼")

# API 設定
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# 這裡就是你要搬運的地方
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="你是一個情緒旅遊專家..." # <--- 從 AI Studio 複製貼到這
)

prompt = st.chat_input("今天心情如何？")
if prompt:
    st.write(f"你說：{prompt}")
    response = model.generate_content(prompt)
    st.write(f"AI 回覆：{response.text}")

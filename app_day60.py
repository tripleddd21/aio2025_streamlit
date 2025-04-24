import openai.cli
import streamlit as st
import openai
import os
import google.generativeai as genai



st.set_page_config(layout="wide")
st.title("💬 Day 60: Tạo dứng dụng GPT cơ bản với Streamlit")

st.subheader("Mô hình hoạt động của ứng dụng ChatGPT và Streamlit")
st.text("- Giao diện người dùng được xây dựng bằng Streamlit.")
st.text("- Người dùng nhập tin nhắn vào hộp thoại.")
st.text("- Tin nhắn được gửi đến API của OpenAI.")
st.text("- Phản hồi từ API được hiển thị trên giao diện như một tin nhắn trả lời từ ChatGPT.")
st.text("- Cuộc hội thoại được lưu trong session (Bộ nhớ tạm)")



# Đặt API key
genai.configure(api_key=st.secrets["gemini_api_key"])

# Tạo model Gemini Pro
model = genai.GenerativeModel('gemini-1.5-flash')

# Streamlit giao diện
st.title("💬 Gemini Chat Bot (Miễn phí)")

# Lưu trạng thái hội thoại
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Hiển thị lịch sử chat
for msg in st.session_state.chat.history:
    role = "user" if msg.role == "user" else "🤖 Trợ lý AI"
    st.chat_message(role).markdown(msg.parts[0].text)

# Nhận input từ người dùng
if prompt := st.chat_input("Nhập câu hỏi của bạn..."):
    # Hiển thị và lưu tin nhắn người dùng
    st.chat_message("user").markdown(prompt)
    response = st.session_state.chat.send_message(prompt)

    # Hiển thị trả lời từ Gemini
    st.chat_message("🤖 Trợ lý AI").markdown(response.text)
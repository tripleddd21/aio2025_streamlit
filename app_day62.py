try:
    import tempfile
    import librosa
    import numpy as np
    import matplotlib.pyplot as plt
    import urllib.request
    import streamlit as st
    import speech_recognition
    from gtts import gTTS
    import IPython.display as ipd
    import os
except ModuleNotFoundError as e:
    print("🚫 Lỗi: Bạn chưa cài đặt đủ các thư viện cần thiết.")
    print("👉 Hãy chạy: pip install streamlit SpeechRecognition")
    raise e

st.set_page_config(page_title="Xử lý âm thanh", layout="centered")

st.title("Day 62: Thư viện xử lý âm thanh")

st.subheader("1. Thư viện librosa")
st.write("Thư viện librosa là một thư viện Python dùng để phân tích âm thanh và nhạc. Nó cung cấp nhiều công cụ hữu ích cho việc xử lý âm thanh, bao gồm trích xuất đặc trưng, phân tích tần số, và nhiều hơn nữa.")

# Upload file
uploaded_file = st.file_uploader("Tải lên file âm thanh (.mp3 hoặc .wav)", type=["mp4", "wav"])

if uploaded_file is not None:
    try:
        # Ghi file tạm ra ổ cứng
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name

        # Dùng librosa để load từ file tạm
        audio, sr = librosa.load(tmp_path, sr=None)

        # Tạo trục thời gian
        time = np.linspace(0, len(audio) / sr, num=len(audio))

        # Vẽ waveform
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(time, audio, color='blue')
        ax.set_title("Waveform")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude")
        ax.axhline(y=0, color='gray', linestyle='--')
        st.pyplot(fig)

        st.success(f"Tần số lấy mẫu: {sr} Hz | Tổng mẫu: {len(audio)}")

    except Exception as e:
        st.error(f"Lỗi khi đọc file âm thanh: {e}")

st.subheader("2. Thư viện Speech Recognition")

st.subheader("3. Thư viện gtts")

st.header("Bài tập")
# --- Test case 1: Load file âm thanh và hiển thị đồ thị + văn bản ---
file_audio = 'hehe.wav'  # hoặc .mp3 nếu ffmpeg có
data, sr = librosa.load(file_audio, sr=None)
time = np.linspace(0, len(audio) / sr, num=len(audio))
st.write("✅ Đã load file âm thanh:", file_audio)

# Hiển thị waveform
fig2, ax = plt.subplots(figsize=(10, 4))
ax.plot(time, audio, color='blue')
ax.set_title("Waveform")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Amplitude")
ax.axhline(y=0, color='gray', linestyle='--')
st.pyplot(fig2)

# Nhận diện bằng speech_recognition

sr = speech_recognition 
st.title("🗣️ Nhận diện giọng nói từ file WAV")

uploaded_file = st.file_uploader("Tải lên file âm thanh (.wav)", type=["wav"])

if uploaded_file is not None:
    try:
        # Lưu file WAV tạm
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_wav:
            tmp_wav.write(uploaded_file.read())
            wav_path = tmp_wav.name

        # Nhận dạng giọng nói
        recognizer = sr.Recognizer()
        st.info("🎧 Đang nhận dạng giọng nói...")
        with sr.AudioFile(wav_path) as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio, language="vi-VN")

        # Hiển thị kết quả
        st.success("✅ Nhận diện thành công!")
        st.text_area("📜 Kết quả nhận dạng:", text, height=300)

        # Nút phát lại âm thanh
        st.audio(wav_path)

        # Nút tải về file văn bản
        st.download_button(
            label="💾 Tải văn bản dưới dạng .txt",
            data=text,
            file_name="ket_qua_nhan_dang.txt",
            mime="text/plain"
        )

        # Xóa file tạm
        os.remove(wav_path)

    except Exception as e:
        st.error(f"❌ Lỗi: {e}")


# --- Test case 2: chuyển text thành giọng nói ---
st.markdown("---")
st.subheader("🔄 Chuyển văn bản thành giọng nói")

text_input = st.text_area("Nhập nội dung văn bản để chuyển sang giọng nói:", "Tôi yêu AIO")
if st.button("🎤 Tạo giọng nói từ văn bản"):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_mp3:
            tts = gTTS(text_input, lang='vi')
            tts.save(tmp_mp3.name)
            audio_path = tmp_mp3.name
        st.audio(audio_path)
        with open(audio_path, "rb") as f:
            st.download_button("💾 Tải file âm thanh .mp3", f, file_name="text_to_speech.mp3", mime="audio/mpeg")
        os.remove(audio_path)
    except Exception as e:
        st.error(f"❌ Lỗi khi chuyển văn bản thành giọng nói: {e}")
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Tiêu đề")
st.write("Đây là ứng dụng Streamlit đơn giản")


# Tạo biểu đồ đơn giản:
st.subheader("Biểu đồ đơn giản")

df = sns.load_dataset("tips")
fig, ax = plt.subplots()
sns.scatterplot(data=df, x="total_bill", y="tip", ax=ax)
st.pyplot(fig)
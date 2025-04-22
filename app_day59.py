import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import pygwalker as pyg
import streamlit.components.v1 as components

st.set_page_config(layout="wide") 
st.title("Day 59: Srteamlit & PyGWalker")

st.header("1. Tải file CSV và hiển thị dữ liệu")

uploaded_file = st.file_uploader("Tải lên file CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Dữ liệu từ file CSV:")
    st.dataframe(df.head())  # Hiển thị 5 dòng đầu tiên của DataFrame
    st.write("Row count: ", df.shape[0])
    st.write("Column count: ", df.shape[1])

st.header("2. Thống kê mô tả dữ liệu")

if uploaded_file is not None:
    st.subheader("Thống kê mô tả")
    st.write("Các thống kê cơ bản:")
    st.dataframe(df.describe())  # Hiển thị thống kê mô tả
    st.write("Các thông tin khác:")
    st.write("Kiểu dữ liệu:")
    st.dataframe(df.dtypes)
    st.write("Giá trị null:")
    st.dataframe(df.isnull().sum())

st.header("3. Phân tích  EDA bằng PyGWWalker")
if uploaded_file is not None:
    st.subheader("Phân tích dữ liệu tương tác với PyGWalker")
    pyg_html = pyg.walk(df, return_html=True)
    components.html(pyg_html, height=1000, scrolling=True)
 
 
if uploaded_file is not None:
    # 💡 Mở rộng 1: Chọn cột
    selected_cols = st.multiselect("Chọn cột để phân tích:", df.columns.tolist())
    if selected_cols:
        df = df[selected_cols]

    # 💡 Mở rộng 2: Biểu đồ tương quan
    numeric_cols = df.select_dtypes(include='number')
    if not numeric_cols.empty:
        corr = numeric_cols.corr()
        fig, ax = plt.subplots()
        sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
        st.subheader("🔍 Ma trận tương quan")
        st.pyplot(fig)


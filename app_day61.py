import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="Day 61: Minh họa huấn luyện Linear Regresssion với Numpy và Streamlit")

st.title("Day 61: Minh họa huấn luyện Linear Regresssion với Numpy và Streamlit")

uploaded_file = st.file_uploader("Tải lên file CSV advertising", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Dữ liệu từ file CSV:")
    st.dataframe(df.head())  # Hiển thị 5 dòng đầu tiên của DataFrame
    st.write("Row count: ", df.shape[0])
    st.write("Column count: ", df.shape[1])
    X = df[["TV", "Radio", "Newspaper"]].values
    Y = df["Sales"].values.reshape(-1, 1)
    # chuẩn hóa dữ liệu đầu vào
    X = (X - np.mean(X, axis = 0))/X.std(axis = 0)
    Y = (Y - np.mean(Y))/Y.std(axis=0)

    # huấn luyện Linear Regression bằng phương pháp vector hóa
    def train_linear_regression(X, Y, learning_rate=0.01, epochs=100):
        m, n = X.shape
        w = np.zeros((n, 1))
        b = 1.0
        loss_history = []
        for i in range(epochs):
            y_pred = X.dot(w) + b

            loss = y_pred - Y

            mse = np.mean(loss**2)
            loss_history.append(mse)
            d_w = (1/m) * X.T.dot(loss)
            d_b = (1/m) * np.sum(loss)

            w -= learning_rate * d_w
            b -= learning_rate * d_b
        return w, b, loss_history
    
    st.title("Huấn luyện Linear Regression")
    lr = st.slider("Chọn learning rate", 0.01, 0.1, 0.01)
    epochs = st.slider("Chọn số lượng epochs", 100, 1000, 200)
    
    if st.button("Train Model"):
        w, b , loss_history = train_linear_regression(X, Y, learning_rate=lr, epochs=epochs)

        st.subheader("Loss theo epoch: ")
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.plot(loss_history, label="Loss")
        ax.set_xlabel("Epoch")
        ax.set_ylabel("MSE Loss")
        st.pyplot(fig)

        st.write("Trọng số w: ", w.flatten())
        st.write("Bias b: ", b)
        
        st.success(f"✅ MSE cuối cùng: {loss_history[-1]:.4f}")


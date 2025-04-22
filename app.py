import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title("Tiêu đề")
st.write("Đây là ứng dụng Streamlit đơn giản")


# Tạo biểu đồ đơn giản:
st.subheader("Biểu đồ đơn giản")

df = sns.load_dataset("tips")
fig, ax = plt.subplots()
sns.scatterplot(data=df, x="total_bill", y="tip", ax=ax)
st.pyplot(fig)

st.title("# Day 58: Srteamlit")

st.write("### 1. Vẽ đồ thị hàm số cơ bản")

x = np.linspace(-10,10,1000)
y = np.sin(x)

fig, ax =plt.subplots()
ax.plot(x, y, label="y = sin(x)", color='blue')
ax.set_title("Đồ thị hàm sin(x) trong khoảng [-10, 10]")
ax.grid(True)

st.pyplot(fig) # hiện thị biểu đồ

st.write("### 2. So sánh 2 hàm số trên cùng một biểu đồ")

x= np.linspace(-5,5,1000)
y1 = np.sin(x)
y2= np.cos(x)

fig, ax = plt.subplots()

ax.plot(x, y1, label="y = sin(x)", color='blue')
ax.plot(x, y2, label="y = cos(x)", color='red')
ax.set_title("Đồ thị hàm sin(x) và cos(x) trong khoảng [-5, 5]")
ax.legend()
ax.grid(True)
st.pyplot(fig) # hiện thị biểu đồ


st.write("### 3. Vẽ đồ thị hàm số bậc 2 y = ax^2 + bx + c")

st.write("Nhập các hệ số a, b, c")


a = float(st.text_input("Nhập hệ số a", value=0.0))
b = float(st.text_input("Nhập hệ số b", value=0.0))
c = float(st.text_input("Nhập hệ số c", value=0.0))

x = np.linspace(-10, 10, 1000)
y = a* x**2 + b*x + c

fig,ax = plt.subplots()
ax.plot(x, y, label="y = ax^2 +bx+c", color = 'red')
ax.set_title("Đồ thị hàm bậc 2 ax^2 + bx + c")
ax.grid(True)

st.pyplot(fig) # hiện thị biểu đồ


st.write("### 4. Tương tác với slider để khảo sát đồ thị")

a = st.slider("Chọn giá trị a", min_value=0.0, max_value=10.0, value=1.0, step=1.0)
b = st.slider("Chọn giá trị b", min_value=0.0, max_value=10.0, value=1.0, step=1.0)
c = st.slider("Chọn giá trị c", min_value=0.0, max_value=10.0, value=1.0, step=1.0)

x = np.linspace(-10, 10, 1000)
y = a* x**2 + b*x + c

fig,ax = plt.subplots()
ax.plot(x, y, label="y = ax^2 +bx+c", color = 'red')
ax.set_title("Đồ thị hàm bậc 2 ax^2 + bx + c")
ax.grid(True)

st.pyplot(fig) # hiện thị biểu đồ


st.write("### 5. Vẽ Heartmap cho biểu đồ z = x^2 + y^2")

x = np.linspace(1, 10, 20)
y = np.linspace(1, 10, 10)
X, Y = np.meshgrid(x, y)
Z= X**2 + Y**2

fig, ax = plt.subplots()
sns.heatmap(Z, cmap='coolwarm', ax=ax, cbar=True)
ax.set_title("Biểu đồ nhiệt cho z = x^2 + y^2")

st.pyplot(fig) # hiện thị biểu đồ
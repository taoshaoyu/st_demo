import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

col1, col2, col3 = st.columns(3)
with col1:
    st.header("Column 1")
    st.write("这是第一列的内容")
with col2:
    st.header("Column 2")
    st.write("这是第二列的内容")
with col3:
    st.header("Column 3")
    st.write("这是第三列的内容")

if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button("增加")
if increment:
    st.session_state.count += 1

st.write(f"计数器值：{st.session_state.count}")

# 使用展开器创建隐藏内容
with st.expander("点击展开更多信息"):
    st.write("这里是一些可以展开的详细信息。")

# 假设我们有一些数据
data = pd.DataFrame({
    'first_column': list(range(1, 101)),
    'second_column': np.random.randn(100)
})

# 用户选择显示的数据数量
number = st.slider("请选择显示数据的数量", 1, 100, 50)

# 显示数据
st.write(data.head(number))

fig, ax = plt.subplots()
ax.hist(data['second_column'], bins=20)

st.pyplot(fig)

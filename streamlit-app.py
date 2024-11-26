import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="My Dashboard", layout="wide")


st.sidebar.title("User Preferences")
theme = st.sidebar.selectbox("Choose a Theme", ["Light", "Dark"])
show_chart = st.sidebar.checkbox("Show Chart", value=True)


st.title("My Personal Dashboard")
st.markdown("Welcome to your personal web app! Let's explore its features.")


name = st.text_input("Enter your name", "Guest")
st.write(f"Hello, {name}!")


if show_chart:
    # Generate and display a chart
    data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["Category A", "Category B", "Category C"]
    )
    st.line_chart(data)
else:
    st.write("🔒 Chart hidden. Enable it from the sidebar.")


col1, col2, col3 = st.columns(3)
col1.metric("Revenue", "$10K", "+5%")
col2.metric("Users", "1.2K", "+10%")
col3.metric("Performance", "98%", "+2%")


with st.expander("About this app"):
    st.write("This app demonstrates the power of Streamlit's widgets.")
    st.write("Feel free to experiment with the inputs!")

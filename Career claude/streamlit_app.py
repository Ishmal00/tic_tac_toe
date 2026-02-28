import streamlit as st
import streamlit.components.v1 as components

st.title("My Career Counselor App")

# Apni HTML file ko read karke yahan display karein
with open("Career claude/career-counselor.html", "r") as f:
    html_code = f.read()
    components.html(html_code, height=800, scrolling=True)

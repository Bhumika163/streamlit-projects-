import streamlit as st
import streamlit.components.v1 as components

with open("index.html", "r", encoding = "utf-8") as html_file:
    html_content = html_file.read()

components.html(html_content, height=500)
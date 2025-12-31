import streamlit as st

# Page configuration
st.set_page_config(page_title="Simple Webpage", page_icon="✨", layout="centered")

# Title and subtitle
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Welcome to My Webpage</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #FF5733;'>A Clean and Simple Page</h3>", unsafe_allow_html=True)

# Input and button
name = st.text_input("Enter your name:")
if st.button("Greet Me"):
    if name:
        st.success(f"Hello {name}! Welcome to the page 🎉")
    else:
        st.warning("Please enter your name!")

# Colored info boxes
st.info("💡 Tip: Streamlit makes web apps super easy!")
st.warning("⚠️ Note: This is a demo page.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Created with Streamlit ❤️</p>", unsafe_allow_html=True)





    
# calculator_board.py
# Calculator board layout using Streamlit

import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="🧮", layout="centered")

# Session state
if "expr" not in st.session_state:
    st.session_state.expr = "0"

# ---------- CSS styling ----------
st.markdown("""
<style>
.calc-box {
    width: 320px;
    margin: auto;
    padding: 15px;
    border-radius: 15px;
    background: #f2f2f2;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
}
.display {
    background: white;
    padding: 15px;
    font-size: 28px;
    text-align: right;
    border-radius: 8px;
    margin-bottom: 10px;
}
button {
    height: 55px;
    font-size: 18px !important;
}
.op button {
    background-color: #ffcc00 !important;
}
.gray button {
    background-color: #e0e0e0 !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("## Calculator")

# ---------- Functions ----------
def press(val):
    if st.session_state.expr == "0":
        st.session_state.expr = str(val)
    else:
        st.session_state.expr += str(val)

def clear():
    st.session_state.expr = "0"

def calculate():
    try:
        st.session_state.expr = str(eval(st.session_state.expr))
    except:
        st.session_state.expr = "Error"

# ---------- Calculator UI ----------
st.markdown("<div class='calc-box'>", unsafe_allow_html=True)

# Display
st.markdown(f"<div class='display'>{st.session_state.expr}</div>", unsafe_allow_html=True)

# Row 1
c1, c2, c3, c4 = st.columns(4)
with c1: st.button("AC", on_click=clear)
with c2: st.button("√x", on_click=lambda: press("**0.5"))
with c3: st.button("%", on_click=lambda: press("/100"))
with c4:
    st.markdown("<div class='op'>", unsafe_allow_html=True)
    st.button("÷", on_click=lambda: press("/"))
    st.markdown("</div>", unsafe_allow_html=True)

# Row 2
c1, c2, c3, c4 = st.columns(4)
with c1: st.button("7", on_click=lambda: press(7))
with c2: st.button("8", on_click=lambda: press(8))
with c3: st.button("9", on_click=lambda: press(9))
with c4:
    st.markdown("<div class='op'>", unsafe_allow_html=True)
    st.button("×", on_click=lambda: press("*"))
    st.markdown("</div>", unsafe_allow_html=True)

# Row 3
c1, c2, c3, c4 = st.columns(4)
with c1: st.button("4", on_click=lambda: press(4))
with c2: st.button("5", on_click=lambda: press(5))
with c3: st.button("6", on_click=lambda: press(6))
with c4:
    st.markdown("<div class='op'>", unsafe_allow_html=True)
    st.button("−", on_click=lambda: press("-"))
    st.markdown("</div>", unsafe_allow_html=True)

# Row 4
c1, c2, c3, c4 = st.columns(4)
with c1: st.button("1", on_click=lambda: press(1))
with c2: st.button("2", on_click=lambda: press(2))
with c3: st.button("3", on_click=lambda: press(3))
with c4:
    st.markdown("<div class='op'>", unsafe_allow_html=True)
    st.button("+", on_click=lambda: press("+"))
    st.markdown("</div>", unsafe_allow_html=True)

# Row 5
c1, c2, c3, c4 = st.columns(4)
with c1: st.button("0", on_click=lambda: press(0))
with c2: st.button(".", on_click=lambda: press("."))
with c3: st.button("xʸ", on_click=lambda: press("**"))
with c4:
    st.markdown("<div class='op'>", unsafe_allow_html=True)
    st.button("=", on_click=calculate)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

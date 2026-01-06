import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Information Portal")

# initialize session state for storing data
if "students" not in st.session_state:
    st.session_state.students = []

# sidebar navigation
menu = st.sidebar.radio(
    "Navigation",
    ["Home", "Student Information", "Student Records"]
)

# HOME PAGE
if menu == "Home":
    st.title("Student Information Portal")
    st.write(
        "This application allows students to enter their information "
        "and view it in a table format."
    )

# STUDENT INFORMATION PAGE
elif menu == "Student Information":
    st.title("Student Information")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=100)
    course = st.text_input("Course")

    if st.button("Submit"):
        if name and course:
            st.session_state.students.append({
                "Name": name,
                "Age": age,
                "Course": course
            })
            st.success("Student information added successfully")
        else:
            st.error("Please fill all fields")

# STUDENT RECORDS PAGE
elif menu == "Student Records":
    st.title("Student Records")

    if st.session_state.students:
        df = pd.DataFrame(st.session_state.students)
        st.table(df)
    else:
        st.info("No student records available")

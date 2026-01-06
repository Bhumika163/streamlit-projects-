import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Student Marks Analysis", layout="centered")

st.title("📊 Student Marks Analysis App")

# File upload
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file)

    # Clean column names (important)
    df.columns = df.columns.str.strip().str.lower()

    st.subheader("📋 Student Database")
    st.dataframe(df)

    # Validate required columns
    if {"name", "subject", "marks"}.issubset(df.columns):

        # Convert marks to numeric
        df["marks"] = pd.to_numeric(df["marks"], errors="coerce")

        # Filter by subject
        st.subheader("🔍 Filter by Subject")
        subjects = df["subject"].unique()
        selected_subject = st.selectbox("Select subject", subjects)

        filtered_df = df[df["subject"] == selected_subject]

        st.subheader(f"📄 Data for {selected_subject}")
        st.dataframe(filtered_df)

        # Subject-wise insights
        avg_marks = filtered_df["marks"].mean()
        max_marks = filtered_df["marks"].max()
        min_marks = filtered_df["marks"].min()

        st.subheader("📈 Subject-wise Insights")
        col1, col2, col3 = st.columns(3)
        col1.metric("Average Marks", round(avg_marks, 2))
        col2.metric("Highest Marks", max_marks)
        col3.metric("Lowest Marks", min_marks)

        # Bar chart
        st.subheader("📊 Student Marks Bar Chart")

        fig, ax = plt.subplots()
        ax.bar(filtered_df["name"], filtered_df["marks"])
        ax.set_xlabel("Student Name")
        ax.set_ylabel("Marks")
        ax.set_title(f"Marks in {selected_subject}")

        st.pyplot(fig)

    else:
        st.error("CSV must contain columns: name, subject, marks")

else:
    st.info("Please upload a CSV file to start analysis.")

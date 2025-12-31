import streamlit as st
import pandas as p
import PyPDF2
from PIL import Image

st.title("Day 5: File processing Demo App")

#upload any file
uploaded_file = st.file_uploader("Upload a file( PDF / TXT / CSV / IMAGE )" , 
                                    type=['pdf', 'txt', 'csv', 'png', 'jpg', 'jpeg'])

if uploaded_file is not None:

    #Display file details
    st.write("File Name: ", uploaded_file.name)
    st.write("File Type: ", uploaded_file.type)
    st.write("File Size: ", uploaded_file.size, "bytes")

#-------TEXT File --------
    if uploaded_file.type == "text/plain":
        st.subheader("TXT File Content:")
        text = uploaded_file.read().decode("utf-8")
        st.text(text)

#-------CSV File ---------
    elif uploaded_file.type == "text/csv":
            st.subheader("CSV File Content:")
            df = pd.read_csv(uploaded_file)
            st.dataframe(df)

#-------PDF File --------
    elif uploaded_file.type == "application/pdf":
            st.subheader("PDF File Content:")
            try:
                pdf_reader = PyPDF2.PdfFileReader(uploaded_file)
                st.write("Total pages:", len(pdf_reader.pages))
                text = reader.pages[0].extract_text()
                st.text(text)
            except:
                st.error("Unable to  reading PDF file.")
            
#-------IMAGE File --------
    elif uploaded_file.type.startswith("image"):
            st.subheader("Image Preview")
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image")

    else:
        st.warning("Unsupported file type!")        


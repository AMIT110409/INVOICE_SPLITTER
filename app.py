import streamlit as st
import os
import shutil
from split_pdf import split_pdf

# Streamlit app configuration
st.set_page_config(page_title="Invoice Splitter", page_icon="📄")

st.title("Invoice Splitter")
st.markdown("""
Upload a multi-invoice PDF file to split it into individual invoices based on blank pages.
Adjust the threshold to control blank page detection sensitivity.
""")

# File uploader
uploaded_file = st.file_uploader("Upload your PDF file", type=["pdf"])

# Threshold slider
threshold = st.slider("Blank Page Detection Threshold", min_value=0.90, max_value=1.00, value=0.99, step=0.01)

if uploaded_file is not None:
    # Save the uploaded file temporarily
    temp_pdf_path = "temp_uploaded.pdf"
    with open(temp_pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Button to split the PDF
    if st.button("Split PDF"):
        with st.spinner("Splitting PDF..."):
            try:
                # Clear previous output directory
                if os.path.exists("output_invoices"):
                    shutil.rmtree("output_invoices")
                
                # Split the PDF
                output_files, num_invoices = split_pdf(temp_pdf_path, threshold)
                
                # Display results
                st.success(f"Successfully split PDF into {num_invoices} invoices!")
                st.write("### Output Invoices")
                
                # Provide download links for each output PDF
                for output_file in output_files:
                    with open(output_file, "rb") as f:
                        st.download_button(
                            label=f"Download {os.path.basename(output_file)}",
                            data=f,
                            file_name=os.path.basename(output_file),
                            mime="application/pdf"
                        )
                
                # Display log file
                if os.path.exists("split_log.txt"):
                    with open("split_log.txt", "r") as f:
                        log_content = f.read()
                    st.write("### Split Log")
                    st.text_area("Log", log_content, height=200)
                
            except Exception as e:
                st.error(f"Error splitting PDF: {str(e)}")
            finally:
                # Clean up temporary file
                if os.path.exists(temp_pdf_path):
                    os.remove(temp_pdf_path)

else:
    st.info("Please upload a PDF file to proceed.")
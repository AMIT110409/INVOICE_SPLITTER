# import streamlit as st
# import os
# import shutil
# from split_pdf import split_pdf

# # Streamlit app configuration
# st.set_page_config(page_title="Invoice Splitter", page_icon="📄")

# st.title("Invoice Splitter")
# st.markdown("""
# Upload a multi-invoice PDF file to split it into individual invoices based on blank pages.
# Adjust the threshold to control blank page detection sensitivity.
# """)

# # File uploader
# uploaded_file = st.file_uploader("Upload your PDF file", type=["pdf"])

# # Threshold slider
# threshold = st.slider("Blank Page Detection Threshold", min_value=0.90, max_value=1.00, value=0.99, step=0.01)

# if uploaded_file is not None:
#     # Save the uploaded file temporarily
#     temp_pdf_path = "temp_uploaded.pdf"
#     with open(temp_pdf_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())
    
#     # Button to split the PDF
#     if st.button("Split PDF"):
#         with st.spinner("Splitting PDF..."):
#             try:
#                 # Clear previous output directory
#                 if os.path.exists("output_invoices"):
#                     shutil.rmtree("output_invoices")
                
#                 # Split the PDF
#                 output_files, num_invoices = split_pdf(temp_pdf_path, threshold)
                
#                 # Display results
#                 st.success(f"Successfully split PDF into {num_invoices} invoices!")
#                 st.write("### Output Invoices")
                
#                 # Provide download links for each output PDF
#                 for output_file in output_files:
#                     with open(output_file, "rb") as f:
#                         st.download_button(
#                             label=f"Download {os.path.basename(output_file)}",
#                             data=f,
#                             file_name=os.path.basename(output_file),
#                             mime="application/pdf"
#                         )
                
#                 # Display log file
#                 if os.path.exists("split_log.txt"):
#                     with open("split_log.txt", "r") as f:
#                         log_content = f.read()
#                     st.write("### Split Log")
#                     st.text_area("Log", log_content, height=200)
                
#             except Exception as e:
#                 st.error(f"Error splitting PDF: {str(e)}")
#             finally:
#                 # Clean up temporary file
#                 if os.path.exists(temp_pdf_path):
#                     os.remove(temp_pdf_path)

# else:
#     st.info("Please upload a PDF file to proceed.")

# import streamlit as st
# import os
# import shutil
# import fitz  # PyMuPDF for PDF handling
# from split_pdf import split_pdf
# import time
# import zipfile
# import io
# from PIL import Image
# import base64
# from datetime import datetime

# # Set page config as the FIRST Streamlit command
# st.set_page_config(page_title="Invoice Splitter", page_icon="📄", layout="wide")

# # Custom CSS for styling with animations
# st.markdown("""
#     <style>
#     .main {
#         font-family: 'Helvetica', sans-serif;
#         transition: background-color 0.3s;
#     }
#     .light-theme {
#         background-color: #f9f9f9;
#         color: #333;
#     }
#     .dark-theme {
#         background-color: #1e1e1e;
#         color: #e0e0e0;
#     }
#     .stButton>button {
#         background-color: #1f77b4;
#         color: white;
#         border-radius: 8px;
#         padding: 10px 20px;
#         font-weight: bold;
#         transition: background-color 0.3s;
#     }
#     .stButton>button:hover {
#         background-color: #155e91;
#     }
#     .stSlider .st-bx {
#         background-color: #e1f3ff;
#     }
#     .stFileUploader {
#         border: 2px dashed #1f77b4;
#         border-radius: 8px;
#         padding: 10px;
#     }
#     .header {
#         background-color: #1f77b4;
#         color: white;
#         padding: 15px;
#         border-radius: 8px;
#         text-align: center;
#         font-size: 24px;
#         font-weight: bold;
#         margin-bottom: 20px;
#     }
#     .footer {
#         text-align: center;
#         font-size: 12px;
#         margin-top: 20px;
#     }
#     .download-section {
#         background-color: #e1f3ff;
#         padding: 15px;
#         border-radius: 8px;
#         margin-top: 10px;
#         animation: fadeIn 0.5s;
#     }
#     @keyframes fadeIn {
#         0% { opacity: 0; }
#         100% { opacity: 1; }
#     }
#     .preview-image {
#         border: 1px solid #ddd;
#         border-radius: 8px;
#         max-width: 100%;
#         margin-top: 10px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Initialize session state for theme, history, and settings
# if "theme" not in st.session_state:
#     st.session_state.theme = "light"
# if "download_history" not in st.session_state:
#     st.session_state.download_history = []
# if "threshold" not in st.session_state:
#     st.session_state.threshold = 0.99

# # Theme toggle function
# def toggle_theme():
#     st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

# # Apply theme
# theme_class = "light-theme" if st.session_state.theme == "light" else "dark-theme"
# st.markdown(f'<div class="main {theme_class}">', unsafe_allow_html=True)

# # Sidebar
# with st.sidebar:
#     st.header("Invoice Splitter Settings")
#     st.button("Toggle Theme 🌙", on_click=toggle_theme, help="Switch between light and dark themes.")
#     st.session_state.threshold = st.slider(
#         "Blank Page Detection Threshold",
#         min_value=0.90,
#         max_value=1.00,
#         value=st.session_state.threshold,
#         step=0.01,
#         help="Set the threshold for detecting blank pages (higher values are stricter)."
#     )
#     # Help section
#     with st.expander("Help ℹ️", expanded=False):
#         st.markdown("""
#         **How to Use:**
#         1. Upload a multi-invoice PDF file.
#         2. Adjust the threshold in the sidebar.
#         3. Click "Split PDF" to process.
#         4. Download individual invoices or all as a ZIP.
#         5. View your download history below.

#         **Contact Support:** [amitrathore110409@gmail.com](mailto:amitrathore110409@gmail.com)
#         """)

# # Header
# st.markdown('<div class="header">📄 Invoice Splitter</div>', unsafe_allow_html=True)
# st.markdown("Split multi-invoice PDFs into individual invoices with ease! Upload your file below.")

# # Main layout with columns
# col1, col2 = st.columns([2, 1])

# with col1:
#     # File uploader and preview
#     st.subheader("Upload PDF")
#     uploaded_file = st.file_uploader(
#         "Choose a PDF file",
#         type=["pdf"],
#         help="Upload a multi-invoice PDF file to split."
#     )

#     # Display PDF info and preview if uploaded
#     if uploaded_file is not None:
#         with st.spinner("Analyzing PDF..."):
#             # Save temporarily
#             temp_pdf_path = "temp_uploaded.pdf"
#             with open(temp_pdf_path, "wb") as f:
#                 f.write(uploaded_file.getbuffer())
#             # Get page count
#             pdf_document = fitz.open(temp_pdf_path)
#             page_count = len(pdf_document)
#             # Render first page as image for preview
#             page = pdf_document.load_page(0)
#             pix = page.get_pixmap(matrix=fitz.Matrix(150/72, 150/72))  # 150 DPI
#             img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
#             pdf_document.close()
#             # Convert image to base64 for display
#             buffered = io.BytesIO()
#             img.save(buffered, format="PNG")
#             img_str = base64.b64encode(buffered.getvalue()).decode()
#         st.info(f"📄 **File Uploaded**: {uploaded_file.name} ({page_count} pages)")
#         st.markdown(f'<img src="data:image/png;base64,{img_str}" class="preview-image" alt="PDF Preview">', unsafe_allow_html=True)

# with col2:
#     # Controls
#     st.subheader("Actions")
#     split_button = st.button("Split PDF", help="Click to split the uploaded PDF.")
#     if st.button("Reset", help="Clear uploaded file and outputs."):
#         if os.path.exists("output_invoices"):
#             shutil.rmtree("output_invoices")
#         if os.path.exists("split_log.txt"):
#             os.remove("split_log.txt")
#         if os.path.exists("temp_uploaded.pdf"):
#             os.remove("temp_uploaded.pdf")
#         st.session_state.download_history = []
#         st.experimental_rerun()

# # Process PDF splitting
# if uploaded_file is not None and split_button:
#     # Confirmation dialog
#     if st.checkbox("Confirm splitting action", help="Check to proceed with splitting."):
#         temp_pdf_path = "temp_uploaded.pdf"
#         with open(temp_pdf_path, "wb") as f:
#             f.write(uploaded_file.getbuffer())
        
#         # Progress bar
#         progress = st.progress(0)
#         status_text = st.empty()
#         status_text.text("Starting PDF splitting...")
#         progress.progress(10)
        
#         try:
#             # Clear previous outputs
#             if os.path.exists("output_invoices"):
#                 shutil.rmtree("output_invoices")
            
#             # Simulate progress
#             progress.progress(30)
#             status_text.text("Converting PDF pages...")
#             time.sleep(0.5)
            
#             # Split the PDF
#             progress.progress(60)
#             status_text.text("Analyzing pages...")
#             output_files, num_invoices = split_pdf(temp_pdf_path, st.session_state.threshold)
            
#             progress.progress(90)
#             status_text.text("Saving output files...")
#             time.sleep(0.5)
            
#             # Display results
#             progress.progress(100)
#             status_text.text("Completed!")
#             st.success(f"✅ Successfully split PDF into **{num_invoices} invoices**!")
            
#             # Download section
#             with st.container():
#                 st.markdown('<div class="download-section">', unsafe_allow_html=True)
#                 st.subheader("Download Invoices")
#                 # Individual downloads
#                 for output_file in output_files:
#                     with open(output_file, "rb") as f:
#                         st.download_button(
#                             label=f"📥 Download {os.path.basename(output_file)}",
#                             data=f,
#                             file_name=os.path.basename(output_file),
#                             mime="application/pdf",
#                             help=f"Download {os.path.basename(output_file)}"
#                         )
#                 # ZIP download
#                 zip_buffer = io.BytesIO()
#                 with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
#                     for output_file in output_files:
#                         zip_file.write(output_file, os.path.join("invoices", os.path.basename(output_file)))
#                 zip_buffer.seek(0)
#                 st.download_button(
#                     label="📦 Download All as ZIP",
#                     data=zip_buffer,
#                     file_name=f"invoices_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip",
#                     mime="application/zip",
#                     help="Download all invoices as a ZIP file."
#                 )
#                 st.markdown('</div>', unsafe_allow_html=True)
            
#             # Update download history
#             history_entry = {
#                 "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#                 "filename": uploaded_file.name,
#                 "num_invoices": num_invoices
#             }
#             st.session_state.download_history.append(history_entry)
            
#             # Display log
#             if os.path.exists("split_log.txt"):
#                 with open("split_log.txt", "r") as f:
#                     log_content = f.read()
#                 with st.expander("View Split Log", expanded=False):
#                     st.text_area("Log", log_content, height=200)
        
#         except Exception as e:
#             st.error(f"❌ Error splitting PDF: {str(e)}")
#             progress.progress(0)
#             status_text.text("Failed!")
        
#         finally:
#             if os.path.exists(temp_pdf_path):
#                 os.remove(temp_pdf_path)

# # Download History
# with st.sidebar:
#     with st.expander("Download History 📜", expanded=False):
#         if st.session_state.download_history:
#             for entry in st.session_state.download_history:
#                 st.write(f"**{entry['timestamp']}**: {entry['filename']} ({entry['num_invoices']} invoices)")
#         else:
#             st.write("No downloads yet.")

# # Footer
# st.markdown(f'<div class="footer {theme_class}">Built for Hackathon | © 2025 Invoice Splitter by Amit</div>', unsafe_allow_html=True)
# st.markdown('</div>', unsafe_allow_html=True)  # Close main div


import streamlit as st
import os
import shutil
import fitz  # PyMuPDF for PDF handling
from split_pdf import split_pdf
import time
import zipfile
import io
from PIL import Image
import base64
from datetime import datetime

# Set page config as the FIRST Streamlit command
st.set_page_config(page_title="Invoice Splitter", page_icon="📄", layout="wide")

# Custom CSS with updated dark blue gradient background
st.markdown("""
    <style>
    .main {
        font-family: 'Helvetica', sans-serif;
        transition: background 0.3s;
    }
    .light-theme {
        background: linear-gradient(135deg, #0D1B2A, #1B263B);
        color: #F5F5F5; /* Off-white text for readability */
    }
    .dark-theme {
        background: linear-gradient(135deg, #0A1421, #151F30);
        color: #F5F5F5; /* Off-white text for readability */
    }
    .stButton>button {
        background-color: #FF6F61; /* Coral button for contrast */
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #FF8A65; /* Light coral on hover */
    }
    .stSlider .st-bx {
        background-color: #415A77; /* Muted blue for slider */
    }
    .stFileUploader {
        border: 2px dashed #FF6F61; /* Coral dashed border */
        border-radius: 8px;
        padding: 10px;
        background-color: rgba(255, 255, 255, 0.05); /* Slight white overlay for contrast */
    }
    .header {
        background-color: #FF6F61; /* Coral header */
        color: white;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .footer {
        text-align: center;
        font-size: 12px;
        margin-top: 20px;
        color: #BBBBBB; /* Lighter gray for footer text */
    }
    .download-section {
        background-color: #415A77; /* Muted blue for download section */
        padding: 15px;
        border-radius: 8px;
        margin-top: 10px;
        animation: fadeIn 0.5s;
    }
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    .preview-image {
        border: 1px solid #FF6F61; /* Coral border for preview */
        border-radius: 8px;
        max-width: 100%;
        margin-top: 10px;
    }
    /* Ensure Streamlit info boxes and success/error messages are readable */
    .stAlert {
        background-color: rgba(255, 255, 255, 0.1);
        color: #F5F5F5;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for theme, history, and settings
if "theme" not in st.session_state:
    st.session_state.theme = "light"
if "download_history" not in st.session_state:
    st.session_state.download_history = []
if "threshold" not in st.session_state:
    st.session_state.threshold = 0.99

# Theme toggle function
def toggle_theme():
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

# Apply theme
theme_class = "light-theme" if st.session_state.theme == "light" else "dark-theme"
st.markdown(f'<div class="main {theme_class}">', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("Invoice Splitter Settings")
    st.button("Toggle Theme 🌙", on_click=toggle_theme, help="Switch between light and dark themes.")
    st.session_state.threshold = st.slider(
        "Blank Page Detection Threshold",
        min_value=0.90,
        max_value=1.00,
        value=st.session_state.threshold,
        step=0.01,
        help="Set the threshold for detecting blank pages (higher values are stricter)."
    )
    # Help section
    with st.expander("Help ℹ️", expanded=False):
        st.markdown("""
        **How to Use:**
        1. Upload a multi-invoice PDF file.
        2. Adjust the threshold in the sidebar.
        3. Click "Split PDF" to process.
        4. Download individual invoices or all as a ZIP.
        5. View your download history below.

        **Contact Support:** [amitrathore110409@gmail](mailto:amitrathore110409@gmail.com)
        """)

# Header
st.markdown('<div class="header">📄 Invoice Splitter </div>', unsafe_allow_html=True)
st.markdown("Split multi-invoice PDFs into individual invoices with ease! Upload your file below.")

# Main layout with columns
col1, col2 = st.columns([2, 1])

with col1:
    # File uploader and preview
    st.subheader("Upload PDF")
    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=["pdf"],
        help="Upload a multi-invoice PDF file to split."
    )

    # Display PDF info and preview if uploaded
    if uploaded_file is not None:
        with st.spinner("Analyzing PDF..."):
            # Save temporarily
            temp_pdf_path = "temp_uploaded.pdf"
            with open(temp_pdf_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            # Get page count
            pdf_document = fitz.open(temp_pdf_path)
            page_count = len(pdf_document)
            # Render first page as image for preview
            page = pdf_document.load_page(0)
            pix = page.get_pixmap(matrix=fitz.Matrix(150/72, 150/72))  # 150 DPI
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            pdf_document.close()
            # Convert image to base64 for display
            buffered = io.BytesIO()
            img.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
        st.info(f"📄 **File Uploaded**: {uploaded_file.name} ({page_count} pages)")
        st.markdown(f'<img src="data:image/png;base64,{img_str}" class="preview-image" alt="PDF Preview">', unsafe_allow_html=True)

with col2:
    # Controls
    st.subheader("Actions")
    split_button = st.button("Split PDF", help="Click to split the uploaded PDF.")
    if st.button("Reset", help="Clear uploaded file and outputs."):
        if os.path.exists("output_invoices"):
            shutil.rmtree("output_invoices")
        if os.path.exists("split_log.txt"):
            os.remove("split_log.txt")
        if os.path.exists("temp_uploaded.pdf"):
            os.remove("temp_uploaded.pdf")
        st.session_state.download_history = []
        st.experimental_rerun()

# Process PDF splitting
if uploaded_file is not None and split_button:
    # Confirmation dialog
    if st.checkbox("Confirm splitting action", help="Check to proceed with splitting."):
        temp_pdf_path = "temp_uploaded.pdf"
        with open(temp_pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Progress bar
        progress = st.progress(0)
        status_text = st.empty()
        status_text.text("Starting PDF splitting...")
        progress.progress(10)
        
        try:
            # Clear previous outputs
            if os.path.exists("output_invoices"):
                shutil.rmtree("output_invoices")
            
            # Simulate progress
            progress.progress(30)
            status_text.text("Converting PDF pages...")
            time.sleep(0.5)
            
            # Split the PDF
            progress.progress(60)
            status_text.text("Analyzing pages...")
            output_files, num_invoices = split_pdf(temp_pdf_path, st.session_state.threshold)
            
            progress.progress(90)
            status_text.text("Saving output files...")
            time.sleep(0.5)
            
            # Display results
            progress.progress(100)
            status_text.text("Completed!")
            st.success(f"✅ Successfully split PDF into **{num_invoices} invoices**!")
            
            # Download section
            with st.container():
                st.markdown('<div class="download-section">', unsafe_allow_html=True)
                st.subheader("Download Invoices")
                # Individual downloads
                for output_file in output_files:
                    with open(output_file, "rb") as f:
                        st.download_button(
                            label=f"📥 Download {os.path.basename(output_file)}",
                            data=f,
                            file_name=os.path.basename(output_file),
                            mime="application/pdf",
                            help=f"Download {os.path.basename(output_file)}"
                        )
                # ZIP download
                zip_buffer = io.BytesIO()
                with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
                    for output_file in output_files:
                        zip_file.write(output_file, os.path.join("invoices", os.path.basename(output_file)))
                zip_buffer.seek(0)
                st.download_button(
                    label="📦 Download All as ZIP",
                    data=zip_buffer,
                    file_name=f"invoices_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip",
                    mime="application/zip",
                    help="Download all invoices as a ZIP file."
                )
                st.markdown('</div>', unsafe_allow_html=True)
            
            # Update download history
            history_entry = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "filename": uploaded_file.name,
                "num_invoices": num_invoices
            }
            st.session_state.download_history.append(history_entry)
            
            # Display log
            if os.path.exists("split_log.txt"):
                with open("split_log.txt", "r") as f:
                    log_content = f.read()
                with st.expander("View Split Log", expanded=False):
                    st.text_area("Log", log_content, height=200)
        
        except Exception as e:
            st.error(f"❌ Error splitting PDF: {str(e)}")
            progress.progress(0)
            status_text.text("Failed!")
        
        finally:
            if os.path.exists(temp_pdf_path):
                os.remove(temp_pdf_path)

# Download History
with st.sidebar:
    with st.expander("Download History 📜", expanded=False):
        if st.session_state.download_history:
            for entry in st.session_state.download_history:
                st.write(f"**{entry['timestamp']}**: {entry['filename']} ({entry['num_invoices']} invoices)")
        else:
            st.write("No downloads yet.")

# Footer
st.markdown(f'<div class="footer {theme_class}">Built for Hackathon | © 2025 Invoice Splitter By Amit</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)  # Close main div

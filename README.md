# INVOICE_SPLITTER
SPLIT THE PDF INVOICE IN INDIVIDUALS  INVOICE  
Invoice Splitter 📄

Invoice Splitter is a Python application that splits multi-invoice PDF files into individual invoices, using blank pages as separators. Built for a hackathon on June 5, 2025, this project features a sleek Streamlit GUI and a powerful CLI, making it ideal for both end-users and developers. It leverages advanced PDF processing to ensure accurate splitting, even with scanned documents.


🚀 Quick Start

Clone the Repo:git clone https://github.com/yourusername/invoice_splitter.git
cd invoice_splitter


Set Up Environment:python -m venv venv
.\venv\Scripts\activate  # Windows
pip install -r requirements.txt


Run the GUI:streamlit run app.py

Open http://localhost:8501 in your browser, upload a PDF, and split invoices with ease!


✨ Features

🖼️ Interactive Streamlit GUI: Upload PDFs, adjust settings, and download results effortlessly.
📜 CLI Support: Automate splitting with a command-line interface.
🔍 Blank Page Detection: Configurable threshold for accurate separation (default: 0.99).
📝 Detailed Logging: Track the process with logs in split_log.txt.
🧪 Test PDF Generator: Create sample PDFs for testing.
🌐 Cross-Platform: Works on Windows, Linux, and macOS.


🛠️ Installation
Prerequisites

🐍 Python 3.8+: Download
🌐 Git: Install
📄 Poppler: Required for PDF-to-image conversion. Install based on your OS:
Windows:
Download from GitHub.
Extract to C:\poppler.
Add C:\poppler\bin to your system PATH (Right-click This PC > Properties > Advanced system settings > Environment Variables > Edit Path).
Verify: pdftoppm --version


Linux:sudo apt-get update
sudo apt-get install poppler-utils

Verify: pdftoppm --version
macOS:brew install poppler

Verify: pdftoppm --version


🌍 Web Browser: For the Streamlit GUI (e.g., Chrome, Firefox)

Steps

Clone the Repository:git clone https://github.com/yourusername/invoice_splitter.git
cd invoice_splitter


Set Up Virtual Environment:python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/macOS


Install Dependencies:pip install -r requirements.txt


Verify Setup:
Test Poppler: pdftoppm --version
Test Streamlit: streamlit hello




📖 Usage
🌟 Streamlit GUI

Launch the app:streamlit run app.py


Open http://localhost:8501 in your browser.
Upload a PDF, adjust the threshold, and click “Split PDF”.
Download your invoices and view the split log.

💻 Command-Line Interface

Generate a test PDF (optional):python generate_test_pdf.py


Split the PDF:python split_pdf.py multi_invoice.pdf --threshold 0.99


Output: PDFs in output_invoices/
Log: split_log.txt



Example
For an 8-page PDF (2-page invoice, blank, 1-page invoice, blank, 3-page invoice):

Output: invoice_1.pdf (pages 1–2), invoice_2.pdf (page 4), invoice_3.pdf (pages 6–8).


📁 Project Structure
invoice_splitter/
├── app.py              # Streamlit GUI application
├── split_pdf.py        # Core PDF splitting logic
├── generate_test_pdf.py # Script to generate test PDFs
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
├── .gitignore          # Git ignore file
├── LICENSE             # MIT License
└── assets/             # Store demo GIFs or screenshots
    └── demo.gif


🐛 Troubleshooting

Click to expand troubleshooting tips


Poppler Not Found:
Ensure pdftoppm is in your PATH.
Reinstall Poppler and restart your terminal.


PDF Splitting Fails:
Check split_log.txt for white pixel percentages.
Adjust --threshold (e.g., 0.95).


Streamlit Issues:
Verify installation: pip install streamlit.
Run streamlit run app.py and check for errors.


Memory Errors:
In split_pdf.py, add dpi=100 to convert_from_path(input_pdf, dpi=100).






🤝 Contributing
We’d love your contributions! Here’s how:

Fork the repository.
Create a feature branch: git checkout -b feature/your-feature
Commit changes: git commit -m "Add your feature"
Push: git push origin feature/your-feature
Open a Pull Request.

Please follow PEP 8 and add comments to your code.

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

🎉 Acknowledgments

Built for a hackathon on June 5, 2025.
Thanks to PyMuPDF, pdf2image, and Streamlit.
Gratitude to the hackathon organizers for the opportunity!


Star the repo ⭐ if you find this project useful!

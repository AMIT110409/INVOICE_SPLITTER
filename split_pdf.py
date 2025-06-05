# import fitz  # PyMuPDF
# import os
# from pathlib import Path
# import argparse
# from pdf2image import convert_from_path
# from PIL import Image
# import logging
# import numpy as np

# # Set up logging
# def setup_logging():
#     logging.basicConfig(
#         level=logging.INFO,
#         format='%(asctime)s - %(levelname)s - %(message)s',
#         handlers=[
#             logging.FileHandler('split_log.txt', mode='w'),
#             logging.StreamHandler()
#         ]
#     )

# # Check if a page is blank based on white pixel percentage
# def is_page_blank(page_image, threshold=0.99):
#     try:
#         # Convert image to grayscale
#         img = page_image.convert('L')
#         # Convert to numpy array for pixel analysis
#         img_array = np.array(img)
#         # Count white or near-white pixels (value >= 240 out of 255)
#         white_pixels = np.sum(img_array >= 240)
#         total_pixels = img_array.size
#         white_ratio = white_pixels / total_pixels
#         logging.info(f"Page analyzed: {white_ratio:.2%} white pixels")
#         return white_ratio >= threshold
#     except Exception as e:
#         logging.error(f"Error analyzing page: {e}")
#         return False

# # Main function to split the PDF
# def split_pdf(input_pdf, threshold):
#     try:
#         # Open the PDF
#         pdf = fitz.open(input_pdf)
#         if pdf.page_count == 0:
#             logging.error("Input PDF is empty")
#             return

#         # Create output directory
#         output_dir = Path("output_invoices")
#         output_dir.mkdir(exist_ok=True)

#         # Convert PDF pages to images
#         logging.info("Converting PDF pages to images...")
#         images = convert_from_path(input_pdf)

#         # List to store page numbers for each invoice
#         invoices = []
#         current_invoice = []

#         # Analyze each page
#         for page_num in range(pdf.page_count):
#             if page_num >= len(images):
#                 logging.warning(f"Page {page_num + 1} could not be converted to image")
#                 continue

#             logging.info(f"Processing page {page_num + 1}")
#             if is_page_blank(images[page_num], threshold):
#                 # If current_invoice has pages, save it as an invoice
#                 if current_invoice:
#                     invoices.append(current_invoice)
#                     current_invoice = []
#             else:
#                 # Add non-blank page to current invoice
#                 current_invoice.append(page_num)

#         # Don't forget the last invoice
#         if current_invoice:
#             invoices.append(current_invoice)

#         # Save each invoice as a separate PDF
#         for idx, invoice_pages in enumerate(invoices, 1):
#             if not invoice_pages:
#                 logging.warning(f"Invoice {idx} is empty, skipping")
#                 continue

#             output_pdf = fitz.open()
#             for page_num in invoice_pages:
#                 output_pdf.insert_pdf(pdf, from_page=page_num, to_page=page_num)
#             output_path = output_dir / f"invoice_{idx}.pdf"
#             output_pdf.save(output_path)
#             output_pdf.close()
#             logging.info(f"Saved invoice_{idx}.pdf with pages {invoice_pages}")

#         pdf.close()
#         logging.info(f"Successfully split PDF into {len(invoices)} invoices")

#     except FileNotFoundError:
#         logging.error(f"Input file {input_pdf} not found")
#     except Exception as e:
#         logging.error(f"Error processing PDF: {e}")

# def main():
#     # Parse command-line arguments
#     parser = argparse.ArgumentParser(description="Split a multi-invoice PDF by blank pages")
#     parser.add_argument("input_pdf", help="Path to the input PDF file")
#     parser.add_argument("--threshold", type=float, default=0.99, help="Blank page threshold (0 to 1)")
#     args = parser.parse_args()

#     # Validate threshold
#     if not 0 <= args.threshold <= 1:
#         logging.error("Threshold must be between 0 and 1")
#         return

#     # Set up logging
#     setup_logging()
#     logging.info("Starting PDF splitting process")

#     # Split the PDF
#     split_pdf(args.input_pdf, args.threshold)

# if __name__ == "__main__":
#     main()


import argparse
import logging
import os
import numpy as np
from pdf2image import convert_from_path
import fitz  # PyMuPDF
from datetime import datetime

# Setup logging to both console and file
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("split_log.txt"),
        logging.StreamHandler()
    ]
)

def calculate_white_pixel_percentage(image):
    """Calculate the percentage of white pixels in an image."""
    # Convert image to numpy array
    img_array = np.array(image.convert('L'))  # Convert to grayscale
    white_pixels = np.sum(img_array >= 240)  # Count pixels that are nearly white (240-255)
    total_pixels = img_array.size
    white_percentage = (white_pixels / total_pixels) * 100
    return white_percentage

def split_pdf(input_pdf, threshold=0.99):
    """
    Split a multi-invoice PDF by blank pages.
    Returns: List of output PDF paths, number of invoices.
    """
    logging.info("Starting PDF splitting process")
    
    # Ensure output directory exists
    output_dir = "output_invoices"
    os.makedirs(output_dir, exist_ok=True)
    
    # Convert PDF pages to images for blank page detection
    logging.info("Converting PDF pages to images...")
    images = convert_from_path(input_pdf)
    
    # Identify blank pages
    blank_pages = []
    for i, image in enumerate(images):
        logging.info(f"Processing page {i + 1}")
        white_percentage = calculate_white_pixel_percentage(image)
        logging.info(f"Page analyzed: {white_percentage:.2f}% white pixels")
        if white_percentage >= (threshold * 100):
            blank_pages.append(i)
    
    # Open the PDF for splitting
    pdf_document = fitz.open(input_pdf)
    total_pages = len(pdf_document)
    
    # Split into invoices based on blank pages
    invoices = []
    start_page = 0
    blank_pages.append(total_pages)  # Add end of document as a boundary
    
    for blank_page in blank_pages:
        if start_page < blank_page:
            # Extract pages between start_page and blank_page
            pages = list(range(start_page, blank_page))
            invoices.append(pages)
        start_page = blank_page + 1
    
    # Save each invoice as a separate PDF
    output_files = []
    for idx, pages in enumerate(invoices, 1):
        output_pdf = os.path.join(output_dir, f"invoice_{idx}.pdf")
        new_pdf = fitz.open()
        for page_num in pages:
            new_pdf.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)
        new_pdf.save(output_pdf)
        new_pdf.close()
        logging.info(f"Saved {output_pdf} with pages {pages}")
        output_files.append(output_pdf)
    
    pdf_document.close()
    logging.info(f"Successfully split PDF into {len(invoices)} invoices")
    return output_files, len(invoices)

def main():
    """CLI entry point for splitting PDFs."""
    parser = argparse.ArgumentParser(description="Split a multi-invoice PDF by blank pages")
    parser.add_argument("input_pdf", help="Path to the input PDF file")
    parser.add_argument("--threshold", type=float, default=0.99, help="Blank page threshold (0 to 1)")
    args = parser.parse_args()
    
    if not os.path.exists(args.input_pdf):
        logging.error(f"Input PDF {args.input_pdf} does not exist.")
        return
    
    try:
        split_pdf(args.input_pdf, args.threshold)
    except Exception as e:
        logging.error(f"Error splitting PDF: {str(e)}")

if __name__ == "__main__":
    main()
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from reportlab.lib.units import inch

# def create_invoice_page(c, page_num, invoice_num):
#     """Create an invoice page with sample content."""
#     c.setFont("Helvetica", 12)
#     c.drawString(1 * inch, 10 * inch, f"Invoice {invoice_num} - Page {page_num}")
#     c.drawString(1 * inch, 9 * inch, "Sample Invoice Content")
#     c.drawString(1 * inch, 8.5 * inch, "Item: Product A | Quantity: 10 | Price: $100")
#     c.drawString(1 * inch, 8 * inch, "Item: Product B | Quantity: 5 | Price: $50")
#     c.drawString(1 * inch, 7.5 * inch, "Total: $150")
#     c.drawString(1 * inch, 7 * inch, f"Generated for testing on 2025-06-05")

# def create_blank_page(c):
#     """Create a blank page with slight noise to simulate a scanned page."""
#     c.setFont("Helvetica", 8)
#     c.setFillGray(0.9)  # Very faint gray to simulate noise
#     c.drawString(0.5 * inch, 0.5 * inch, "Scanner artifact (faint mark)")
#     c.setFillGray(0)  # Reset to black for subsequent pages

# def generate_test_pdf(output_path):
#     """Generate a test PDF with invoices and blank pages."""
#     c = canvas.Canvas(output_path, pagesize=letter)
    
#     # Invoice A: Pages 1-2
#     create_invoice_page(c, 1, "A")
#     c.showPage()
#     create_invoice_page(c, 2, "A")
#     c.showPage()
    
#     # Blank page (Page 3)
#     create_blank_page(c)
#     c.showPage()
    
#     # Invoice B: Page 4
#     create_invoice_page(c, 1, "B")
#     c.showPage()
    
#     # Blank page (Page 5)
#     create_blank_page(c)
#     c.showPage()
    
#     # Invoice C: Pages 6-8
#     create_invoice_page(c, 1, "C")
#     c.showPage()
#     create_invoice_page(c, 2, "C")
#     c.showPage()
#     create_invoice_page(c, 3, "C")
#     c.showPage()
    
#     c.save()
#     print(f"Generated {output_path}")

# if __name__ == "__main__":
#     generate_test_pdf("multi_invoice.pdf")


# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from reportlab.lib.units import inch

# def create_invoice_page(c, page_num, invoice_data):
#     """Create an invoice page with consistent format but varied content."""
#     c.setFont("Helvetica", 12)
#     c.drawString(1 * inch, 10 * inch, f"Invoice {invoice_data['id']} - Page {page_num}")
#     c.drawString(1 * inch, 9 * inch, "Invoice Details")
    
#     # Add itemized list
#     y = 8.5
#     total = 0
#     for item in invoice_data['items']:
#         c.drawString(1 * inch, y * inch, f"Item: {item['name']} | Quantity: {item['quantity']} | Price: ${item['price']}")
#         total += item['quantity'] * item['price']
#         y -= 0.5
#     c.drawString(1 * inch, y * inch, f"Total: ${total}")
#     c.drawString(1 * inch, (y - 0.5) * inch, f"Generated for testing on 2025-06-05")
    
#     # Add table
#     c.setLineWidth(1)
#     c.grid([1 * inch, 3 * inch, 5 * inch], [5 * inch, 4.5 * inch, 4 * inch])
#     c.drawString(1.2 * inch, 4.8 * inch, "Item")
#     c.drawString(3.2 * inch, 4.8 * inch, "Qty")
#     c.drawString(4.2 * inch, 4.8 * inch, "Price")
#     c.drawString(1.2 * inch, 4.3 * inch, invoice_data['items'][0]['name'])
#     c.drawString(3.2 * inch, 4.3 * inch, str(invoice_data['items'][0]['quantity']))
#     c.drawString(4.2 * inch, 4.3 * inch, f"${invoice_data['items'][0]['price']}")

# def create_blank_page(c):
#     """Create a blank page with slight noise."""
#     c.setFont("Helvetica", 8)
#     c.setFillGray(0.9)  # Very faint gray
#     c.drawString(0.5 * inch, 0.5 * inch, "Scanner artifact (faint mark)")
#     c.setFillGray(0)  # Reset to black

# def generate_test_pdf(output_path):
#     """Generate a test PDF with varied invoices and blank pages."""
#     c = canvas.Canvas(output_path, pagesize=letter)
    
#     # Invoice A: 2 pages
#     invoice_a = {
#         'id': 'A',
#         'items': [
#             {'name': 'Widget X', 'quantity': 10, 'price': 100},
#             {'name': 'Gadget Y', 'quantity': 5, 'price': 50},
#             {'name': 'Tool Z', 'quantity': 20, 'price': 200}
#         ]
#     }
#     create_invoice_page(c, 1, invoice_a)
#     c.showPage()
#     create_invoice_page(c, 2, invoice_a)
#     c.showPage()
    
#     # Blank page (Page 3)
#     create_blank_page(c)
#     c.showPage()
    
#     # Invoice B: 1 page
#     invoice_b = {
#         'id': 'B',
#         'items': [
#             {'name': 'Component P', 'quantity': 8, 'price': 75},
#             {'name': 'Device Q', 'quantity': 12, 'price': 60}
#         ]
#     }
#     create_invoice_page(c, 1, invoice_b)
#     c.showPage()
    
#     # Blank page (Page 5)
#     create_blank_page(c)
#     c.showPage()
    
#     # Invoice C: 3 pages
#     invoice_c = {
#         'id': 'C',
#         'items': [
#             {'name': 'Machine R', 'quantity': 15, 'price': 150},
#             {'name': 'Part S', 'quantity': 25, 'price': 40},
#             {'name': 'Unit T', 'quantity': 10, 'price': 80}
#         ]
#     }
#     create_invoice_page(c, 1, invoice_c)
#     c.showPage()
#     create_invoice_page(c, 2, invoice_c)
#     c.showPage()
#     create_invoice_page(c, 3, invoice_c)
#     c.showPage()
    
#     c.save()
#     print(f"Generated {output_path}")

# if __name__ == "__main__":
#     generate_test_pdf("multi_invoice.pdf")

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import lightgrey

def create_invoice_page(c, page_num, invoice_data):
    """Create an invoice page with a professional format."""
    c.setFont("Helvetica", 12)
    
    # Header: Company Info
    c.setFillColor(lightgrey)
    c.rect(1 * inch, 10 * inch, 6.5 * inch, 0.8 * inch, fill=1)
    c.setFillColor("black")
    c.setFont("Helvetica-Bold", 14)
    c.drawString(1.2 * inch, 10.5 * inch, "Tech Supplies Inc.")
    c.setFont("Helvetica", 10)
    c.drawString(1.2 * inch, 10.3 * inch, "123 Business Road, City, Country")
    c.drawString(1.2 * inch, 10.1 * inch, "Phone: (123) 456-7890 | Email: sales@techsupplies.com")
    
    # Invoice Details
    c.setFont("Helvetica", 12)
    c.drawString(5 * inch, 9.5 * inch, f"Invoice {invoice_data['id']}")
    c.drawString(5 * inch, 9.2 * inch, f"Date: 2025-06-05")
    
    # Bill To
    c.drawString(1 * inch, 8.8 * inch, "Bill To:")
    c.drawString(1 * inch, 8.5 * inch, invoice_data['customer'])
    c.drawString(1 * inch, 8.2 * inch, invoice_data['customer_address'])
    
    # Itemized Table
    c.setLineWidth(1)
    table_y = [7.5 * inch, 7.2 * inch] + [(7.2 - i * 0.5) * inch for i in range(len(invoice_data['items']))]
    c.grid([1 * inch, 3 * inch, 4.5 * inch, 6 * inch], table_y)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1.2 * inch, 7.3 * inch, "Item Description")
    c.drawString(3.2 * inch, 7.3 * inch, "Quantity")
    c.drawString(4.7 * inch, 7.3 * inch, "Unit Price")
    c.drawString(5.2 * inch, 7.3 * inch, "Total")
    c.setFont("Helvetica", 10)
    total = 0
    for i, item in enumerate(invoice_data['items']):
        y = 7.2 - i * 0.5
        item_total = item['quantity'] * item['price']
        total += item_total
        c.drawString(1.2 * inch, y * inch, item['name'])
        c.drawString(3.2 * inch, y * inch, str(item['quantity']))
        c.drawString(4.7 * inch, y * inch, f"${item['price']:.2f}")
        c.drawString(5.2 * inch, y * inch, f"${item_total:.2f}")
    
    # Totals
    tax_rate = 0.05
    tax = total * tax_rate
    grand_total = total + tax
    y = 7.2 - len(invoice_data['items']) * 0.5
    c.setFont("Helvetica", 11)
    c.drawString(4 * inch, (y - 0.5) * inch, f"Subtotal: ${total:.2f}")
    c.drawString(4 * inch, (y - 0.8) * inch, f"Tax (5%): ${tax:.2f}")
    c.setFont("Helvetica-Bold", 11)
    c.drawString(4 * inch, (y - 1.1) * inch, f"Grand Total: ${grand_total:.2f}")
    
    # Footer
    c.setFont("Helvetica", 10)
    c.drawString(1 * inch, 1 * inch, "Payment Terms: Due within 30 days")
    c.drawString(1 * inch, 0.8 * inch, "Thank you for your business!")
    c.line(1 * inch, 0.6 * inch, 7.5 * inch, 0.6 * inch)
    c.drawString(1 * inch, 0.4 * inch, f"Page {page_num}")

def create_blank_page(c):
    """Create a blank page with slight noise."""
    c.setFont("Helvetica", 8)
    c.setFillGray(0.9)
    c.drawString(0.5 * inch, 0.5 * inch, "Scanner artifact (faint mark)")
    c.setFillGray(0)

def generate_test_pdf(output_path):
    """Generate a test PDF with professional invoices and blank pages."""
    c = canvas.Canvas(output_path, pagesize=letter)
    
    # Invoice A: 2 pages
    invoice_a = {
        'id': '001',
        'customer': 'ABC Corp',
        'customer_address': '456 Client Street, City, Country',
        'items': [
            {'name': 'Laptop Pro', 'quantity': 2, 'price': 1000},
            {'name': 'Mouse', 'quantity': 5, 'price': 20},
            {'name': 'Keyboard', 'quantity': 3, 'price': 50}
        ]
    }
    create_invoice_page(c, 1, invoice_a)
    c.showPage()
    create_invoice_page(c, 2, invoice_a)
    c.showPage()
    
    # Blank page (Page 3)
    create_blank_page(c)
    c.showPage()
    
    # Invoice B: 1 page
    invoice_b = {
        'id': '002',
        'customer': 'XYZ Ltd',
        'customer_address': '789 Business Avenue, City, Country',
        'items': [
            {'name': 'Monitor', 'quantity': 1, 'price': 300},
            {'name': 'Webcam', 'quantity': 4, 'price': 60}
        ]
    }
    create_invoice_page(c, 1, invoice_b)
    c.showPage()
    
    # Blank page (Page 5)
    create_blank_page(c)
    c.showPage()
    
    # Invoice C: 3 pages
    invoice_c = {
        'id': '003',
        'customer': 'Tech Solutions',
        'customer_address': '101 Tech Park, City, Country',
        'items': [
            {'name': 'Server', 'quantity': 1, 'price': 2000},
            {'name': 'Router', 'quantity': 2, 'price': 150},
            {'name': 'Switch', 'quantity': 5, 'price': 100}
        ]
    }
    create_invoice_page(c, 1, invoice_c)
    c.showPage()
    create_invoice_page(c, 2, invoice_c)
    c.showPage()
    create_invoice_page(c, 3, invoice_c)
    c.showPage()
    
    c.save()
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_test_pdf("multi_invoice.pdf")
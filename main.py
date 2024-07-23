import sys  # Import the sys module to handle command-line arguments
from pypdf import PdfWriter  # Import PdfWriter from the pypdf library to manipulate PDF 

def extract_first(input_pdf, output_pdf, pages=3):
    """
    Function to extract the first few pages from an input PDF and save them to an output PDF.
    
    Parameters:
    input_pdf (str): The path to the input PDF file.
    output_pdf (str): The path to the output PDF file.
    pages (int): The number of pages to extract from the start (default is 3).
    """
    
    # Open the input PDF file in binary read mode
    reader = open(input_pdf, "rb")
    
    # Create a PdfWriter object to write the extracted pages to a new PDF
    writer = PdfWriter()

    # Extract the specified number of pages from the beginning of the PDF
    writer.append(fileobj=reader, pages=(0, pages))

    # Open the output PDF file in binary write mode
    output_pdf = open(output_pdf, "wb")

    # Write the pages that were added to the writer to the output PDF file
    writer.write(output_pdf)

    # Close the writer and output PDF file to free up resources
    writer.close()
    output_pdf.close()

if __name__ == "__main__":
    # Check if the number of command-line arguments is correct
    if len(sys.argv) != 3:
        # If not, print a usage message and exit with a status code of 1 (indicating an error)
        print("Usage: python3 main.py <input_pdf> <output_pdf>")
        sys.exit(1)

    # Get the input and output file paths from the command-line arguments
    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]

    # Call the function to extract the first few pages from the input PDF and save to the output PDF
    extract_first(input_pdf, output_pdf)

    # Print a message indicating the operation was successful
    print(f"First 3 pages of {input_pdf} have been saved as {output_pdf}")

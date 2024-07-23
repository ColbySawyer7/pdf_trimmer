import sys  # Import the sys module to handle command-line arguments
from pypdf import PdfWriter  # Import PdfWriter from the pypdf library to manipulate PDF 
import pymupdf
import fitz

# Read single PDF, trim it to size and then name a new output file based on the extracted text

class CCGFile:
    def __init__(self, ccg_order: str = None, lot: int = None, date: str = None):
        self.ccg_order = ccg_order
        self.lot = lot
        self.date = date

    # Method to check that all parameters are not None
    def validate(self):
        if self.ccg_order is None or self.lot is None or self.date is None:
            raise ValueError("All parameters must be non-None.")
        return True

def extract_first(input_pdf, pages=3):
    """
    Function to extract the first few pages from an input PDF and save them to an output PDF.
    
    Parameters:
    input_pdf (str): The path to the input PDF file.
    pages (int): The number of pages to extract from the start (default is 3).
    """
    
    # Open the input PDF file in binary read mode
    reader = pymupdf.open(input_pdf)
    
    # Create a PdfWriter object to write the extracted pages to a new PDF
    writer = PdfWriter()

    # Determine the number of pages to extract
    pages_to_extract = min(reader.page_count, pages)

    reader = open(input_pdf, "rb")
    
    # Extract the specified number of pages from the beginning of the PDF
    writer.append(fileobj=reader, pages=(0, pages_to_extract))
        
    ccg_file: CCGFile = find_keywords(input_pdf)

    if ccg_file.validate:
        # Open the output PDF file in binary write mode
        sanitized_date = ccg_file.date.replace('/', '')
        output_pdf = open(f'{ccg_file.ccg_order}-{ccg_file.lot}-{sanitized_date}.pdf', "wb")

        # Write the pages that were added to the writer to the output PDF file
        writer.write(output_pdf)

        # Close the writer and output PDF file to free up resources
        writer.close()
        output_pdf.close()
    else:
        reader.close()
        writer.close()

def find_keywords(input_pdf):
    info = CCGFile() 
    doc = fitz.open(input_pdf)  # example document
    page = doc[0]  # first page
    words = page.get_text("words", sort=True)  # extract sorted words

    for i, word in enumerate(words):
        # information items will be found prefixed with their "key"
        text = word[4]
        #print(f'Index:{i}, Word: {text}')
        if text == "DATE:":  # the following word will be the date!
            date = words[i + 1][4]
            print("DATE:", date)
            info.date = date
        elif text == "CCG":
            if words[i + 1][4] == "ORDER" and words[i + 2][4] == "#:":
                ccg_order = words[i+3][4]
                print("CCG ORDER #:", ccg_order)
                info.ccg_order = ccg_order
        elif text == "LOT":
            if words[i + 1][4] == "#:":
                lot = words[i + 2][4]
                print("LOT #:", lot)
                info.lot = lot
    
    return info

if __name__ == "__main__":
    # Check if the number of command-line arguments is correct
    if len(sys.argv) != 2:
        # If not, print a usage message and exit with a status code of 1 (indicating an error)
        print("Usage: python3 main.py <input_pdf>")
        sys.exit(1)

    # Get the input and output file paths from the command-line arguments
    input_pdf = sys.argv[1]
    #output_pdf = sys.argv[2]

    # Call the function to extract the first few pages from the input PDF and save to the output PDF
    extract_first(input_pdf)

    # Print a message indicating the operation was successful
    #print(f"First 3 pages of {input_pdf} have been saved as {output_pdf}")

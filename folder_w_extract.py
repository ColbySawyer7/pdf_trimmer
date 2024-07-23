import sys  # Importing the sys module to get command line arguments
import os   # Importing the os module to interact with the operating system
from pypdf import PdfWriter  # Importing PdfWriter from pypdf to handle PDF writing
import pymupdf
import fitz

# Trim all PDFs in input directory, renaming based on extracted text

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

def extract_first(input_pdf, output_loc, pages=3):
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
        filename = f'{ccg_file.ccg_order}-{ccg_file.lot}-{sanitized_date}.pdf'
        
        output_pdf = open(os.path.join(output_loc, filename), "wb")

        # Write the pages that were added to the writer to the output PDF file
        writer.write(output_pdf)

        # Close the writer and output PDF file to free up resources
        writer.close()
        output_pdf.close()
    else:
        reader.close()
        writer.close()

def process_folder(pages=3):
    """
    Function to process all the PDF files inside a specified folder
    
    Parameters:
    pages (int): The number of pages to extract from the start (default is 3).
    """
    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        # Check if the file has a .pdf extension
        if filename.endswith(".pdf"):
            # Construct the full paths for the input and output PDF files
            input_pdf = os.path.join(input_folder, filename)
            # Call the extract_first function to process the file
            extract_first(input_pdf, output_folder, pages)
            # Print a message indicating successful processing
            # print(f"First {pages} pages of {input_pdf} have been saved as {output_pdf}")

def find_keywords(input_pdf):
    info = CCGFile() 
    doc = fitz.open(input_pdf)  # example document
    page = doc[0]  # first page
    words = page.get_text("words", sort=True)  # extract sorted words

    for i, word in enumerate(words):
        # information items will be found prefixed with their "key"
        text = word[4]
        print(f'Index:{i}, Word: {text}')
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

# This is the main entry point of the script
if __name__ == "__main__":
    # Check if the script was run with exactly two command line arguments (excluding the script name)
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_folder> <output_folder>")
        sys.exit(1)  # Exit the script with an error code

    # Assign the arguments to variables for the input and output folders
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    # Check if the input folder exists
    if not os.path.isdir(input_folder):
        print(f"Input folder {input_folder} does not exist.")
        sys.exit(1)  # Exit the script with an error code

    # Check if the output folder exists; if not, create it
    if not os.path.isdir(output_folder):
        os.makedirs(output_folder)

    # Process all PDF files in the input folder
    process_folder()

    # Print a message indicating that processing is complete
    print("Processing complete.")

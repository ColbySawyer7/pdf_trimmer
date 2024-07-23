import sys  # Importing the sys module to get command line arguments
import os   # Importing the os module to interact with the operating system
from pypdf import PdfWriter  # Importing PdfWriter from pypdf to handle PDF writing

# Take all PDFs from one folder, extract first 3 pages and then save as new PDF based on new name

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
    # Create a PdfWriter object to write PDF content
    writer = PdfWriter()

    # Append the first few pages from the reader to the writer
    writer.append(fileobj=reader, pages=(0, pages))

    # Open the output PDF file in binary write mode and write the content from the writer to it
    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)

    # Close both the writer and reader to free up resources
    writer.close()
    reader.close()

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
            output_pdf = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_output.pdf")
            # Call the extract_first function to process the file
            extract_first(input_pdf, output_pdf, pages)
            # Print a message indicating successful processing
            print(f"First {pages} pages of {input_pdf} have been saved as {output_pdf}")

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

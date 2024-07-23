import sys
import os
from pypdf import PdfWriter

def extract_first(input_pdf, output_pdf, pages=3):
    # Open file to read from (Reader) and Writer
    reader = open(input_pdf, "rb")
    writer = PdfWriter()

    # Extract first 3 pages of pdf
    writer.append(fileobj=reader, pages=(0, pages))

    # Start Output PDF and Write to it 
    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)

    # Close Writer and Reader
    writer.close()
    reader.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_folder> <output_folder>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    if not os.path.isdir(input_folder):
        print(f"Input folder {input_folder} does not exist.")
        sys.exit(1)

    if not os.path.isdir(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            input_pdf = os.path.join(input_folder, filename)
            output_pdf = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_output.pdf")
            extract_first(input_pdf, output_pdf)
            print(f"First 3 pages of {input_pdf} have been saved as {output_pdf}")

    print("Processing complete.")

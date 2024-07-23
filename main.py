import sys
from pypdf import PdfWriter

def extract_first(input_pdf, output_pdf, pages=3):
    # Open file to read from (Reader) and Writer
    reader = open(input_pdf, "rb")
    writer = PdfWriter()

    # Extract first 3 pages of pdf
    writer.append(fileobj=reader, pages=(0, pages))

    # Start Output PDF and Write to it 
    output_pdf = open(output_pdf, "wb")
    writer.write(output_pdf)

    # Close Writer and Output file
    writer.close()
    output_pdf.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 main.py <input_pdf> <output_pdf>")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    #number = sys.argv[3]

    extract_first(input_pdf, output_pdf)
    print(f"First 3 pages of {input_pdf} have been saved as {output_pdf}")

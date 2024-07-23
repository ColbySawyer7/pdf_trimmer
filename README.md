# Python PDF Stripper

The script is a Python program designed to extract the first three pages from a given PDF file and save them as a new PDF file. It uses the `pypdf` library to handle the PDF file operations.

#### Key Components of the Script:

1. **Importing Libraries:**
   - `sys`: A module that provides access to command-line arguments.
   - `PdfWriter` from `pypdf`: A class to create and manipulate PDF files.

2. **Function Definition - `extract_first`:**
   - **Parameters:**
     - `input_pdf`: The filename (or path) of the PDF file to read from.
     - `output_pdf`: The filename (or path) of the new PDF file to save the extracted pages.
     - `pages`: Optional parameter specifying the number of pages to extract. Default is set to 3.
   - **Functionality:**
     - Opens the `input_pdf` file in binary read mode (`rb`).
     - Initializes a `PdfWriter` object to create a new PDF.
     - Appends the first `pages` pages (default is 3) from the `input_pdf` to the `PdfWriter` object.
     - Opens the `output_pdf` file in binary write mode (`wb`).
     - Writes the extracted pages to the `output_pdf`.
     - Closes the `PdfWriter` and the output file to ensure all data is properly saved and resources are freed.

3. **Main Execution Block:**
   - Checks if the script receives exactly three command-line arguments: the script name, `input_pdf`, and `output_pdf`.
   - If not, it prints a usage message and exits.
   - Otherwise, it extracts the command-line arguments for `input_pdf` and `output_pdf`.
   - Calls the `extract_first` function with these arguments to perform the extraction.
   - Prints a success message indicating the operation is complete.

#### Usage:

To run the script, use the following command in the terminal:

```bash
python extract_pages.py <input_pdf> <output_pdf>
```

- `<input_pdf>`: Replace with the path to the PDF file from which you want to extract the first three pages.
- `<output_pdf>`: Replace with the desired path for the new PDF file containing the extracted pages.

For example:

```bash
python extract_pages.py input.pdf output.pdf
```

This will take `input.pdf`, extract the first three pages, and save them as `output.pdf`.

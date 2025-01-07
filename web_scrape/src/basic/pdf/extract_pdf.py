from pathlib import Path
import camelot # Very week lib, better to find another one.

FILE_NAME = "foo.pdf"
CURRENT_DIR = Path(__file__).parent
pdf_file = Path(CURRENT_DIR / FILE_NAME)

if not pdf_file.exists():
    raise FileNotFoundError("Pdf file not found")

tables = camelot.read_pdf(str(pdf_file), pages="1")
print(tables)
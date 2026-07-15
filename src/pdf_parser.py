import pdfplumber
import os

# Path to your resume PDF
pdf_path = r"C:\Users\hp\Documents\resume-project\data\swathi_updated_resume (1).pdf"

# Path to save extracted text
output_path = r"C:\Users\hp\Documents\resume-project\output\resume.txt"


def save_text(text, output_path):
    """Save extracted text to a file."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)


# Extract text from PDF
with pdfplumber.open(pdf_path) as pdf:
    text = ""

    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

# Print first 500 characters
print("=" * 60)
print("First 500 characters:\n")
print(text[:500])
print("=" * 60)

# Save the extracted text
save_text(text, output_path)

print(f"\n✅ Text saved successfully to:\n{output_path}")
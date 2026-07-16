import os
import re


def load_text(file_path):
    """
    Load text from a file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def clean_text(text):
    """
    Clean extracted resume text.
    """

    # Remove extra spaces and tabs
    text = re.sub(r"[ \t]+", " ", text)

    # Remove multiple blank lines
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    # Remove unnecessary special characters
    text = re.sub(r"[•▪►■]", "", text)

    # Remove leading/trailing whitespace
    text = text.strip()

    return text


def save_text(text, output_path):
    """
    Save cleaned text to a file.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)


if __name__ == "__main__":

    # Input file generated from pdf_parser.py
    input_path = r"C:\Users\hp\Documents\resume-project\output\resume.txt"

    # Output cleaned file
    output_path = r"C:\Users\hp\Documents\resume-project\output\clean_resume.txt"

    # Check input file exists
    if not os.path.exists(input_path):
        print("❌ resume.txt not found!")
        print(input_path)
        exit()

    print("✅ Resume text found.")
    print(f"Reading: {input_path}\n")

    # Load text
    resume_text = load_text(input_path)

    # Clean text
    cleaned_text = clean_text(resume_text)

    # Display preview
    print("=" * 60)
    print("First 500 characters of cleaned text:\n")
    print(cleaned_text[:500])
    print("=" * 60)

    # Save cleaned text
    save_text(cleaned_text, output_path)

    print(f"\n✅ Cleaned text successfully saved to:\n{output_path}")
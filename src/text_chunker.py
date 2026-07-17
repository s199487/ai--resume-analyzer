import os
import json


def load_text(file_path):
    """
    Load cleaned resume text from a file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def chunk_text(text, chunk_size=200, overlap=50):
    """
    Split text into overlapping chunks.

    chunk_size = Number of words in each chunk.
    overlap = Number of words shared between consecutive chunks.
    """
    words = text.split()
    chunks = []

    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)

        start += (chunk_size - overlap)

    return chunks


def save_chunks(chunks, output_path):
    """
    Save chunks to a JSON file.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(chunks, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":

    input_path = r"C:\Users\hp\Documents\resume-project\output\clean_resume.txt"

    output_path = r"C:\Users\hp\Documents\resume-project\output\chunks.json"

    if not os.path.exists(input_path):
        print("❌ clean_resume.txt not found!")
        exit()

    print("✅ Reading cleaned resume...")

    text = load_text(input_path)

    chunks = chunk_text(
        text=text,
        chunk_size=200,
        overlap=50
    )

    print(f"\n✅ Total Chunks Created: {len(chunks)}")

    print("\n========== First Chunk Preview ==========\n")
    print(chunks[0])
    print("\n=========================================\n")

    save_chunks(chunks, output_path)

    print(f"✅ Chunks saved successfully to:\n{output_path}")

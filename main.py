import os
import pdfplumber


def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text


def main():
    pdf_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'PDF Files')

    files = os.listdir(pdf_dir)

    for file_name in files:
        if file_name.endswith('.pdf'):
            pdf_path = os.path.join(pdf_dir, file_name)
            text = extract_text_from_pdf(pdf_path)

            txt_path = os.path.splitext(pdf_path)[0] + '.txt'
            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(text)

    print("Text extraction complete.")


if __name__ == "__main__":
    main()

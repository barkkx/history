import pdfplumber

from gtts import gTTS


def get_pdf_text(pdf_file):
    with pdfplumber.PDF(open(pdf_file, mode='rb')) as file:
        pages = file.pages
        pdf_text = ''.join(page.extract_text() for page in pages)
        pdf_text.replace("\n", ' ')
    return pdf_text


def get_media_file(pdf_text):
    language = 'ru'
    phrase = gTTS(text=pdf_text, lang=language, slow=False)
    phrase.save("text.mp3")


def main():
    file_path = "Text.pdf"
    pdf_text = get_pdf_text(file_path)
    get_media_file(pdf_text)


if __name__ == '__main__':
    main()

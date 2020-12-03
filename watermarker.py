import PyPDF2
import sys

# inputs two or more pdf files and merges them into one


def pdf_watermarker(template_file, watermark_file, output_file):
    template = PyPDF2.PdfFileReader(open(template_file, 'rb'))
    watermark = PyPDF2.PdfFileReader(open(watermark_file, 'rb'))
    output = PyPDF2.PdfFileWriter()

    for i in range(template.numPages):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

    with open(output_file, 'wb') as file:
        output.write(file)


def main():
    template = sys.argv[1]
    watermark = sys.argv[2]
    output = sys.argv[3]
    pdf_watermarker(template, watermark, output)


if __name__ == "__main__":
    main()

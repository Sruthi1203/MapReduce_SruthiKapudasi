import PyPDF2

def extract_pages(pdf_path, start_page, end_page, output_file):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        with open(output_file, 'w', encoding='utf-8') as output:
            for page_num in range(start_page - 1, end_page):
                page = reader.pages[page_num]
                text = page.extract_text()
                if text:
                    output.write(text)
                    output.write("\n")

#PDF path
pdf_path = 'Harry_Potter.pdf'
#Date of birth 09/24/2000

# Extract for file.txt (pages 3117-3127) (Birthday Month: September: 9/2=4.5 = rounded to 5. From Chapter 5(Page 3093): My birth date is 24. 
# So I started from 24th page and took next 10 pages.)
extract_pages(pdf_path, 3117, 3127, 'file.txt')

# Extract for file2.txt (pages 3193-3202) (Birth Year : 2000, last two dogits is 00, adding 1 in front: 100: 3093: 3193-3203)
extract_pages(pdf_path, 3193, 3203, 'file2.txt')

print("Pages extracted and saved to file.txt and file2.txt")


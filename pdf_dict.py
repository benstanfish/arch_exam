from pathlib import Path
import os, json
import pymupdf

source_dir = './pdfs'
pdf_dict_path = 'dict.json' 

sections = ['gakka1_2', 'gakka3', 'gakka4_5']
years = list(range(2015, 2025))

pdfs_by_year = {}
for year in years:
    pdfs_by_year[year] = [file for file in os.listdir(source_dir) if \
                           'other' not in file and str(year) in file]

pdfS_by_section = {}
for section in sections:
    pdfS_by_section[section] = [file for file in os.listdir(source_dir) if \
                           'other' not in file and section in file]

pdf_dict = {
    'year': pdfs_by_year,
    'section': pdfS_by_section
}

with open(pdf_dict_path, 'w', encoding='utf-8') as file:
    json.dump(pdf_dict, file, ensure_ascii=False, indent=4)



# # print(text)

#     # for page in doc:
#     #     print(page.get_text())
#     pages = [page for page in doc.pages()]
#     # for page in pages:
#     #     print(page.get_text())
#     #print(pages[1].get_text())
#     # print(pages[12].get_images())
#     # print(pages[12].get_image_info())
#     a_page = pages[12]
#     # page_dict = a_page.get_text('dict')
#     # for item in page_dict:
#     #     print(item)

#     # blocks = page_dict['blocks']
#     # for item in blocks:
#     #     print(item['type'])
#     # print(a_page.get_drawings())
#     svg_content = a_page.get_svg_image()
#     print(svg_content)
#     with open('output.svg', 'w') as f:
#         f.write(svg_content)
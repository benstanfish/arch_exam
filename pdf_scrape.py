from pathlib import Path
import os
import pymupdf

dir = r'.\jaeic_pdfs'
abs_dir = Path(dir).absolute()

files = []
for root, dirnames, filenames in os.walk(abs_dir):
    for filename in filenames:
        files.append(root + '\\' + filename)

selected_files = [file for file in files
                  if 'gakka' in file
                  and 'toan' not in file]
# for file in selected_files:
#     print(file)


selected_file = selected_files[0]
with pymupdf.open(selected_file) as doc:
#     text = chr(12).join([page.get_text() for page in doc])

# Path(Path(selected_file).stem + '.txt').write_bytes(text.encode('utf16'))

# print(text)

    # for page in doc:
    #     print(page.get_text())
    pages = [page for page in doc.pages()]
    # for page in pages:
    #     print(page.get_text())
    #print(pages[1].get_text())
    # print(pages[12].get_images())
    # print(pages[12].get_image_info())
    a_page = pages[12]
    # page_dict = a_page.get_text('dict')
    # for item in page_dict:
    #     print(item)

    # blocks = page_dict['blocks']
    # for item in blocks:
    #     print(item['type'])
    # print(a_page.get_drawings())
    svg_content = a_page.get_svg_image()
    print(svg_content)
    with open('output.svg', 'w') as f:
        f.write(svg_content)
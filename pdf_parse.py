from pathlib import Path
import os, json
import pymupdf

source_dir = './pdfs'
output_dir = './out'
pdf_dict_path = 'dict.json'

sections = ['gakka1_2', 'gakka3', 'gakka4_5']
years = list(range(2015, 2025))

with open(pdf_dict_path, 'r') as file:
    data = json.load(file)

by_year = data['year']
by_section = data['section']


#region Create Folders for Output Files

# def check_or_make_dir(dir_path):
#     if os.path.exists(dir_path) and os.path.isdir(dir_path):
#         pass
#     else:
#         os.mkdir(os.path.abspath(dir_path))

# check_or_make_dir(output_dir)
# for section in by_section:
#     section_dir = os.path.join(os.path.abspath(output_dir), section)
#     check_or_make_dir(section_dir)

#endregion

# for file in by_section['gakka3']:
#     file_rel_path = os.path.join(source_dir, file)

a_file = by_section['gakka4_5'][0]



def scrub(a_string):
    temp = a_string
    """
        Notes: I put an extra space after the period for ．
    """
    replace_chars = {
        '０': '0',
        '１': '1',
        '２': '2',
        '３': '3',
        '４': '4',
        '５': '5',
        '６': '6',
        '７': '7',
        '８': '8',
        '９': '9',
        '워': '²',
        '．': '. ',
        '\n\ueeb7\ueeb9\n': '/',
        '\n\ueeb7\ueeb8\n': '/',
        '\n\ueeb7\ueeb8\ueeb9\n': '/',
        '\uee4c\n\uee4d\n\uee4e': '(',
        '\uee4f\n\uee50\n\uee51': ')',
        '쓕': '「',
        '\n': ''
    }
    for bad_char in replace_chars.keys():
        temp = temp.replace(bad_char, replace_chars[bad_char])
    return temp


is_inspect_mode = True



with pymupdf.open(os.path.join(source_dir, a_file)) as doc:
    pages = [page for page in doc.pages()]

    if is_inspect_mode:
        page_no = 1
        line_no = 30
        
        a_page = pages[page_no].get_text('blocks')
        for index, line in enumerate(a_page):
            print(index, line[4].replace('\n', ''))

        a_line = a_page[line_no]
        print(a_line)

    else:

        out_dict = {}
        for index, page in enumerate(pages):
            page_key = index
            page_content = []
            blocks = page.get_text('blocks')
            for block in blocks:
                page_content.append(scrub(block[4]))
            if len(page_content) > 0:
                out_dict[index] = page_content
        
        with open('out_dict.json', 'w', encoding='utf-8') as json_file:
            json.dump(out_dict, json_file, ensure_ascii=False, indent=4)




    # blocks = [block for block in pages[1].get_text('blocks')]
    # for block in blocks:
    #     print(block[4].replace('\n', ''))



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
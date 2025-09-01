import os
import shutil

source_dir = './pdfs'
target_dir = source_dir + '/other'

files_not_containing_gakka = [file for file in os.listdir(source_dir) if 'gakka' not in file]
for file in files_not_containing_gakka:
    try:
        shutil.move(
            os.path.join(source_dir, file),
            os.path.join(target_dir, file)
        )
    except Exception as e:
        print(e)

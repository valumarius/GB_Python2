import zipfile
import hashlib
import os

with zipfile.ZipFile("files/file1.zip") as zip_ref:
    zip_ref.extractall()

with open("file1/parts.md5") as parts_md5:
    hashes = parts_md5.read().split('\n')
    hashes.remove('')

dir_list = os.listdir("file1")
dir_list.remove('parts.md5')

counter = 0
for line in hashes:
    for file in dir_list[:]:
        with open("file1/{}".format(file), "rb") as f:
            content = f.read()
            h = hashlib.md5()
            h.update(content)
            counter += 1
            print(counter)
            if h.hexdigest() == line:
                with open("blablablah", "ba") as f_out:
                    r = f_out.write(content)
                dir_list.remove(file)

import gzip
import shutil
with open('C:\\Users\\Tron\\Desktop\\hilbert\\pics\\test2.png', 'rb') as f_in:
    with gzip.open('C:\\Users\\Tron\\Desktop\\hilbert\\test2_compress.png.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

# with gzip.open('C:\\Users\\Tron\\Desktop\\hilbert\\test2_compress.png.gz', 'rb') as f:
#     file_content = f.read()

# # file_content=file_content.decode()
# file_content.save("C:\\Users\\Tron\\Desktop\\hilbert\\reworked2_compress.png",optimize=True) #compress lvl 9 
# import zlib
# s = b'This is a Byte String.'
# compressed = zlib.compress(s)
# print("Compressed String:", compressed)

# decompressed = zlib.decompress(compressed)
# print("\nDecompressed String:", decompressed)



############################
# import zlib
# import codecs

# my_data = 'Hello world'

# new_data = zlib.compress(my_data.encode())
# compressed_data = zlib.compress(new_data)
# f = open('C:\\Users\\Tron\\Desktop\\hilbert\\helloworld.txt', 'wb')
# f.write(compressed_data)
# f.close()
# decompressed_data = zlib.decompress(compressed_data)
# new_data = zlib.compress(decompressed_data.decode())
# print('Decompressed data: ' + decompressed_data)



### https://stackoverflow.com/questions/12468179/unicodedecodeerror-utf8-codec-cant-decode-byte-0x9c zadnji error


import gzip
content = b"Lots of content here"
with gzip.open('C:\\Users\\Tron\\Desktop\\hilbert\\helloworld.txt.gz', 'wb') as f:
    f.write(content)

with gzip.open('C:\\Users\\Tron\\Desktop\\hilbert\\helloworld.txt.gz', 'rb') as f:
    file_content = f.read()

print(file_content)

# import time

# print(time.time())
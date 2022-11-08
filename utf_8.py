import sys
import os

print(sys.getdefaultencoding())
print()

print(ord('a'))
print(chr(97))
print()

s = 'hello'
enc_ascii = s.encode('ascii')
enc_utf8 = s.encode('utf8')
enc_utf16 = s.encode('utf16')

print(type(enc_utf8))
print(type(enc_utf16))
print(type(enc_ascii))
print()

print(enc_utf8)
print(enc_utf16)
print(enc_ascii)
print()

print(len(enc_utf8))
print(len(enc_utf16))
print(len(enc_ascii))
print()

str_in_bytes = b'hello'
str_in_byte = s.encode('utf8')
str_in_text = 'hello'
ba = bytearray(b'hello')
ba[0] = 87
result = str(str_in_bytes, 'utf8')
add_result = str_in_bytes.decode('utf8')
print(ba)
print(str_in_bytes)
print(str_in_byte)
print('hello'.encode('utf8'))
print('привет'.encode('utf8'))
print(str_in_bytes[0])
print(str_in_text[0])
print(type(str_in_bytes))
print(result)
print(add_result)
print()

jpeg = [120, 80, 97, 80, 230]
with open(r'jpeg.bin', 'w+b') as jp:
    jp.write(bytes(jpeg))
with open(r'jpeg.bin', 'rb') as jpg:
    data = jpg.read()
    for b in data:
        print(int(b))
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/3?style=for-the-badge) ![GitHub](https://img.shields.io/github/license/CRPrinzler/HASH-verify?style=for-the-badge) ![GitHub last commit](https://img.shields.io/github/last-commit/CRPrinzler/HASH-verify?style=for-the-badge)

# HASH-verify
Verify file hashes of downloaded files easily in a GUI

![alt text](https://user-images.githubusercontent.com/11914696/139138144-72e78738-2906-46af-bb4a-f25265193dc0.png)

## What it does...
This gui based Python3 app calculates 3 types of file hashes and can evaluate if a hash matches.

This is usable, when you download a file from a webpage. Often you also receive a hash value in order to check that the downloaded file has not been tempered with.

Supported hash types:

* MD5
* SHA1
* SHA256
* SHA3_256

## Running the app
* Python3
* pip3 install PySimpleGUI

./hasher.py

## Test
The LICENSE file in this repository has the following hashes:

SHA1        e204516c6dde9caa1a77ff28cf8a880924040d7b

MD5         55a0fb9781c803bb5bdc3ad02fff2032

SHA256      273b97556cfb88148d6b498f6592a52105fcc684ccbc2fb0de6547b5d8bc6934

SHA3_256    15a8d1e24d6313e00e6aa8819469af4159d3bfbb68ef3183010b714051bd0b30

Use it as a test file.

## References

PySimpleGUI -> https://pysimplegui.readthedocs.io/en/latest/

File Hashing -> https://nitratine.net/blog/post/how-to-hash-files-in-python/

### Additional info on hashlib

https://docs.python.org/3/library/hashlib.html

## Enjoy and let me know if you like it.


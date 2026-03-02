'''
This file contains code for functions used
-Apoorva S Shekhawat
'''
import hashlib

def chunk_text(text, chunk_size = 500, overlap = 100):

    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size - overlap):
        chunks.append(" ".join(words[i:i + chunk_size]))

    return chunks

def file_hash(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()
        
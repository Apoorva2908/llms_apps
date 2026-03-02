import fitz
import os
import pickle
import faiss
import numpy as np 

from utils import chunk_text, file_hash
from table_store import extract_tables
from azure_embedder import embed_chunks

INDEX_PATH = "index/faiss.index"
META_PATH = "index/meta.pkl"
CACHE_PATH = "index/cache.pkl"

def clean_text(page):
    blocks = page.get_text("blocks")
    text_blocks = [b[4] for b in blocks if "Figure" not in b[4]]

    return "\n".join(text_blocks)

def process_pdf(pdf_path):

    pdf_id = file_hash(pdf_path)
    cache = load_cache()
    
    if pdf_id in cache:
        return cache[pdf_id]
    
    doc = fitz.open(pdf_path)

    full_text = ""
    for page in doc:
        full_text += clean_text(page)
    
    tables = extract_tables(pdf_path)
    chunks = chunk_text(full_text)
    embeddings = embed_chunks(chunks)
    cache[pdf_id] = (chunks, embeddings, tables)
    save_cache(cache)

    return chunks, embeddings, tables

def build_or_update_index(new_chunks, new_embeddings):

    new_embeddings = np.array(new_embeddings).astype("float32")
    if os.path.exists(INDEX_PATH):
        index = faiss.read_index(INDEX_PATH)
        meta = pickle.load(open(META_PATH), "rb")
    else:
        dim = new_embeddings.shape[1]
        index = faiss.IndexFlatIP(dim)
        meta = []
    
    index.add(new_embeddings)
    meta.extend(new_chunks)

    faiss.write_index(index, INDEX_PATH)
    pickle.dump(meta, open(META_PATH, "wb"))

def load_cache():
    if os.path.exists(CACHE_PATH):
        return pickle.load(open(CACHE_PATH, "rb"))
    return {}

def save_cache(cache):
    pickle.dump(cache, open(CACHE_PATH, "wb"))
'''
This script will be used to search top k candidates for the given query
-Apoorva S Shekhawat'''

import faiss
import pickle 
import numpy as np 
from azure_embedder import embed_chunks

INDEX_PATH = "index/faiss.index"
META_PATH = "index/meta.pkl"

def search(query, k = 5):
    index = faiss.read_index(INDEX_PATH)
    chunks = pickle.load(open(META_PATH, "rb"))
    q_emb = np.array(embed_chunks([query])).astype("float32")
    scores, ids = index.search(q_emb, k)
    return [chunks[i] for i in ids[0]]
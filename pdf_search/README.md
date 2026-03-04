
# 📄 Multi-PDF Research Paper Semantic Search

Semantic search over multiple research papers using **Azure OpenAI embeddings + FAISS**, built for **GitHub Codespaces**.

Upload PDFs → automatic cleaning → table extraction → chunking → embeddings → vector search.

---

## ✨ Features

* 📚 Multi-PDF ingestion
* 🧹 Figure caption removal
* 📊 Table extraction → stored as structured dictionary
* 🔁 PDF hash caching (no duplicate embedding cost)
* ⚡ Batch embedding with Azure OpenAI
* 💾 Persistent FAISS index (survives Codespaces restarts)
* 🔍 Semantic search over all papers

---

## 🏗️ Tech Stack

| Component        | Tool                                  |
| ---------------- | ------------------------------------- |
| PDF parsing      | PyMuPDF                               |
| Table extraction | Camelot                               |
| Embeddings       | Azure OpenAI `text-embedding-3-small` |
| Vector DB        | FAISS                                 |
| API              | FastAPI                               |
| Environment      | GitHub Codespaces                     |

---

# ⚙️ Codespaces Setup

## 1️⃣ Recommended machine

```
4 core / 8 GB RAM
```

This supports **hundreds of research papers** comfortably.

---

## 2️⃣ Add Codespaces Secrets

Go to:

**Repo → Settings → Codespaces → Secrets**

Add:

```
AZURE_OPENAI_API_KEY
AZURE_OPENAI_ENDPOINT
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

---

## 3️⃣ Install dependencies

```bash
pip install pymupdf camelot-py faiss-cpu fastapi uvicorn python-multipart openai numpy
```

---

# 📁 Project Structure

```
pdf_semantic_search/
│── app.py                # FastAPI entry point
│── ingestion.py         # PDF → chunks → embeddings → FAISS
│── search.py            # Semantic retrieval
│── azure_embedder.py    # Azure embedding client
│── table_store.py       # Table extraction
│── utils.py             # Chunking + PDF hashing
│
├── data/                # Uploaded PDFs
└── index/               # FAISS + cache storage
```

---

# 🚀 Running the App

Start the API:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

Run streamlit (new terminal)
streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0

In Codespaces:

➡ Open **Ports tab → click the forwarded URL**

---

# 📥 API Usage

## Upload a PDF

```
POST /upload
```

Processes the paper and adds it to the vector index.

Response:

```json
{
  "msg": "processed",
  "chunks_added": 42,
  "tables_found": 3
}
```

---

## Search

```
GET /search?q=your query
```

Example:

```
/search?q=transformer architecture training stability
```

Response:

```json
{
  "results": [
    "top matching chunk text...",
    "next relevant chunk..."
  ]
}
```

---

# 🧠 How It Works

### Ingestion pipeline

```
PDF
 → text extraction
 → figure removal
 → table extraction
 → chunking
 → Azure embedding (batched)
 → FAISS index update
 → cache by PDF hash
```

---

### Search pipeline

```
query
 → embedding
 → FAISS similarity search
 → return top-k chunks
```

---

# 💰 Cost Efficiency

Using:

```
text-embedding-3-small
```

Typical research paper:

* 30–40 chunks
* very low embedding cost

Caching ensures:

✅ Re-uploads cost = 0
✅ Instant reprocessing

---

# 🧮 Memory Behaviour (Codespaces)

Each vector ≈ **6 KB**

| Chunks | RAM used |
| ------ | -------- |
| 10k    | ~60 MB   |
| 100k   | ~600 MB  |

Safe limit on 8 GB machine:

✅ ~150k–250k chunks

---

# 📊 Table Handling

Tables are extracted with Camelot and stored as:

```python
{
  "table_0": {column → values},
  "table_1": {...}
}
```

This enables future:

* table semantic search
* structured querying
* table summarisation

---

# 🔁 Caching Strategy

Each PDF is hashed:

```
same file → no re-embedding
```

This:

* saves cost
* speeds up ingestion
* enables idempotent uploads

---

# 🧱 FAISS Index

We use:

```
IndexFlatIP
```

Why:

* works with cosine similarity
* no training required
* perfect for mid-scale research collections

Index is persisted to:

```
index/faiss.index
index/meta.pkl
```

---

# ⚠️ Common Issues

### Camelot requires system dependency

If tables fail:

```bash
apt-get install ghostscript python3-tk -y
```

---

### Azure deployment name mismatch

Your Azure model deployment name must match:

```python
MODEL = "text-embedding-3-small"
```

---

# 📌 Summary

This project gives you:

* a **cost-efficient research paper search engine**
* fully runnable in **Codespaces**
* powered by **Azure OpenAI embeddings**
* with **persistent FAISS vector storage**

---


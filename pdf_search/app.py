import os
import shutil
from fastapi import FastAPI, UploadFile

from ingestion import process_pdf, build_or_update_index
from search import search

app = FastAPI()

@app.post("/upload")
async def upload_pdf(file: UploadFile):
    path = f"data/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    chunks, embeddings, tables = process_pdf(path)

    build_or_update_index(chunks, embeddings)

    return {
        "msg": "processed",
        "chunks_added": len(chunks),
        "tables_found": len(tables)
    }

@app.get("/search")
def query(q:str):
    results = search(q)
    return {"results": results}
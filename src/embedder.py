# embedder.py

import json
import os
from dotenv import load_dotenv
from langchain_community.docstore.document import Document
from langchain.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def load_chunks_data(file_path: str) -> list[dict]:
    # Returns List of sections as dictionaries
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
    
def prepare_documents(chunks_data: list[dict]) -> list[Document]:
    # Returns Langchain compatible documents
    return [
        Document(
            page_content = f"Section {entry['section']}: {entry['section_title']}\n\n{entry['section_desc']}",
            metadata = {
                "chapter" : entry["chapter"],
                "section" : entry["section"],
                "section_title" : entry["section_title"],
                "act" : entry["act"]
            }
        )
        for entry in chunks_data
    ]

def build_vectordb():
    
    # load environment variables
    load_dotenv()
    chunks_json_path = os.getenv("CHUNKS_JSON_PATH")
    persist_dir_path = os.getenv("PERSIST_DIRECTORY_PATH")
    collection_name = os.getenv("COLLECTION_NAME")

    if not all([chunks_json_path, persist_dir_path, collection_name]):
        raise EnvironmentError("❌ Missing one or more required environment variables.")
    
    # load and process data
    chunks_data = load_chunks_data(chunks_json_path)
    documents = prepare_documents(chunks_data)

    # initialize embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # ✅ Create FAISS vectorstore and save to disk
    vectordb = FAISS.from_documents(documents, embeddings)
    vectordb.save_local(persist_dir_path)

    print(f"✅ Vectorstore successfully created in collection '{collection_name}' at '{persist_dir_path}'")

if __name__ == "__main__" :
    build_vectordb()
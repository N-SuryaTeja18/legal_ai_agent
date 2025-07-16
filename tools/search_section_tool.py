# search_section_tool.py

import os
from dotenv import load_dotenv
from crewai.tools import tool
from langchain.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

@tool("Sections Search Tool")
def search_law_sections(query: str) -> list[dict]:
    """
    Search vector database for sections relevant to the input query using MMR.

    Args:
        query (str): User query in natural language.

    Returns:
        list[dict]: List of matching sections with metadata and content.
    """
    # Load environment variables
    load_dotenv()

    # Vector DB config
    persist_dir_path = os.getenv("PERSIST_DIRECTORY_PATH")
    # collection_name = os.getenv("COLLECTION_NAME")

    if not persist_dir_path:
        raise EnvironmentError("❌ Missing 'PERSIST_DIRECTORY_PATH' in .env")

    # Load vector DB
    embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_db = FAISS.load_local(persist_dir_path, embedding_function)

    # Create MMR-based retriever
    retriever = vector_db.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 5,
            "lambda_mult": 0.5
        }
    )

    # Search with MMR
    docs = retriever.invoke(query)

    # Format results
    return [
        {
            "chapter": doc.metadata.get("chapter"),
            "section": doc.metadata.get("section"),
            "section_title": doc.metadata.get("section_title"),
            "act": doc.metadata.get("act"),
            "content": doc.page_content
        }
        for doc in docs
    ]

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from rag.pdf_loader import load_pdf

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create/Open ChromaDB
vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings,
    collection_name="pdf_collection"
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)


def load_vectorstore(pdf_path):
    global retriever

    chunks = load_pdf(pdf_path)

    # Add metadata
    for chunk in chunks:
        chunk.metadata["source"] = pdf_path

    print(f"Chunks Loaded : {len(chunks)}")

    # Add new PDF to existing database
    vectorstore.add_documents(chunks)

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    print(f"PDF Indexed Successfully : {pdf_path}")
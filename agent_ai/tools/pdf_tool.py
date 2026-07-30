from langchain_core.tools import tool
import rag.vector_store as vs


@tool
def pdf_tool(question: str) -> str:
    """
    Search the uploaded PDF and answer the user's question.
    """

    if vs.retriever is None:
        return "Please upload a PDF first."

    docs = vs.retriever.invoke(question)

    answer = ""

    for doc in docs:
        answer += doc.page_content + "\n\n"

    return answer
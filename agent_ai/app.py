import os
import streamlit as st
from supervisor import supervisor
from rag.vector_store import load_vectorstore

# ======================================
# Page Config
# ======================================
st.set_page_config(
    page_title="Agent AI",
    page_icon="🤖",
    layout="wide"
)

# ======================================
# CSS
# ======================================
st.markdown("""
<style>

.main{
    padding-top:1rem;
}

.block-container{
    padding-top:2rem;
}

[data-testid="stSidebar"]{
    background:#f8f9fa;
}

.chat-title{
    text-align:center;
    font-size:40px;
    font-weight:bold;
    color:#0E76FD;
}

.chat-sub{
    text-align:center;
    color:gray;
    margin-bottom:30px;
}

</style>
""", unsafe_allow_html=True)

# ======================================
# Session State
# ======================================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "pdf_loaded" not in st.session_state:
    st.session_state.pdf_loaded = False

# ======================================
# Sidebar
# ======================================
with st.sidebar:

    st.title("🤖 Agent AI")

    st.divider()

    st.subheader("📂 Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose PDF",
        type=["pdf"]
    )

    if uploaded_file:

        os.makedirs("pdfs", exist_ok=True)

        pdf_path = os.path.join(
            "pdfs",
            uploaded_file.name
        )

        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner("Indexing PDF..."):
            load_vectorstore(pdf_path)

        st.session_state.pdf_loaded = True
        st.success("✅ PDF Ready")

    st.divider()

    st.subheader("Status")

    if st.session_state.pdf_loaded:
        st.success("✅ PDF Loaded")
    else:
        st.warning("No PDF Uploaded")

    st.divider()

    st.subheader("Available Agents")

    st.markdown("""
🧮 Calculator Agent

📄 PDF Agent

🗄 SQL Agent

🌐 Web Agent

🌦 Weather Agent
""")

# ======================================
# Header
# ======================================
st.markdown(
    "<div class='chat-title'>🤖 Agent AI</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='chat-sub'>Multi-Agent AI Assistant powered by LangGraph</div>",
    unsafe_allow_html=True
)

# ======================================
# Chat History
# ======================================
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ======================================
# Chat Input
# ======================================
question = st.chat_input("Ask me anything...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    config = {
        "configurable": {
            "thread_id": "chat1"
        }
    }

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                # Select Agent
                selected = supervisor(question)

                # Collaboration Workflow
                if callable(selected):
                    response = selected(question, config)

                # LangGraph Agent
                else:
                    response = selected.invoke(
                        {
                            "messages": [
                                {
                                    "role": "user",
                                    "content": question
                                }
                            ]
                        },
                        config=config
                    )

                # Extract Response
                if isinstance(response, dict):

                    if "messages" in response:

                        answer = response["messages"][-1].content

                    else:

                        answer = str(response)

                else:

                    answer = str(response)

                # Convert list output to string
                if isinstance(answer, list):

                    text = ""

                    for item in answer:

                        if hasattr(item, "text"):
                            text += item.text

                        elif isinstance(item, dict):
                            text += item.get("text", "")

                        else:
                            text += str(item)

                    answer = text

            except Exception as e:

                answer = f"❌ Error:\n\n{e}"

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

# ======================================
# Footer
# ======================================
st.divider()

st.caption(
    "🚀 Powered by LangGraph • Groq • ChromaDB • MySQL • Streamlit • Multi-Agent AI"
)
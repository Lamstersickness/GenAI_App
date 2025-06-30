import os
import streamlit as st
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredPDFLoader, UnstructuredWordDocumentLoader
from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from tempfile import NamedTemporaryFile
from textwrap import wrap
import re

def show_document_qna(uploaded_files):
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
    # Load API Key
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=OPENAI_API_KEY)

    st.title("📄 Document QnA Tool")
    faiss_folder_path = "faiss_store_docs"
    main_placeholder = st.empty()
    llm = OpenAI(temperature=0.9, max_tokens=500)

    process_files_clicked = st.sidebar.button("Process Files")

    if process_files_clicked and uploaded_files:
        docs = []

        for uploaded_file in uploaded_files[:3]:  # Limit to 3 files
            suffix = "." + uploaded_file.name.split(".")[-1]
            with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                # Read and write in chunks (1MB)
                for chunk in uploaded_file.chunks() if hasattr(uploaded_file, 'chunks') else [uploaded_file.read()]:
                    tmp.write(chunk)
                tmp_path = tmp.name

            # Use appropriate loader
            if uploaded_file.name.endswith(".pdf"):
                loader = UnstructuredPDFLoader(tmp_path)
            elif uploaded_file.name.endswith(".docx"):
                loader = UnstructuredWordDocumentLoader(tmp_path)
            else:
                st.warning(f"Unsupported file type: {uploaded_file.name}")
                continue

            data = loader.load()
            docs.extend(data)

        # Split and embed
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        split_docs = text_splitter.split_documents(docs)

        embeddings = OpenAIEmbeddings()
        vectorstore_openai = FAISS.from_documents(split_docs, embeddings)
        vectorstore_openai.save_local(faiss_folder_path)
        st.success("📚 Documents processed and vectorstore saved!")

    # Query section
    query = st.text_input("Ask a question about the uploaded documents:")
    if query:
        if os.path.exists(faiss_folder_path):
            embeddings = OpenAIEmbeddings()
            vectorstore = FAISS.load_local(faiss_folder_path, embeddings, allow_dangerous_deserialization=True)

            chain = RetrievalQAWithSourcesChain.from_llm(
                llm=llm,
                retriever=vectorstore.as_retriever()
            )

            result = chain({"question": query}, return_only_outputs=True)
            answer_text = result.get("answer", "No answer found.")
            answer_text = re.sub(r"\(.*?AppData.*?\.pdf\)", "", answer_text)

            sources_text = result.get("sources", "No sources found.")
            

            wrapped_answer = "\n".join(wrap(answer_text, width=100))

            st.markdown(f"""
#### ✅ **Response**
{wrapped_answer}

---

#### 📄 **Sources**
🔗 `{sources_text}`
""")

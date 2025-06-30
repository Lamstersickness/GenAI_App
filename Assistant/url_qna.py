# Assistant/url_qna.py

import os
import time
import streamlit as st
from dotenv import load_dotenv
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def show_url_qna():
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    llm = OpenAI(api_key=OPENAI_API_KEY, temperature=0.9, max_tokens=500)

    st.markdown("Enter up to 3 news article URLs to begin.")
    urls = []
    for i in range(3):
        url = st.text_input(f"URL {i+1}")
        urls.append(url.strip())

    process_clicked = st.button("🔍 Process URLs")
    faiss_folder_path = "faiss_store_openai"

    status_placeholder = st.empty()

    if process_clicked:
        loader = UnstructuredURLLoader(urls=urls)
        status_placeholder.info("📡 Loading article content...")
        data = loader.load()

        # Split and embed
        splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n", ".", ","], chunk_size=1000)
        status_placeholder.info("🔧 Splitting text into chunks...")
        docs = splitter.split_documents(data)

        embeddings = OpenAIEmbeddings()
        vectorstore = FAISS.from_documents(docs, embeddings)
        status_placeholder.info("📦 Generating vector embeddings...")
        time.sleep(2)

        vectorstore.save_local(faiss_folder_path)
        status_placeholder.success("✅ Articles indexed!")

    query = st.text_input("Ask a question about the URLs:")
    if query and os.path.exists(faiss_folder_path):
        embeddings = OpenAIEmbeddings()
        vectorstore = FAISS.load_local(faiss_folder_path, embeddings, allow_dangerous_deserialization=True)

        chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
        result = chain({"question": query}, return_only_outputs=True)

        st.markdown("### 📘 Answer")
        st.success(result["answer"])
        st.markdown("#### 📄 Sources")
        st.code(result.get("sources", "No sources found."))

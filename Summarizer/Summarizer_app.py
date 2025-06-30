import streamlit as st
from .textsummary import summary
from .YT_summary import summarize_from_url
from .article_summarizer import summarize_article
from .file_summarizer import summarize_file

def show_summarizer_ui():
    st.subheader("🧠 AI Summarization Suite")

    # Tabs for different summarization options
    tabs = st.tabs(["📝 Text Summarizer", "📺 YouTube Summarizer", "📰 Article Summarizer", "📄 PDF/DOCX Summarizer"])

    # ---- Text Summarizer ----
    with tabs[0]:
        st.markdown("### Summarize Raw Text")
        input_text = st.text_area("Enter text to summarize:")
        if st.button("Summarize Text"):
            if input_text.strip():
                output = summary(input_text)
                st.success("✅ Summary:")
                st.write(output)
            else:
                st.warning("Please enter text.")
    
    # ---- YouTube Summarizer ----
    with tabs[1]:
        st.markdown("### Summarize YouTube Video")
        yt_url = st.text_input("YouTube URL")
        if st.button("Summarize Video"):
            if yt_url:
                result = summarize_from_url(yt_url)
                st.success("✅ Video Summary:")
                st.write(result)
            else:
                st.warning("Please enter a valid URL.")

    # ---- Article Summarizer ----
    with tabs[2]:
        st.markdown("### Summarize Web Article")
        article_url = st.text_input("Article URL")
        if st.button("Summarize Article"):
            if article_url:
                result = summarize_article(article_url)
                st.success("✅ Article Summary:")
                st.write(result)
            else:
                st.warning("Please enter a valid article URL.")

    # ---- File Summarizer ----
    with tabs[3]:
        st.markdown("### Summarize Uploaded File")
        file = st.file_uploader("Upload a PDF or DOCX file", type=["pdf", "docx"])
        if file and st.button("Summarize File"):
            result = summarize_file(file)
            st.success("✅ File Summary:")
            st.write(result)

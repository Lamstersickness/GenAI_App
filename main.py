import streamlit as st
from Summarizer.Summarizer_app import show_summarizer_ui
from Generator.generator_app import show_generator_ui
from Assistant.assistant_app import show_assistant_ui

# Set App Config
st.set_page_config(
    page_title="GenAI Multi-Modal App",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Theme Toggle
theme_mode = st.sidebar.selectbox("🎨 Select Theme", ["Light", "Dark"])

def apply_theme(mode):
    if mode == "Dark":
        st.markdown("""
        <style>
        body { background-color: #121212; color: white; }
        .stTextInput > div > div > input,
        .stTextArea > div > textarea {
            background-color: #333; color: white;
        }
        </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
        body { background-color: #f9f9f9; color: black; }
        </style>
        """, unsafe_allow_html=True)

apply_theme(theme_mode)

# ------------------- Sidebar -------------------
with st.sidebar:
    st.image("static/logo.jpg", width=150)
    
    with st.expander("ℹ️ About this App"):
        st.markdown("""
        **GenAI Multi-Modal App** combines:
        - 🧠 Summarization tools
        - 🎨 Generative AI (images, code, speech, captions)
        - 📚 LangChain-based Assistant

        Built with [Streamlit](https://streamlit.io/), [OpenAI](https://openai.com), and [HuggingFace](https://huggingface.co).
        """)

    st.markdown("---")
    st.markdown("🔗 [GitHub Repo](https://github.com)")
    st.markdown("🛠 Maintained by [Your Name](https://google.com)")

# ------------------- Main Interface -------------------
st.markdown("<h1 style='text-align: center; color:#BF40BF;'>🧠 GenAI Multi-Modal App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Your all-in-one AI app for summarization, generation, and more.</p>", unsafe_allow_html=True)

# Tabbed UI
tabs = st.tabs([
    "📝 Summarizer Tool",
    "🎨 Generator Tool",
    "📚 Assistant Tool"
])

with tabs[0]:
    show_summarizer_ui()

with tabs[1]:
    show_generator_ui()

with tabs[2]:
    show_assistant_ui()

import streamlit as st
from .image_gen import generate_image_from_text
from .text_to_speech import generate_speech
from .yt_caption_generator import caption_from_youtube_url
from .text_to_code import generate_code

def show_generator_ui():
    st.header("🚀 Content Generator Toolkit")

    tabs = st.tabs([
        "🎨 Text-to-Image",
        "🗣️ Text-to-Speech",
        "🎬 YouTube Captions",
        "💻 Text-to-Code"
    ])

    # ---- Text to Image ----
    with tabs[0]:
        st.markdown("### Generate an Image from Text")
        prompt = st.text_input("Enter image prompt")
        if st.button("Generate Image"):
            if prompt:
                image = generate_image_from_text(prompt)
                st.image(image, caption="Generated Image", use_column_width=True)
            else:
                st.warning("Please enter a prompt.")

    # ---- Text to Speech ----
    with tabs[1]:
        st.markdown("### Convert Text to Audio")
        text = st.text_area("Enter text to convert")
        voice = st.selectbox("Select a voice", ["alloy", "echo", "fable", "onyx", "nova", "shimmer"])
        if st.button("Generate Speech"):
            if text:
                audio = generate_speech(text, voice)
                st.audio(audio, format="audio/mp3")
            else:
                st.warning("Please enter text to convert.")

    # ---- YouTube Captions ----
    with tabs[2]:
        st.markdown("### Extract Captions from a YouTube Video")
        yt_url = st.text_input("YouTube Video URL")
        if st.button("Extract Captions"):
            if yt_url:
                captions = caption_from_youtube_url(yt_url)
                st.text_area("Extracted Captions", value=captions, height=300)
            else:
                st.warning("Please enter a valid YouTube URL.")

    # ---- Text to Code ----
    with tabs[3]:
        st.markdown("### Generate Code from Prompt")
        code_prompt = st.text_area("Describe what the code should do")
        if st.button("Generate Code"):
            if code_prompt:
                code = generate_code(code_prompt)
                st.code(code, language="python")
            else:
                st.warning("Please enter a prompt for code generation.")

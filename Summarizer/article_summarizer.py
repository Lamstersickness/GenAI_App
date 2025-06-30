from newspaper import Article
from transformers import pipeline
import torch
article_summary = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", torch_dtype=torch.bfloat16)

def summarize_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        text = article.text

        if not text.strip():
            return "Could not extract text from the URL."

        if len(text) > 4000:
            text = text[:4000]
        summary = article_summary(text, min_length=100, max_length=300, do_sample=False)[0]['summary_text']
        return summary
    except Exception as e:
        return f"Error summarizing article: {e}"
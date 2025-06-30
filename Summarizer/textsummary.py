import torch
from transformers import pipeline

text_summary = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", torch_dtype = torch.bfloat16)

def summary(input):
    output = text_summary(input, min_length=100, max_length=300, do_sample=False)
    return output[0]['summary_text']
import re


def summarize(text, max_sentences=3):
    sentences = re.split(r"(?<=[.?!])\s", text)
    return " ".join(sentences[:max_sentences])
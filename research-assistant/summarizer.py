from transformers import pipeline

def summarize_text(texts, model="facebook/bart-large-cnn"):
    summarizer = pipeline("summarization", model=model)
    summaries = []
    for text in texts:
        summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
        summaries.append(summary[0]['summary_text'])
    return summaries
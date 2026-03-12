from transformers import pipeline, AutoTokenizer

model_name = "t5-base"
summarizer = pipeline("summarization", model= model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def generate_summary(text: str):

    result = summarizer(text, max_length=60, min_length=20, do_sample=False)
    summary_text = result[0]["summary_text"]

    tokens = tokenizer(summary_text, return_tensors="pt")
    token_count = len(tokens["input_ids"][0])

    return summary_text, token_count


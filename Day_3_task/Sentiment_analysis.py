from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F
import os

output_dir = r"D:\Entrans_intern\Day_3_task"
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "Sentiment_analysis_report.txt")

###### Load pretrained model name
model_name = "distilbert-base-uncased-finetuned-sst-2-english"

###### Load pretrained model
model = AutoModelForSequenceClassification.from_pretrained(model_name)

###### Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

###### user input loop
while True:
    text = input("Enter a sentence  or (type 'exit' to quit): ")

    if text.lower() == "exit":
        break

    ### Converting text → tokens (convert the sentence into individual words in a list) and (assign id's for each token)
    inputs = tokenizer(text, return_tensors="pt")   # it will return the pytorch tensor like dictionary( input_ids and attention_mask)

    ### Model prediction( we will pass the dict to the model to predict the logistic values)
    outputs = model(**inputs) # it will return the model prediction which will include the logistic values

    ### Convert logits → probabilities to find out the confidence score using softmax
    probs = F.softmax(outputs.logits, dim=1)

    ### the "torch.max" will find out the max value and return its position
    confidence, predicted_class = torch.max(probs, dim=1)

    labels = ["Negative", "Positive"]

    sentiment = labels[predicted_class]

    with open(output_file, "a", encoding= "UTF8") as file:
        file.write(f"Text : {text}\nSentiment: {sentiment}\nConfidence Score: {round(confidence.item(), 2)}\n\n")
    print("Sentiment:", sentiment)
    print("Confidence Score:", round(confidence.item(), 2))
    print()


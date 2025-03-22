from transformers import pipeline

summarizer = pipeline("summarization")

text = input("Özetlemek istediğiniz metni girin: ")
summary = summarizer(text, max_length=30, min_length=10, do_sample=False)

print("Özet:", summary[0]['summary_text'])

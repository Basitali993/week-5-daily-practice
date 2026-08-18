import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

text = "This is a very useful machine learning project."

tokens = word_tokenize(text)

stop_words = set(stopwords.words("english"))

filtered_tokens = [
    word for word in tokens
    if word.lower() not in stop_words and word.isalpha()
]

print("Original Text:")
print(text)

print("\nTokens:")
print(tokens)

print("\nAfter Stopword Removal:")
print(filtered_tokens)

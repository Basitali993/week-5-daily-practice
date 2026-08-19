import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import string

# Download required NLTK resources
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

# Sample post
text = """Python is a popular programming language used for
machine learning and artificial intelligence."""

# Tokenize text
tokens = word_tokenize(text)

# Load English stopwords
stop_words = set(stopwords.words("english"))

# Remove stopwords and punctuation
clean_tokens = [
    word.lower()
    for word in tokens
    if word.lower() not in stop_words
    and word not in string.punctuation
    and word.isalpha()
]

# Count word frequency
word_frequency = Counter(clean_tokens)

# Extract top keywords
keywords = word_frequency.most_common(10)

print("Original Text:")
print(text)

print("\nClean Tokens:")
print(clean_tokens)

print("\nExtracted Keywords:")
for word, frequency in keywords:
    print(f"{word}: {frequency}")
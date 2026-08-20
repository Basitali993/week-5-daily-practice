import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Sample post
text = """
Microsoft is developing artificial intelligence tools
using Python for modern software development.
"""

# Process text with spaCy
doc = nlp(text)

print("Original Text:")
print(text)

print("\nTokens:")
for token in doc:
    print(token.text)

print("\nNouns and Proper Nouns:")
keywords = []

for token in doc:
    if token.pos_ in ["NOUN", "PROPN"]:
        keywords.append(token.text)
        print(f"{token.text} -> {token.pos_}")

print("\nExtracted Keywords:")
print(keywords)
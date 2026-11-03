import re
text = "  AI Applications Are VERY Useful!!! NLP is interesting.  "

# convert the text to lowercase
text = text.lower()
print(text)

# remove punctuation
text = re.sub(r'[^\w\s]', "", text)
print(text)

# remove extra spaces
text = re.sub(r'\s+', " ", text).strip()
print(text)

# tokenize the text
tokens = text.split()
print(tokens)

# remove 'is' and 'are' from the tokens list
stop_words = {'is', 'are'}

filtered_tokens = [word for word in tokens if word not in stop_words]
print(filtered_tokens)  
import re

text = "  AI IS AMAZING!!!    NLP: is useful.   "

text = text.lower()
# print(text)

text = re.sub(r'[^\w\s]', "", text)
# print(text)

text = re.sub(r'\s+', " ", text).strip()
# print(text)

text = 'AI makes applications intelligent.'
tokens = text.lower().replace('.','').split()
print(tokens)
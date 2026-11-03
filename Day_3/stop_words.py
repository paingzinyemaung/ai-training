text = 'the product is good and the service is fast'

stop_words = {'the', 'is', 'and'}

tokens = text.split()

print(tokens)

# List comprehension to filter out stop words
filtered_tokens = [word for word in tokens if word not in stop_words]

print(filtered_tokens)
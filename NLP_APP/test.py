text = 'The product is excellent and useful'

text = text.lower()

if 'excellent' in text or 'useful' in text:
    print('Positive')
else:
    print('Negative')
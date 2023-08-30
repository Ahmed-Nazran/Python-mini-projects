import quotes

def generate_random_quote():
    quote = quotes.random()
    return f'"{quote["text"]}" - {quote["author"]}'

print("Random Quote Generator")
print(generate_random_quote())

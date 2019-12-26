text = input('Please enter a string: ')
length = len(text)
half = int(length / 2)

print (text[:half].lower() + text[half:].upper())

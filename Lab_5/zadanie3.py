text = input()

words = text.split()

abbreviation = ''.join(word[0].upper() for word in words if len(word) >= 3)

print(abbreviation)
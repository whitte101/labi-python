import re

text = input("Введите текст: ")

sentences = re.split(r'(?<=[.!?])\s+', text.strip())

sentences = [s.strip() for s in sentences if s.strip()]

for sentence in sentences:
    print(sentence)

print(f"Предложений в тексте: {len(sentences)}")
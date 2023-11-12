text = "Python 3.9 is the latest version of Python. It's awesome!"

# Выведите 10 самых часто встречаемых слов в тексте и их количество.
# Введите ваше решение ниже.
words = {}
trans = str.maketrans({"'": " ",
                       ".": None,
                       "!": None,
                       "?": None,
                       ",": None,
                       ":": None,
                       ";": None})
edited_text = text.translate(trans).lower().split()

print(edited_text)
for word in edited_text:
    if word.isalpha():
        if not words.get(word):
            words[word] = 1
        else:
            words[word] += 1

print(sorted(words.items(), key=lambda word: word[1], reverse=True)[:10])

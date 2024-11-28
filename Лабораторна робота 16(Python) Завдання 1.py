import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
import string
import matplotlib.pyplot as plt

# Завантаження тексту із архіву Project Gutenberg
from nltk.corpus import gutenberg
nltk.download('gutenberg')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

# Завантаження тексту за варіантом
text = gutenberg.raw('carroll-alice.txt')

# Визначення кількості слів у тексті
words = word_tokenize(text)  # Токенізація тексту
word_count = len(words)
print(f"Кількість слів у тексті: {word_count}")

# Визначення 10 найбільш вживаних слів у тексті
freq_dist = FreqDist(words)
most_common_words = freq_dist.most_common(10)
print("10 найбільш вживаних слів (до очищення):")
for word, count in most_common_words:
    print(f"{word}: {count}")

# Побудова стовпчастої діаграми для 10 найпоширеніших слів
plt.figure(figsize=(10, 5))
words_labels, words_counts = zip(*most_common_words)
plt.bar(words_labels, words_counts, color='skyblue')
plt.title('10 найбільш вживаних слів (до очищення)')
plt.xlabel('Слова')
plt.ylabel('Кількість')
plt.show()

# Видалення стоп-слів та пунктуації
stop_words = set(stopwords.words('english'))
words_cleaned = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]

# Визначення 10 найбільш вживаних слів після очищення
freq_dist_cleaned = FreqDist(words_cleaned)
most_common_words_cleaned = freq_dist_cleaned.most_common(10)
print("10 найбільш вживаних слів (після очищення):")
for word, count in most_common_words_cleaned:
    print(f"{word}: {count}")

# Побудова стовпчастої діаграми для 10 найпоширеніших слів після очищення
plt.figure(figsize=(10, 5))
words_labels_cleaned, words_counts_cleaned = zip(*most_common_words_cleaned)
plt.bar(words_labels_cleaned, words_counts_cleaned, color='lightgreen')
plt.title('10 найбільш вживаних слів (після очищення)')
plt.xlabel('Слова')
plt.ylabel('Кількість')
plt.show()

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

# Завантаження необхідних ресурсів NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Імена файлів
input_file = "input_text.txt"
output_file = "output_text.txt"

# Зчитування тексту із готового файлу
with open(input_file, "r") as file:
    raw_text = file.read()

# Токенізація по словам
tokens = word_tokenize(raw_text)
print("Токенізація:", tokens)

# Лемматизація та стеммінг
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

lemmatized_words = [lemmatizer.lemmatize(word.lower()) for word in tokens if word.isalpha()]
stemmed_words = [stemmer.stem(word) for word in lemmatized_words]
print("Лемматизація:", lemmatized_words)
print("Стеммінг:", stemmed_words)

# Видалення стоп-слів
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in lemmatized_words if word not in stop_words]
print("Без стоп-слів:", filtered_words)

# Видалення пунктуації (вже враховано в `lemmatized_words`, бо фільтруємо тільки `isalpha()`)

# Запис обробленого тексту у інший файл
processed_text = " ".join(filtered_words)
with open(output_file, "w") as file:
    file.write(processed_text)

print(f"Оброблений текст збережено в файл: {output_file}")

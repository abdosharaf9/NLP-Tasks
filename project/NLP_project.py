from nltk.stem import SnowballStemmer, PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
import pandas as pd


def get_tokenize_words(text: str):
    return word_tokenize(text)


def get_tokenize_sents(text: str):
    return sent_tokenize(text)


def stem_using_snowball(word: str):
    stemmer = SnowballStemmer(language="english")
    return stemmer.stem(word)


def stem_using_porter(word: str):
    stemmer = PorterStemmer()
    return stemmer.stem(word)


def stem_words_list(words: list[str], choice: int):
    match choice:
        case 1:
            return [stem_using_porter(word) for word in words]
        case 2:
            return [stem_using_snowball(word) for word in words]


# 29355 rows
dataset = pd.read_csv("Task 2/Quote_data.csv")

# Get the first 100 quotes only
quotes = dataset.iloc[:100, 0].values

tokenized_quotes_using_words = [get_tokenize_words(quote) for quote in quotes]
tokenized_quotes_using_sents = [get_tokenize_sents(quote) for quote in quotes]
stemmed_quotes_using_porter = [stem_words_list(word, 1) for word in tokenized_quotes_using_words]
stemmed_quotes_using_snowball = [stem_words_list(word, 2) for word in tokenized_quotes_using_words]


print("Tokenize using Word Tokenization:")
print(tokenized_quotes_using_words)

print("\n\t\t========================================")

print("Tokenize using Sentance Tokenization:")
print(tokenized_quotes_using_sents)

print("\n\t\t========================================")

print("Stem using Porter Stemmer:")
print(stemmed_quotes_using_porter)

print("\n\t\t========================================")

print("Stem using Snowball Stemmer:")
print(stemmed_quotes_using_snowball)


from nltk import ngrams
from nltk.tokenize import word_tokenize

def get_n_grams(n: int, text: list[str]) -> list[any]:
    return [gram for gram in ngrams(sequence=text, n=n)]

# text = input("Enter the sentence: ")
# n = int(input("Enter the value of n: "))

# n_grams = get_n_grams(n=n, text=word_tokenize(text))
# print(n_grams)
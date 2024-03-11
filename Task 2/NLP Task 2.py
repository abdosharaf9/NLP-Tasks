from nltk.stem import SnowballStemmer, PorterStemmer
from nltk.tokenize import word_tokenize


def get_tokenize_words(text: str):
    return word_tokenize(text)


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


def get_user_input():
    print("Please enter some text:")
    text = input()
    
    while len(text) < 3:
        print("Please enter a valid text:")
        text = input()
    
    print("\nChoose one of these options:-")
    print("1) Stemming using Porter Stemmer.\n2) Stemming using Snowball Stemmer.")
    choice = int(input())
    
    while choice not in [1, 2]:
        print("Please enter a valid choice!")
        choice = int(input())
    
    return (text, choice)


if __name__ == "__main__":
    input_text, choice = get_user_input()
    tokenized_words = get_tokenize_words(input_text)
    output = stem_words_list(tokenized_words, choice)
            
    print("\n\t\t========================================")
    print(f"Your Output:-\n{output}")


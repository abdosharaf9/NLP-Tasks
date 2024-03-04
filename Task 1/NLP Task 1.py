from nltk.tokenize import *

def get_user_input():
    print("Please enter some text:")
    text = input()
    
    while len(text) < 3:
        print("Please enter a valid text:")
        text = input()
    
    print("\nChoose one of these options:-")
    print("1) Tokenized Words.\n2) Tokenized Sentences.\n3) Using \"split\" Function.")
    choice = int(input())
    
    while choice not in [1, 2, 3]:
        print("Please enter a valid choice!")
        choice = int(input())
    
    return (text, choice)


def get_tokenize_words(text: str):
    return word_tokenize(text)


def get_tokenize_sents(text: str):
    return sent_tokenize(text)


def get_splitted_text(text: str):
    return text.split()


if __name__ == "__main__":
    text, choice = get_user_input()
    
    output = ""
    match choice:
        case 1:
            output = get_tokenize_words(text)
        case 2:
            output = get_tokenize_sents(text)
        case 3:
            output = get_splitted_text(text)
    
    print("\n\t\t========================================")
    print(f"Your Output:-\n{output}")


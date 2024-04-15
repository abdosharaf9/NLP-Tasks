from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords

# POS tagging using Penn Treebank tagset
def pos_tag_penn(text):
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens, tagset='ptb')
    return tagged

# POS tagging using Universal tagset
def pos_tag_universal(text):
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens, tagset='universal')
    return tagged

# Remove stopwords before tagging
def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    return ' '.join(filtered_tokens)


if __name__ == "__main__":
    input_text = input("Enter a sentence: ")
    input_text = remove_stopwords(input_text)

    tagged_penn = pos_tag_penn(input_text)
    print("Tagged words using Penn Treebank tagset:")
    for word, tag in tagged_penn:
        print(f"{word}: {tag}")

    tagged_universal = pos_tag_universal(input_text)
    print("\nTagged words using Universal tagset:")
    for word, tag in tagged_universal:
        print(f"{word}: {tag}")

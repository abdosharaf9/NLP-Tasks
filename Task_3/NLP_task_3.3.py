from nltk.corpus import stopwords

if __name__ == "__main__":
    languages = ['english', 'spanish', 'french', 'german', 'italian', 'dutch', 'portuguese', 'russian', 'arabic', 'turkish']
    stop_words_lists = {}

    for lang in languages:
        stop_words_lists[lang] = set(stopwords.words(lang))

    # Print stop words for each language
    for lang, stop_words in stop_words_lists.items():
        print(f"Stop words in {lang.capitalize()}:")
        print(stop_words, end="\n\n")

from spacy import blank

def sent_tokenize(text, language):
    nlp = blank(language)
    
    if 'sentencizer' not in nlp.pipe_names:
        nlp.add_pipe('sentencizer')
    
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    
    return sentences


if __name__ == "__main__":
    # input_text = input("Enter input text: ")
    input_text = "L'informatique, c'est étudier les ordinateurs et les programmes. On crée des logiciels pour aider les gens à faire des choses sur leurs ordinateurs. C'est important pour beaucoup de choses comme les sites web et les jeux vidéos. L'informatique est intéressante parce qu'elle change toujours, et elle nous aide à faire plein de choses plus facilement."
    
    # language = input("Enter language code: ")
    language = "fr"
    
    sentences = sent_tokenize(input_text, language)
    print("Tokenized sentences:-")
    
    for idx, sentence in enumerate(sentences, start=1):
        print(f"[{idx}] {sentence}")

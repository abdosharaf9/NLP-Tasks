from nltk.tokenize import *

text = """
Hi! My name is Abdo Sharaf. I'm a CS student at FACI - DU. This is my graduation year.
Nice to meat you. Have a nice day! I live in Las Vegas.
"""

print(sent_tokenize(text))
print(word_tokenize(text))
print(text.split())
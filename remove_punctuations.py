import string
import re

# pass it into your corpus and see the magic
def remove_punctuations(text):
    text = text.lower()
    text = re.sub('\[.*\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)  # removes punctuation and other symbol
    text = re.sub('\n\n\n', '', text)
    text = re.sub('\n\n', '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)  # remove numbers

    return text

import string, nltk, os

""" 
Text preprocessing module.

Detection of Fake News Using Machine learning 
Bachelor's thesis
@author: Matej Koreň
@date: 2023/05/10
"""

# Looking for additional packages to be installed
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/wordnet.zip')
except LookupError:
    nltk.download('wordnet')

try:
    nltk.data.find('corpora/omw-1.4.zip')
except LookupError:
    nltk.download('omw-1.4')

try:
    nltk.data.find('corpora/stopwords.zip')
except LookupError:
    nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# slovak stopwords in package directory
sk_stopwords = os.path.join(os.path.dirname(__file__),'datasets/stopwords.txt')

def process_text(text):
    """ Custom function to tokenize, lemmatize and remove stopwords from given text. """
    
    # punctuation removing
    text = ''.join(
        [c for c in text if c not in string.punctuation and c not in string.digits])
    # tokenization
    tokens = word_tokenize(text)
    lemmatiser = WordNetLemmatizer()
    # lemmatization
    lemmatized = [lemmatiser.lemmatize(word) for word in tokens]
    
    with open(sk_stopwords, encoding='utf-8') as file:
            sw = file.readlines()
    
    sw.append(stopwords.words('english'))   # english&slovak combined

    # stop words removing
    stopped = [word for word in lemmatized if word.lower() not in sw]

    file.close()
    
    return stopped

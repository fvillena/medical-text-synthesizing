import re
import scipy.sparse
import numpy as np
def normalizer(text):
    """Receives a string, lowers the string, removes all the punctutation and 
    special characters and returns a normalized string."""
    text = text.lower() #string lowering
    text = re.sub(r'[^A-Za-zñáéíóú]', ' ', text) #replaces every punctuation with a space
    text = re.sub('á', 'a', text) #replaces special vowels to their base forms
    text = re.sub('é', 'e', text)
    text = re.sub('í', 'i', text)
    text = re.sub('ó', 'o', text)
    text = re.sub('ú', 'u', text)
    return text
def tokenizer(sentence):
    """Receives a string sentence, divides the sentence into words and returns a list of word tokens."""
    tokens = sentence.split(' ')
    tokens = [token for token in tokens if token != '']
    return tokens
class DiagnosticGenerator:
    """Class to generate a diagnostic based on a markov matrix and a vocabulary."""
    def __init__(self, markov_matrix_file, vocabulary_file):
        """Receives the location of a binary scipy sparse matrix containing the markov matrix
        and a text file containing each word of the vocabulary separated by a line break."""
        self.vocabulary = []
        with open(vocabulary_file, encoding='utf-8') as file:
            for line in file:
                word = line.rstrip()
                self.vocabulary.append(word)
        self.model = scipy.sparse.load_npz(markov_matrix_file)
    def generate(self, initial_word='<START>'):
        """Receives a initial word string to start the markov process until it reaches the <END> token
        and return a list of word tokens."""
        current_word = initial_word
        diagnostic = []
        diagnostic.append(current_word)
        while current_word != '<END>':
            index = self.vocabulary.index(current_word)
            next_words_distribution = self.model[index,:].toarray()[0]
            next_word = np.random.choice(self.vocabulary, 1, p=next_words_distribution)[0]
            current_word = next_word
            diagnostic.append(current_word)
        return diagnostic

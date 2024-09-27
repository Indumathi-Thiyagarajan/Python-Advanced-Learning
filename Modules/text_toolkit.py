import string
import os

def text_to_words(input_data):
    words_list = []
    if isinstance(input_data, str):
        if os.path.isfile(input_data):
            with open(input_data, 'r') as f:
                input_text = f.read()
        input_text = input_data

        for word in input_text.split():
            word = word.strip(string.punctuation).lower()
            words_list.append(word)
    return words_list
    
def word_freq(input_data):
    word_freq = {}
    for word in text_to_words(input_data):      
            count = 0
            word_freq[word] = count + 1 if word not in word_freq else word_freq[word] + 1
    return word_freq

def unique_words(input_data):
    return set(word_freq(input_data).keys())

def word_cooccurrence_matrix(input_data, window=2):
    """
    Create a word co-occurrence matrix with a given window size.
    """
    import numpy as np

    vocab = {}
    
    for word in text_to_words(input_data):
        if word not in vocab:
            vocab[word] = len(vocab)
            
    matrix = np.zeros((len(vocab), len(vocab)))

    for i, word in enumerate(text_to_words(input_data)):
        for j in range(max(0, i - window), min(len(text_to_words(input_data)), i + window + 1)):
            if i != j:
                matrix[vocab[word], vocab[text_to_words(input_data)[j]]] += 1

    return matrix

def text_generator(input_data):
    
    """
    A generator that yields one line of text at a time.
    """
    
    def generator():
        if isinstance(input_data, str):
            if os.path.isfile(input_data):
                with open(input_data, 'r') as f:
                    for line in f:
                        yield line.strip()
            else:
                for line in input_data.split("\n"):
                    yield line.strip()
        else:
            raise ValueError("Input must be a string representing text or a file path.")
    return list(generator())

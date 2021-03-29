#Importing all the important modules that are reuired
import pandas as pd
import numpy as np
import random
import string
#Dataset is loaded
df = pd.read_csv ('C:/Users/Hp 840/Desktop/Shakespeare_data.csv')
df.head ()
#Unnecesary lines are removed
df = df.dropna (subset = ['Player', 'ActSceneLine'])
df.tail ()
lines = df ['PlayerLine'].tolist ()
print (lines [:4])

# The length of lines generated is restricted to 20 and also to protect code from infinte loop.
Line = 20

# This is used to check the value of 2 values and if diffrence is less than this then they are consider equal.
Diff = 0.0001

# This mark the end of string.
End1 = 'endl'

# white-spaces and punctuations from a line are removed  and converted into a list of tokens
def token (line):
    base = line.strip ().lower ()
    tokens = ''.join ([x for x in base if x not in string.punctuation]).split ()
    return tokens

# apiring is added to dictionery
def paired (dictionary, key, value, debug = False):
    if key not in dictionary:
        dictionary [key] = []
    if debug: print (key, dictionary [key])
    dictionary [key].append (value)

# Convert list to probability values
def probability_convertion (chain):
    frequency = {}
    probability = {}
    num_of_words = len (chain)

    for word in chain:
        frequency [word] = frequencies.get (word, 0) + 1

    for word, freq in frequency.items ():
        probability [word] = round (float (freq) / num_of_words, 3)

    return probability

#main function for buliding markav model and model is built here.

def markov_model_built (corpus, first_order_markov_chain, second_order_markov_chain):
    # This is a dictionary of words which are used to start a line in Shakespeare's plays
    words = []

    for line in corpus:
        tokens = token (line)
        num_of_tokens = len (tokens)

        for idx in range (num_of_tokens):
            token = tokens [idx]

            if idx == 0:
                words.append (token)

                # First word of line is of no use.
                continue

            # first-order markov chain
            last = tokens [idx - 1]
            paired (first_order_markov_chain, last, token)

            # The second word in a line can only have a first-level
            # markov chain since there is only a single word before it
            if idx == 1:
                continue

            # Chaining last word of line with end so that t can be used during Predicition
            if idx == num_of_tokens - 1:
                paired (second_order_markov_chain, (last, token), END_TOKEN)

            # second-order markov chain
            second_last_token = tokens [idx - 2]
            paired (second_order_markov_chain, (second_last_token), token)

    # Converting first-order markov chain to probability values
    for word, chain in first_order_markov_chain.items ():
        first_order_markov_chain [word] = probability_convertion (chain)

    # Converting second-order markov chain to probability values
    for pair, chain in second_order_markov_chain.items ():
        second_order_markov_chain [pair] = probability_convertion (chain)

    print ('Successfully built Markov Model!\n')
    return list (set (words))


# Helpers Functions for using the Markov Model for Text-Generation from the Corpus

# Picking up word with highest probablity from second order markov chain and if two words have same probablity than randomly select.
def next_word_prediction (key, dictionary, debug = False):
    max_prob = 0.0
    most_used_words = []

    for next_word, probability in dictionary.items ():
        if probability > max_prob:
            max_prob = probability
            most_used_words = [next_word]
        elif max_prob - probability < Diff:
            most_used_words.append (next_word)

    if debug: print (key, most_used_words)
    return random.choice (most_used_words)

# Randomly picking word ferom first order.
def next_word_picked (key, dictionary, debug = False):
    if debug: print (dictionary)
    return random.choice (dictionary.keys ())

# Generating  text based on corpus
def text_generated (first_word, markov_chain_one, markov_chain_two):
    line = []
    word = first_word.lower ()

    if word not in markov_chain_one.keys ():
        return 0

    line.append (word)
    next_word = pick_next_word (first_word, markov_chain_one [first_word])
    line.append (next_word)

    n = 0
    while n < Line:
        nextto_next_word = next_word_prediciton ((word, next_word), markov_chain_two [(word, next_word)])

        if next_word2 == END_TOKEN:
            return ' '.join (line)

        word = next_word
        next_word = next_word2
        line.append (next_word2)
        n += 1

# Writing play of given length.
def play (hints, markovchain1, markovchain2):
    for word in hints:
        line = write_line (word, markovchain1, markovchain2)

        if (line): print (line)

##################################################################
#Prediction
# Last words from seriesis used to lookup.
def predict (sequence, markovvhain1, markovchain2):
    # Sanity checks
    sequence = sequence.strip ()
    if (sequence == ""):
        raise ValueError( 'Sequence is empty')

    tokens = token (sequence)
    line = ''
    for token in reversed (tokens):
        line = text_generated (token, markovchain1, markovchain2)

        if line:
            break

    return line




#Its a pre bulits first order markov chain. It chains a word with the word(s) that can come after it
markovchain_1 = {}

# Its a pre bulits second order markov chain. It chains a pair of words with word(s) that can follow it
markovchain_2 = {}

#Looking in both first and second order chain.

words = markov_model_built(lines, markovchain_1, markovchain_2)


play_length = 20
hints = [random.choice (words) for x in range (play_length)]
play (hints, markovchain_1, markovchain_2)

predict('Lead us from hence', markovchain_1, markovchain_2)

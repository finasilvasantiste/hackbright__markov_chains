"""Generate Markov text from text files."""

from random import choice
from random import randrange


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path).read()

    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
        

    chains = {}
    
    text_list = text_string.split()
    # return "Works!"

    for index in range(len(text_list)-2):
        key = (text_list[index], text_list[index+1])
        next_word = text_list[index+2]

        if chains.get(key, False) == False: # Key is not in dictionary
            value_list = []
            value_list.append(next_word)
            chains[key] = value_list
        else:
            key_value_list = chains[key] # Key is already in dictionary
            key_value_list.append(next_word)
            chains[key] = key_value_list


    # print(chains)

    return chains


def make_text(chains):
    """Return text from chains."""

    sentence = []


    # your code goes here
    for key in chains:
        subsentence =[]
        # subsentence = str(key) + chains[key][0]
        # sentence.append(key[0])
        # sentence.append(key[1])
        # sentence.append(chains[key][0])
        subsentence.append(key[0])
        subsentence.append(key[1])
        subsentence.append(chains[key][0])
        #print(subsentence)
        sentence.extend(subsentence)

    # print(sentence)
    # print(" ".join(sentence))
    return " ".join(sentence)


input_path = "green-eggs.txt"

# 1. Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# 2. Get a Markov chain
chains = make_chains(input_text)

# 3. Produce random text
random_text = make_text(chains)

# print(random_text)chains = make_chains(input_text)

# 3. Produce random text

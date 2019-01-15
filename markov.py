"""Generate Markov text from text files."""

from random import choice


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
    

    # def create_value_list():
    #     return "Works!"

    for index in range(len(text_list)-2):
        #chains[(text_list[index], text_list[index+1])] = text_list[index+2]
        key = (text_list[index], text_list[index+1])
        next_word = text_list[index+2]
        # chains[key] = chains.get(key, create_value_list())

        if chains.get(key, False) == False: # Key is not in dictionary
            # print("If")
            value_list = []
            value_list.append(next_word)
            chains[key] = value_list
        else:
            # print("ELSE")
            # chains[key]
            key_value_list = chains[key]
            key_value_list.append(next_word)
            chains[key] = key_value_list


    # key = ("Would", "you")


    print(chains)
    # return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

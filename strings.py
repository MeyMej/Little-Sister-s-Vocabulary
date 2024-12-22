"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return "un" + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.
    """
    prefix = vocab_words[0]  
    words_with_prefix = [prefix] 
    for word in vocab_words[1:]:  
        words_with_prefix.append(prefix + word)
    
    return " :: ".join(words_with_prefix)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """        
    if word.endswith("ness"):
        word_without_suffix = word[:-4]
        
        if word_without_suffix.endswith("i"):
            return word_without_suffix[:-1] + "y"
        
        return word_without_suffix
    
    return word 


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    words = sentence.split()

    adjective = words[index]

    adjective = adjective.rstrip('.,!?')

    return adjective + "en" 
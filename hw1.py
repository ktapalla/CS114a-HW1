from collections import Counter, defaultdict

from typing import Iterable, TypeVar, Sequence

# DO NOT MODIFY
T = TypeVar("T")

# DO NOT MODIFY
START_TOKEN = "<start>"
# DO NOT MODIFY
END_TOKEN = "<end>"


def counts_to_probs(counts: Counter[T]) -> defaultdict[T, float]:
    """Return a defaultdict with the input counts converted to probabilities."""
    prob_dict = defaultdict(list)
    #generates total sum of all keys/tokens
    sum = 0
    for val in counts.values():
       sum += val
    #calculates probability of each and enters it into the dictionary
    for key, val in counts.items():
        prob = val/sum
        prob_dict.update({key : prob})
    return prob_dict


def bigrams(sentence: Sequence[str]) -> list[tuple[str, str]]:
    """Return the bigrams contained in a sequence."""
    tpl_list = list()
    sentence = list(sentence)
    sentence.insert(0, START_TOKEN)
    sentence.insert(len(sentence), END_TOKEN)
    for ind in range(len(sentence)-1):
        tpl_list.append(tuple([sentence[ind], sentence[ind+1]]))
    return tpl_list


def trigrams(sentence: Sequence[str]) -> list[tuple[str, str, str]]:
    """Return the trigrams contained in a sequence."""
    tpl_list = list()
    sentence = list(sentence)
    sentence.insert(0, START_TOKEN)
    sentence.insert(0, START_TOKEN)
    sentence.insert(len(sentence), END_TOKEN)
    sentence.insert(len(sentence), END_TOKEN)
    for ind in range(len(sentence)-2):
        tpl_list.append(tuple([sentence[ind], sentence[ind + 1], sentence[ind + 2]]))
    return tpl_list


def count_unigrams(sentences: Iterable[list[str]], lower: bool = False) -> Counter[str]:
    """Count the unigrams in an iterable of sentences, optionally lowercasing."""
    counter = Counter()
    if lower == False:
        # enters tokens into counter to be updated
        for token in sentences:
            counter.update(token)
    # makes all words in sentence lowercase and enters lowercase words to counter
    else:
        lowercase_token = list()
        for token in sentences:
            for words in token:
                lowercase_token.append(words.lower())
        counter.update(lowercase_token)
    return counter


def count_bigrams(sentences: Iterable[list[str]], lower: bool = False) -> Counter[tuple[str, str]]:
    """Count the bigrams in an iterable of sentences, optionally lowercasing."""
    counter = Counter()
    # makes sentences bigrams and enters bigrams into counter to be updated
    if lower == False:
        for token in sentences:
            bigram_tokens = bigrams(token)
            counter.update(bigram_tokens)
    # makes sentences lowercase and converts to bigrams then enters bigrams into counter to be updated
    else:
        for token in sentences:
            lowercase_token = list()
            for words in token:
                lowercase_token.append(words.lower())
            bigram_tokens = bigrams(lowercase_token)
            counter.update(bigram_tokens)
    return counter


def count_trigrams(sentences: Iterable[list[str]], lower: bool = False) -> Counter[tuple[str, str, str]]:
    """Count the trigrams in an iterable of sentences, optionally lowercasing."""
    counter = Counter()
    # makes sentences trigrams and enters trigrams into counter to be updated
    if lower == False:
        for token in sentences:
            trigram_tokens = trigrams(token)
            counter.update(trigram_tokens)
    # makes sentences lowercase and converts to trigrams then enters trigrams into counter to be updated
    else:
        for token in sentences:
            lowercase_token = list()
            for words in token:
                lowercase_token.append(words.lower())
            trigram_tokens = trigrams(lowercase_token)
            counter.update(trigram_tokens)
    return counter

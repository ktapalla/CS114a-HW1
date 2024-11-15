# README - COSI 114a HW1

The code provided in this repository contains the solutions to HW1 for COSI 114a - Fundamentals of Natural Language Processing I. The purpose of this assignment was to use ``` Counter ``` and ``` defaultdict ``` classes to implement counters and probability distribution, and to implement functions that extract and count n-grams. As this assignment was done for a class, some helper files and testing files were provided. All student-written solutions to the assignment were written in the ``` hw1.py ``` file. 

## Installation and Execution 

Get the files from GitHub and in your terminal/console move into the project folder. To run the test file included with the files given to students, run the following: 

``` bash 
python test_hw1.py 
```

Doing this will run the set of tests in the test file that was provided to students to test their code. Running the test file will print a score to the user's console indicating the success of the program for each given test case. 

Note: I've added some additional tests to the original file provided in order to correct old bugs/mistakes. The original submission of this assignment resulted in IndexErrors for bigram and trigram tests that consisted of shorter sentences. The added test cases are the following: 

1. ``` test_bigrams2 ```
2. ``` test_bigrams_short1 ```
3. ``` test_trigrams2 ```
4. ``` test_trigrams_short1 ```
5. ``` test_trigrams_short2 ```


## Assignment Description 

### Normalizing Counts 

The function ``` counts_to_probs(counts: Counter[T]) -> defaultdict[T, float] ``` takes a ``` Counter ``` as an argument and returns a ``` defaultdict ``` with the same keys, but with values transformed from counts to probabilities. The following is assumed: 

1. All values in the input counter are non-negative integers, and at least one value is greater than zero (this the total of the counts is greater than zero). 
2. The input counter is not empty. 

### Creating N-Grams 

The following two functions have been written: 

1. ``` bigrams(sentence: Sequence[str]) -> list[tuple[str, str]] ``` 
2. ``` trigrams(sentence: Sequence[str]) -> list[tuple[str, str, str]] ```

Each of these takes a sentence (a sequence of strings, each a token) as input and returns a list of the n-grams in the sentence. Each n-gram is represented as a tuple of strings and the n-grams are created by iterating over the input sequence. 

When creating the n-grams, the sentence is padded so that the first and last n-gram are filled with the values of ``` START_TOKEN ``` and ``` END_TOKEN ``` provided (``` <start> ``` and ``` <end> ```). The general idea is that for an n-gram of order n, a padding of the size n-1 is needed. If ``` sentence ``` is of a shorter variation, it is possible for ``` START_TOKEN ``` and ``` END_TOKEN ``` to appear in the same n-gram. 

### Counting N-Grams 

The following three functions have been written: 

1. ``` count_unigrams(sentences: Iterable[Sequence[str]], lower: bool = False) -> Counter[str] ``` 
2. ``` count_bigrams(sentences: Iterable[Sequence[str]], lower: bool = False) -> Counter[tuple[str, str]] ``` 
3. ``` trigrams(sentences: Iterable[Sequence[str]], lower: bool = False) -> Counter[tuple[str, str, str]] ```

Each function takes an iterable (not necessarily a list or tuple, could be a generator, etc.) of sentences, where each sentence is a sequence of string tokens, and returns a ``` Counter ``` over the n-grams contained in those sentences. If the ``` lower ``` argument is set to ``` True ```, then the sentence is lowercased before the n-grams are extracted, but in these cases a lowercase copy is made of the input sentences and the original input isn't modified. 

The implementations for ``` count_bigrams ``` and ``` count_trigrams ``` call on the ``` bigrams ``` and ``` trigrams ``` functions in order to create the n-grams. It is assumed that both the iterable and input sentences are non-empty. 
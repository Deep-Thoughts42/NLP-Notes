# N-gram Language Models (3)
## Table of Contents
- [N-gram Language Models (3)](#n-gram-language-models-3)
  - [Table of Contents](#table-of-contents)
  - [N-grams (3.1)](#n-grams-31)

--- 

The idea of assigning probabilities for a next word to show up in a text, or the likelihood of a sentence apeparing in a text can be valuable pieces of information in NLP applications. Speech recognition and spelling correction are two examples. 

Models that assign probabilities to sequences of words are called `language models` or `LMs`. The simplest model that assigns these probabilities is called the `n-gram`.

An n-gram is a sequence of *n* words, and n-gram models can be used to estimate the probability of the last word of an n-gram given the previous words. 

## N-grams (3.1)
# BPE Tokenizer and Vocabulary Learner

This project consists of two main components: a vocabulary learner and a tokenizer, both utilizing the Byte Pair Encoding (BPE) algorithm. The learner generates a vocabulary from training text files, and the tokenizer uses this vocabulary to tokenize new text files.

## Components

### Vocabulary Learner (`bpe_learn.py`)
- **Input:** Training text file(s).
- **Output:** A vocabulary file saved as `vocab.pickle` using Python's `pickle` module.

### Tokenizer (`bpe_tokenizer.py`)
- **Input:** Text file(s) to be tokenized.
- **Output:** Tokenized text files with the extension `.bpe`.

## How to Run

### Vocabulary Learner
To generate the vocabulary, run the following command:
```
$ ./bpe_learn.py trn/.tok
```
This will create a `vocab.pickle` file in the current directory.

### Tokenizer
To tokenize text files using the generated vocabulary, run:
```
$ ./bpe_tokenizer.py test/.tok
```
This will produce `.tok.bpe` files as output.

## Vocabulary Learner Workflow
1. For each input file, convert each word into a tuple of individual character tokens and their frequency, storing them in a corpus (dictionary of tuples).
   - Example: `'great'` becomes `{('g', 'r', 'e', 'a', 't', '_'): frequency, ...}`
2. Calculate the frequency of adjacent token pairs in the corpus.
3. Add the most frequent token pair to the vocabulary (list).
4. Update the corpus with this token pair.
5. Stop learning if no changes occur or if the highest frequency token pair has a frequency of 1.
6. Save the vocabulary as `vocab.pickle`.

## Tokenizer Workflow
1. For each input file, decompose each word into individual characters.
   - Example: `'great'` becomes `['g', 'r', 'e', 'a', 't', '_']`
2. Sequentially check each token pair in the vocabulary and merge them in the token list if found.
   - Example transformation:
     - `['g', 'r', 'e', 'a', 't_']`
     - `['g', 're', 'a', 't_']`
     - `['g', 're', 'at_']`
     - `['gre', 'at_']`
     - `['great_']`
3. Remove the underscore (`_`) from the token.
4. Join the tokens into a string separated by `+`.
   - Example: `great`, `inter+changeable`
5. Save the output in the format: `<original token>\t<bpe segmented tokens>`

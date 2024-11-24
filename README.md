# Korean Corpus Analysis

This repository contains a series of assignments focused on processing and analyzing Korean text corpora. Each assignment builds upon the previous one, culminating in a comprehensive toolkit for tasks such as morphological analysis, word frequency extraction, and vector-based similarity analysis.

## Repository Structure

- **HW1: BPE Tokenizer and Vocabulary Learner**
  - **Scripts:**
    - `bpe_learn.py`: Generates a vocabulary using the Byte Pair Encoding (BPE) algorithm.
    - `bpe_tokenizer.py`: Tokenizes text files using the generated vocabulary.
  - **Description:** See [HW1.md](HW1.md) for detailed instructions and usage.

- **HW2: Morphological Analysis for Korean Corpus**
  - **Scripts:**
    - `trn.txt`: Training corpus for morphological analysis.
  - **Description:** See [HW2.md](HW2.md) for detailed instructions and usage.

- **HW3: Hanja to Hangeul Conversion Tool**
  - **Scripts:**
    - `hanja2hangeul_table.py`: Generates a Hanja-Hangeul conversion table.
    - `hanja2hangeul.py`: Converts Hanja to Hangeul using the generated table.
  - **Description:** See [HW3.md](HW3.md) for detailed instructions and usage.

- **HW4: Morphological Analysis and Context Extraction Scripts**
  - **Scripts:**
    - `get_morphs_tags.py`: Extracts morphemes and POS tags.
    - `tagged2context.py`: Extracts index terms and generates context files.
  - **Description:** See [HW4.md](HW4.md) for detailed instructions and usage.

- **HW5: Word Frequency by Year**
  - **Scripts:**
    - `word_frequency_by_year.py`: Extracts word frequencies from yearly context files.
  - **Description:** See [HW5.md](HW5.md) for detailed instructions and usage.

- **HW6: Co-Word Frequency and T-Score Calculation**
  - **Scripts:**
    - `coword_frequency.py`: Generates word frequency, co-word frequency, and context size files.
    - `calc_co-oc_tscore.py`: Calculates t-scores for co-words.
  - **Description:** See [HW6.md](HW6.md) for detailed instructions and usage.

- **HW7: Co-Word Vector Indexing and Similarity**
  - **Scripts:**
    - `coword_vector_indexer.py`: Creates word vectors from t-score files.
    - `coword_vector_similarity.py`: Finds and displays the most similar words to a given query.
  - **Description:** See [HW7.md](HW7.md) for detailed instructions and usage.

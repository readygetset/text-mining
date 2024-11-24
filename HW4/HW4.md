# Morphological Analysis and Context Extraction Scripts

This project involves creating two scripts: one for extracting morphemes and part-of-speech (POS) tags from a morphological analysis file, and another for extracting index terms to generate context files.

## Scripts

### 1. `get_morphs_tags.py`
- **Purpose:** Extracts all morphemes and their corresponding POS tags from a given morphological analysis file.
- **Function:** `get_morphs_tags`
- **Usage:**
  ```bash
  $ ./get_morphs_tags.py input_file > output_file
  ```
  - Example: 
    ```bash
    $ ./get_morphs_tags.py all > all.mt
    ```

### 2. `tagged2context.py`
- **Purpose:** Extracts index terms from a given morphological analysis file and generates a context file.
- **Function:** `get_index_terms`
- **Usage:**
  ```bash
  $ ./tagged2context.py input_file(s)
  ```
  - Example:
    ```bash
    $ ./tagged2context.py *.tag
    ```
  - Output files are generated as `input_file.context` for each input file.

## Considerations

### Extracting Morphemes and POS Tags
- Handle cases where the characters '+' or '/' appear within a word segment.

### Extracting Index Terms
- **Indexable POS Tags:** 
  - NNG (Common Noun), NNP (Proper Noun), NR (Numeral), NNB (Dependent Noun), SL (Foreign Language; English), SH (Hanja), SN (Number).
- **Index Terms:**
  - Extract both single and compound terms.
  - Compound terms are combinations of consecutive indexable morphemes within the same word segment.
  - If both single and compound terms appear in the same word segment, list single terms first, followed by compound terms.
  - For sequences of three or more single terms, only extract the longest compound term.
    - Example: `정부/NNG+조직/NNG+개편/NNG` -> `정부`, `조직`, `개편`, `정부조직개편`
  - Extract NNG, NNP, SH, SL as single index terms (except when SL is part of a compound term).
  - Do not extract NR, NNB, SN as single index terms.

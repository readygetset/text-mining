# Co-Word Vector Indexing and Similarity

This project involves creating scripts to generate word vectors from t-score files and to find the most similar words to a given query using these vectors.

## Scripts

### 1. `coword_vector_indexer.py`
- **Purpose:** Generates word vectors (co-word vectors) from a t-score file and saves them as a dictionary of dictionaries in a pickle file.
- **Usage:**
  ```bash
  $ ./coword_vector_indexer.py input_file output_file
  ```
  - Example:
    ```bash
    $ ./coword_vector_indexer.py all.tscore all.pickle
    ```

- **Output File:**
  - The output is a pickle file containing a dictionary of dictionaries representing word vectors.

### 2. `coword_vector_similarity.py`
- **Purpose:** Displays the 30 most similar words (related words) and their similarity scores to a user query.
- **Usage:**
  ```bash
  $ ./coword_vector_similarity.py input_file
  ```
  - Example:
    ```bash
    $ ./coword_vector_similarity.py all.pickle
    ```

- **Input File:**
  - The input is a pickle file containing word vectors (co-word vectors).

- **Constraints:**
  - Related word candidates are limited to the target word's co-words and the co-words of those co-words.
  - Only save candidates with a cosine similarity greater than 0.001.
  - Do not output candidates that are the same as the target word.
  - Do not output candidates that are contained within the target word (e.g., exclude "개인정보/정보 *", "교육부장관/장관 *", "인사청문회/청문회 *").
  - Output the top 30 related words in descending order of similarity.

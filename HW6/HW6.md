# Co-Word Frequency and T-Score Calculation

This project involves creating scripts to generate word frequency, co-word frequency, and context size files from yearly context files, and to calculate t-scores for co-words.

## Scripts

### 1. `coword_frequency.py`
- **Purpose:** Generates yearly `.1gram`, `.2gram`, and `.1gram_context` files from context files.
- **Usage:**
  ```bash
  $ ./coword_frequency.py input_file(s)
  ```
  - Example:
    ```bash
    $ ./coword_frequency.py *.context
    ```

- **Output Files:**
  - **`.1gram` and `.1gram_context` Format:**
    ```
    word\tfrequency
    ```
    - The first line of `.1gram` should include the frequency for `#Total`.
  - **`.2gram` Format:**
    ```
    target_word\tco_word\tfrequency
    ```

- **Considerations:**
  - Words appearing more than once in the same context are counted once (use a set for deduplication).
  - Target and co-word pairs are output once based on string sorting (e.g., output "A B frequency" but not "B A frequency").
  - All output files should be sorted based on string order.

### 2. `calc_co-oc_tscore.py`
- **Purpose:** Calculates co-word t-scores from `.1gram`, `.2gram`, and `.1gram_context` files.
- **Usage:**
  ```bash
  $ ./calc_co-oc_tscore.py
  ```

- **Output Files:**
  - **`.tscore` Format:**
    ```
    target_word\tco_word\tt-score
    ```

- **Constraints:**
  - Only output t-scores that are positive.
  - Calculate t-scores only for co-word frequencies that are greater than or equal to the CUTOFF (5).
  - Exclude cases where the target word includes the co-word (e.g., exclude "개인정보/정보 *", "교육부장관/장관 *", "인사청문회/청문회 *").
  - All output files should be sorted based on string order.

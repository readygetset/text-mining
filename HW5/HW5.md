# Word Frequency by Year

This script extracts word frequencies from context files for each year and outputs the results in a specified format.

## Script

### `word_frequency_by_year.py`
- **Purpose:** Extracts word frequencies from yearly context files and compiles them into a single output.
- **Usage:**
  ```bash
  $ ./word_frequency_by_year.py input_file(s) > output_file
  ```
  - Example:
    ```bash
    $ ./word_frequency_by_year.py *.context > result.txt
    ```

## Output Format

- The output is formatted as follows:
  ```
  word\tfrequency_list
  ```
  - Each line contains a word followed by a tab-separated list of frequencies corresponding to each year.

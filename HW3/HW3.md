# Hanja to Hangeul Conversion Tool

This project involves creating a conversion tool that translates Hanja characters to Hangeul using a predefined table. The table is generated from an Excel file provided in the 6th-week lecture materials.

## Components

### Hanja-Hangeul Table
- **File:** `hanja2hangeul_table.py`
- Generated from the "검색엔진용한자음가사전" Excel file.

### Conversion Program
- **File:** `hanja2hangeul.py`
- This script performs the conversion of input files based on specified options.

## How to Run

To execute the conversion, use the following command format:
```
$ ./hanja2hangeul.py [option] input_file(s)
```

- The output file will be saved as `input_file.out`.

### Options

- **`-h1`**: Convert Hanja to Hangeul
  ```bash
  $ ./hanja2hangeul.py -h1 sample.txt
  ```

- **`-h2`**: Convert Hanja to Hangeul (Hanja)
  ```bash
  $ ./hanja2hangeul.py -h2 sample.txt
  ```

- **`-h3`**: Convert Hanja to Hanja (Hangeul)
  ```bash
  $ ./hanja2hangeul.py -h3 sample.txt
  ```

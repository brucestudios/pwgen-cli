# CSV Toolkit

A Python command-line toolkit for performing common operations on CSV files.

## Features

- Read CSV files and display contents
- Write data to CSV files (basic)
- Filter rows based on a condition (placeholder for extension)
- Convert CSV delimiter from one format to another

## Installation

```bash
pip install csv-toolkit
```

## Usage

### Read a CSV file

```bash
csv-tool read data.csv
```

Specify a different delimiter:

```bash
csv-tool read data.csv -d ';'
```

If the CSV does not have a header:

```bash
csv-tool read data.csv --no-header
```

### Convert CSV delimiter

Convert a CSV from comma-delimited to semicolon-delimited:

```bash
csv-tool convert input.csv output.csv -i ',' -o ';'
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Bruce Fang (henshao.fang@outlook.com)
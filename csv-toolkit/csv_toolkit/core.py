import csv
from typing import List, Dict, Any, Optional

def read_csv(file_path: str, delimiter: str = ',', has_header: bool = True) -> List[Dict[str, Any]]:
    """
    Read a CSV file and return a list of dictionaries.
    
    Args:
        file_path: Path to the CSV file.
        delimiter: Delimiter used in the CSV (default: ',').
        has_header: Whether the CSV has a header row (default: True).
    
    Returns:
        List of dictionaries representing the rows.
    """
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        if has_header:
            reader = csv.DictReader(csvfile, delimiter=delimiter)
        else:
            # If no header, we'll generate keys as column0, column1, etc.
            reader = csv.reader(csvfile, delimiter=delimiter)
            rows = list(reader)
            if not rows:
                return []
            # Generate headers
            headers = [f'column{i}' for i in range(len(rows[0]))]
            # Create dictionaries
            reader = (dict(zip(headers, row)) for row in rows)
        return list(reader)

def write_csv(data: List[Dict[str, Any]], file_path: str, delimiter: str = ',', 
              header: Optional[List[str]] = None) -> None:
    """
    Write a list of dictionaries to a CSV file.
    
    Args:
        data: List of dictionaries to write.
        file_path: Path to the output CSV file.
        delimiter: Delimiter to use (default: ',').
        header: List of column names. If None, uses keys from the first dict.
    """
    if not data:
        # If no data, write an empty file or just header if provided
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            if header:
                writer = csv.writer(csvfile, delimiter=delimiter)
                writer.writerow(header)
        return

    if header is None:
        header = list(data[0].keys())
    
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header, delimiter=delimiter)
        writer.writeheader()
        writer.writerows(data)

def filter_csv(data: List[Dict[str, Any]], condition: callable) -> List[Dict[str, Any]]:
    """
    Filter rows in the CSV data based on a condition.
    
    Args:
        data: List of dictionaries (CSV rows).
        condition: A function that takes a row (dict) and returns True/False.
    
    Returns:
        Filtered list of dictionaries.
    """
    return [row for row in data if condition(row)]

def convert_csv_delimiter(input_path: str, output_path: str, 
                          input_delimiter: str = ',', output_delimiter: str = ',') -> None:
    """
    Convert a CSV file from one delimiter to another.
    
    Args:
        input_path: Path to the input CSV.
        output_path: Path to the output CSV.
        input_delimiter: Delimiter of the input CSV.
        output_delimiter: Delimiter for the output CSV.
    """
    data = read_csv(input_path, delimiter=input_delimiter)
    write_csv(data, output_path, delimiter=output_delimiter)
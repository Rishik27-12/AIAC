def analyze_csv_file(file_path):
    """
    Opens a CSV file and returns:
    - Number of rows
    - Number of empty rows
    - Number of words in the file
    
    Returns:
        tuple: (total_rows, empty_rows, word_count)
    """
    import csv
    
    total_rows = 0
    empty_rows = 0
    word_count = 0
    
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                total_rows += 1
                # Check if row is empty (all cells are empty or whitespace)
                if all(cell.strip() == '' for cell in row):
                    empty_rows += 1
                # Count words in all cells of the row
                for cell in row:
                    word_count += len(cell.strip().split())
        
        return total_rows, empty_rows, word_count
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

# Example usage and testing
if __name__ == "__main__":
    # Test with a sample CSV file
    file_path = "SRU.csv.txt"  # Using the file in your workspace
    
    result = analyze_csv_file(file_path)
    if result:
        total_rows, empty_rows, word_count = result
        print(f"Total rows: {total_rows}")
        print(f"Empty rows: {empty_rows}")
        print(f"Total words: {word_count}")
        
        # Example output format as requested
        print(f"\nExample: File has {total_rows} rows with {empty_rows} empty row(s) and {word_count} words in total.")

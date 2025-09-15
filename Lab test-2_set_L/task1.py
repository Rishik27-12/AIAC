import re
import tempfile
import os

def extract_valid_emails_from_log(filepath):
    """
    Reads a log file line by line, extracts valid email addresses using regex,
    and returns a unique sorted list of emails.
    """
    # Reliable regex for most real-world emails
    email_regex = re.compile(
        r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    )
    emails = set()
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                found = email_regex.findall(line)
                emails.update(found)
    except FileNotFoundError:
        return []
    return sorted(emails)


# --- Test Cases ---

def test_extract_valid_emails_from_log():
    sample_log = """Support ticket: user1@example.com
Invalid: user@@example.com
Contact: admin@shop.com, helpdesk@shop.com
"""
    expected = ["admin@shop.com", "helpdesk@shop.com", "user1@example.com"]

    # Test with sample log file
    with tempfile.NamedTemporaryFile('w+', delete=False) as tmp:
        tmp.write(sample_log)
        tmp.flush()
        result = extract_valid_emails_from_log(tmp.name)
        assert result == expected, f"Expected {expected}, got {result}"
    
    os.unlink(tmp.name)

    # Test with empty file
    with tempfile.NamedTemporaryFile('w+', delete=False) as tmp:
        tmp.flush()
        result = extract_valid_emails_from_log(tmp.name)
        assert result == [], f"Expected empty list, got {result}"
    
    os.unlink(tmp.name)

    # Test with missing file
    result = extract_valid_emails_from_log("nonexistent.log")
    assert result == [], f"Expected empty list, got {result}"


if __name__ == "__main__":
    test_extract_valid_emails_from_log()
    print("All tests passed.")

    # --- Demo run with sample input ---
    sample_log = """Support ticket: user1@example.com
Invalid: user@@example.com
Contact: admin@shop.com, helpdesk@shop.com
"""
    with tempfile.NamedTemporaryFile('w+', delete=False) as tmp:
        tmp.write(sample_log)
        tmp.flush()
        output = extract_valid_emails_from_log(tmp.name)
    
    os.unlink(tmp.name)

    print("Sample Output:")
    # Format the result to match the exact format requested
    formatted_output = "[" + ", ".join(f'"{email}"' for email in output) + "]"
    print(formatted_output)

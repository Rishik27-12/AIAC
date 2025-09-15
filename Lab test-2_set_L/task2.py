import csv
from collections import defaultdict
import tempfile
import os
import random
import string

def accumulate_customer_totals(csv_filepath):
    """
    Reads a CSV file with fields: order_id, customer, amount.
    Accumulates total amounts per customer.
    Returns a dict {customer: total_amount}.
    Skips malformed rows and handles empty files gracefully.
    """
    totals = defaultdict(float)
    try:
        with open(csv_filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) != 3:
                    continue  # Skip malformed rows
                order_id, customer, amount = row
                try:
                    amount_val = float(amount)
                except ValueError:
                    continue  # Skip rows with invalid amount
                totals[customer] += amount_val
    except FileNotFoundError:
        print(f"File not found: {csv_filepath}")
        return {}
    return dict(totals)

def print_sorted_totals(totals):
    """
    Prints customer totals sorted by customer name.
    """
    for customer in sorted(totals):
        print(f"{customer}: {totals[customer]:.2f}")

# --- Test Cases ---

def test_small_dataset():
    print("Test: Small Dataset")
    sample_csv = """1,Alice,100.50
2,Bob,200
3,Alice,50
4,Charlie,300.75
5,Bob,abc
6,Bob,100
7,MalformedRow
8,David,400
"""
    expected = {
        'Alice': 150.50,
        'Bob': 300.0,
        'Charlie': 300.75,
        'David': 400.0
    }
    with tempfile.NamedTemporaryFile('w+', delete=False, newline='') as tmp:
        tmp.write(sample_csv)
        tmp.flush()
        totals = accumulate_customer_totals(tmp.name)
        print_sorted_totals(totals)
        # Check correctness
        assert all(abs(totals.get(k, 0) - v) < 1e-6 for k, v in expected.items()), f"Expected {expected}, got {totals}"
    os.unlink(tmp.name)
    print("Small dataset test passed.\n")

def test_empty_file():
    print("Test: Empty File")
    with tempfile.NamedTemporaryFile('w+', delete=False, newline='') as tmp:
        tmp.flush()
        totals = accumulate_customer_totals(tmp.name)
        print_sorted_totals(totals)
        assert totals == {}, f"Expected empty dict, got {totals}"
    os.unlink(tmp.name)
    print("Empty file test passed.\n")

def test_large_dataset(num_customers=1000, orders_per_customer=1000):
    print("Test: Large Dataset")
    customers = [f"Customer_{i}" for i in range(num_customers)]
    with tempfile.NamedTemporaryFile('w+', delete=False, newline='') as tmp:
        writer = csv.writer(tmp)
        expected = defaultdict(float)
        for customer in customers:
            for _ in range(orders_per_customer):
                amount = round(random.uniform(1, 1000), 2)
                order_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
                writer.writerow([order_id, customer, str(amount)])
                expected[customer] += amount
        tmp.flush()
        totals = accumulate_customer_totals(tmp.name)
        # Only print first 5 for brevity
        print("First 5 customers' totals:")
        for customer in sorted(list(totals)[:5]):
            print(f"{customer}: {totals[customer]:.2f}")
        # Check correctness (within a small tolerance due to float rounding)
        for customer in customers:
            assert abs(totals[customer] - expected[customer]) < 1e-2, f"Mismatch for {customer}"
    os.unlink(tmp.name)
    print("Large dataset test passed.\n")

if __name__ == "__main__":
    test_small_dataset()
    test_empty_file()
    test_large_dataset()

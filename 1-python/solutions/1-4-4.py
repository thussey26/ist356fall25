'''
Write tests

'''


# Test functions to assert expected results

def test_parsedate_mdy():
    # Test Case 1: Valid input
    date = parsedate_mdy("02/05/2025")
    assert date == datetime(2025, 2, 5), f"Test failed: expected '2025-02-05', got {date}"

    # Test Case 2: Another valid input
    date = parsedate_mdy("12/25/2023")
    assert date == datetime(2023, 12, 25), f"Test failed: expected '2023-12-25', got {date}"

def test_formatdate_ymd():
    # Test Case 1: Valid datetime object
    date_str = formatdate_ymd(datetime(2025, 2, 5))
    assert date_str == "2025-02-05", f"Test failed: expected '2025-02-05', got {date_str}"

    # Test Case 2: Another valid datetime object
    date_str = formatdate_ymd(datetime(2023, 12, 25))
    assert date_str == "2023-12-25", f"Test failed: expected '2023-12-25', got {date_str}"

# Run the test functions
if __name__ == "__main__":
    test_parsedate_mdy()
    test_formatdate_ymd()
    print("All tests passed!")

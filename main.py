#!/usr/bin/env python3
"""
Test code for lib.py functions.
This script tests the CSV reading and display functionality.
"""

import sys
import os
from pathlib import Path

# Import functions from lib.py
from lib import read_output_csv, display_data, load_and_display, get_data_summary, print_summary


def test_csv_functions():
    """
    Test the CSV reading and display functions.
    """
    print("=== Testing lib.py functions ===\n")
    
    # Test file path (look for data.csv in current directory)
    test_file = Path(__file__).parent / "data.csv"
    
    print(f"Testing with file: {test_file}")
    
    # Test 1: Read CSV file
    print("\n1. Testing read_output_csv function:")
    data = read_output_csv(str(test_file))
    
    if data is not None:
        print(f"✓ Successfully read {len(data)} rows of data")
    else:
        print("✗ Failed to read data or file not found")
        print("Note: This is expected if data.csv doesn't exist yet.")
        print("Run func.py first to generate output data.csv")
        create_sample_data()
        return
    
    # Test 2: Display data
    print("\n2. Testing display_data function:")
    display_data(data)
    
    # Test 3: Combined load and display
    print("\n3. Testing load_and_display function:")
    data2 = load_and_display(str(test_file))
    
    # Test 4: Get data summary
    print("\n4. Testing get_data_summary function:")
    summary = get_data_summary(data)
    
    if summary:
        print("✓ Summary calculation successful")
        print_summary(summary)
    else:
        print("✗ Summary calculation failed")
    
    print("=== Test completion ===\n")


def create_sample_data():
    """
    Create sample data.csv for testing if it doesn't exist.
    """
    try:
        import pandas as pd
        
        # Create sample data based on specification
        sample_data = pd.DataFrame({
            'data': [-4, -14, -24, -114, -3319]  # Results of y = -5*x + 1 for x = [1, 3, 5, 23, 664]
        })
        
        sample_file = Path(__file__).parent / "data.csv"
        sample_data.to_csv(sample_file, index=False)
        print(f"Created sample data file: {sample_file}")
        
        # Now test with the sample data
        print("\nTesting with sample data:")
        test_csv_functions()
        
    except ImportError:
        print("pandas not available for creating sample data")
    except Exception as e:
        print(f"Error creating sample data: {str(e)}")


def main():
    """
    Main test function.
    """
    print("Starting lib.py function tests...\n")
    
    try:
        test_csv_functions()
        print("All tests completed!")
        
    except Exception as e:
        print(f"Error during testing: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Function processor that reads CSV data, applies mathematical function, and outputs results.
Implements y = f(x) = -5*x + 1

Usage:
    python func.py -i <input_folder> -o <output_folder>
"""

import argparse
import pandas as pd
import os
import shutil
import sys
from pathlib import Path


def apply_function(x):
    """
    Apply the predefined function to input value.
    Function: y = f(x) = -5*x + 1
    
    Args:
        x (float): Input value
        
    Returns:
        float: Calculated output value
    """
    return -5 * x + 1


def process_data(input_folder, output_folder):
    """
    Process CSV data by applying function and save results.
    
    Args:
        input_folder (str): Path to input folder containing data.csv
        output_folder (str): Path to output folder for results
        
    Returns:
        bool: True if processing successful, False otherwise
    """
    try:
        # Check input file existence
        input_file = Path(input_folder) / "data.csv"
        if not input_file.exists():
            print(f"Error: Input file {input_file} does not exist.")
            return False
        
        # Read input CSV
        print(f"Reading input data from: {input_file}")
        df = pd.read_csv(input_file)
        
        # Validate input format
        if 'x' not in df.columns:
            print("Error: Input CSV must have 'x' column.")
            return False
        
        # Extract x values and convert to numeric
        x_values = pd.to_numeric(df['x'], errors='coerce')
        
        # Check for conversion errors
        if x_values.isna().any():
            print("Warning: Some x values could not be converted to numbers.")
            x_values = x_values.dropna()
        
        # Apply function to calculate y values
        y_values = x_values.apply(apply_function)
        
        # Create output directory if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)
        
        # Create output DataFrame with format1 specification
        output_df = pd.DataFrame({'data': y_values})
        
        # Save output CSV
        output_file = Path(output_folder) / "data.csv"
        output_df.to_csv(output_file, index=False)
        print(f"Output data saved to: {output_file}")
        
        # Copy required files to output folder
        copy_files_to_output(output_folder)
        
        return True
        
    except Exception as e:
        print(f"Error during processing: {str(e)}")
        return False


def copy_files_to_output(output_folder):
    """
    Copy lib.py, main.py, and data.md to output folder.
    
    Args:
        output_folder (str): Path to output folder
    """
    try:
        # Get current script directory
        script_dir = Path(__file__).parent
        
        # Files to copy
        files_to_copy = ['lib.py', 'main.py', 'data.md']
        
        for filename in files_to_copy:
            src_file = script_dir / filename
            dst_file = Path(output_folder) / filename
            
            if src_file.exists():
                shutil.copy2(src_file, dst_file)
                print(f"Copied {filename} to output folder")
            else:
                print(f"Warning: {filename} not found in current directory")
                
    except Exception as e:
        print(f"Error copying files: {str(e)}")


def main():
    """
    Main function to handle command line arguments and execute processing.
    """
    parser = argparse.ArgumentParser(
        description="Process CSV data with mathematical function y = -5*x + 1"
    )
    parser.add_argument(
        '-i', '--input', 
        required=True, 
        help='Input folder containing data.csv'
    )
    parser.add_argument(
        '-o', '--output', 
        required=True, 
        help='Output folder for results'
    )
    
    args = parser.parse_args()
    
    # Validate input folder
    if not os.path.exists(args.input):
        print(f"Error: Input folder '{args.input}' does not exist.")
        sys.exit(1)
    
    # Process data
    print("Starting data processing...")
    success = process_data(args.input, args.output)
    
    if success:
        print("Processing completed successfully!")
        sys.exit(0)
    else:
        print("Processing failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()

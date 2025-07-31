#!/usr/bin/env python3
"""
Library functions for reading and displaying output CSV data.
"""

import pandas as pd
import os
from pathlib import Path


def read_output_csv(file_path):
    """
    Read output CSV file and return data.
    
    Args:
        file_path (str): Path to the CSV file to read
        
    Returns:
        pd.DataFrame: Loaded data, or None if error occurred
    """
    try:
        if not os.path.exists(file_path):
            print(f"Error: File {file_path} does not exist.")
            return None
        
        # Read CSV file
        df = pd.read_csv(file_path)
        print(f"Successfully loaded data from: {file_path}")
        return df
        
    except Exception as e:
        print(f"Error reading CSV file: {str(e)}")
        return None


def display_data(data):
    """
    Display data to stdout.
    
    Args:
        data (pd.DataFrame): Data to display
    """
    if data is None:
        print("No data to display.")
        return
    
    try:
        print("\n=== Data Display ===")
        print(f"Shape: {data.shape[0]} rows, {data.shape[1]} columns")
        print(f"Columns: {list(data.columns)}")
        print("\nData:")
        print(data.to_string(index=False))
        print("===================\n")
        
    except Exception as e:
        print(f"Error displaying data: {str(e)}")


def load_and_display(file_path):
    """
    Convenience function to load CSV file and display its contents.
    
    Args:
        file_path (str): Path to the CSV file
    """
    data = read_output_csv(file_path)
    display_data(data)
    return data


def get_data_summary(data):
    """
    Get summary statistics of the data.
    
    Args:
        data (pd.DataFrame): Data to summarize
        
    Returns:
        dict: Summary statistics
    """
    if data is None:
        return None
    
    try:
        summary = {}
        for column in data.columns:
            if data[column].dtype in ['int64', 'float64']:
                summary[column] = {
                    'count': len(data[column]),
                    'mean': data[column].mean(),
                    'std': data[column].std(),
                    'min': data[column].min(),
                    'max': data[column].max()
                }
        return summary
        
    except Exception as e:
        print(f"Error calculating summary: {str(e)}")
        return None


def print_summary(summary):
    """
    Print summary statistics to stdout.
    
    Args:
        summary (dict): Summary statistics dictionary
    """
    if summary is None:
        print("No summary available.")
        return
    
    print("\n=== Data Summary ===")
    for column, stats in summary.items():
        print(f"\nColumn: {column}")
        for stat_name, stat_value in stats.items():
            print(f"  {stat_name}: {stat_value:.4f}")
    print("====================\n")

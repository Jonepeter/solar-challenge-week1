# Author: Petros Abebe
# Description: This script loads the data from the specified path and returns it as a pandas DataFrame.
# Usage: python scripts/load_data.py
# Import necessary libraries
import pandas as pd
import os
import sys
import logging

# define function to load data
def load_data(data_path):
    """
    Load data from the specified path and return it as a pandas DataFrame.
    
    Parameters:
    data_path (str): The path to the data file.
    
    Returns:
    pd.DataFrame: The loaded data.
    """
    try:
        # Check if the file exists
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"The file {data_path} does not exist.")
        
        # Load the data
        data = pd.read_csv(data_path)
        
        # Return the loaded data
        return data
    
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        sys.exit(1)
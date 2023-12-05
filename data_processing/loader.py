import pandas as pd


def load_excel_data(file_path):
    """
    Load an Excel file into a pandas DataFrame.

    Parameters:
    file_path (str): The path to the Excel file.

    Returns:
    DataFrame: A pandas DataFrame containing the data from the Excel file.
    """
    try:
        data = pd.read_excel(file_path)
        print("Data found. Data head:", data.head())
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")


def load_simulated_data():
    """
    Load the simulated data from the Excel file.

    Returns:
    DataFrame: A pandas DataFrame containing the simulated data.
    """
    # Update the file path to the correct location
    return load_excel_data('../excels/Simulated Data.xlsx')


def load_real_world_data():
    """
    Load the real-world data from the Excel file.

    Returns:
    DataFrame: A pandas DataFrame containing the real-world data.
    """
    # Update the file path to the correct location
    return load_excel_data('../excels/CPP Real World Data.xlsx')

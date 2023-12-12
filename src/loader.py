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

    return load_excel_data('../data/Simulated Data.xlsx')


def load_real_world_data():
    """
    Load the real-world data from the Excel file.

    Returns:
    DataFrame: A pandas DataFrame containing the real-world data.
    """

    return load_excel_data('../data/CPP Real World Data.xlsx')


def main():
    # Testing purposes
    real_world_data = load_real_world_data()
    simulated_data = load_simulated_data()
    print(real_world_data.head())
    print(simulated_data.head())


if __name__ == "__main__":
    main()

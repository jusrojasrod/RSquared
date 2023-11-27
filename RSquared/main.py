# import pandas_datareader.data as reader    # Para traer la data directamente
# de la página de Fama-French

import pandas as pd
# import numpy as np
# from datetime import date
# import yfinance as yf
# import matplotlib.pyplot as plt

import os
import time


def runStrategy():
    """
    """
    pass


if __name__ == "__main__":
    # Start timer
    start_time = time.time()

    # Setup
    folderPath_rsrc = '/ETFs/Resources/'
    folderPath_results = '/ETFs/results/'
    pictures = '/Pictures/'
    cwd = os.getcwd()
    path_rsrc = cwd + folderPath_rsrc
    path_results = cwd + folderPath_results

    # Read data
    ETFs = pd.read_excel(path_rsrc + "list_of_ETFs.xlsx")

    runStrategy()

    elapsed_time = time.time() - start_time

    print(f"Elapsed time: {elapsed_time:.2f} s")

import re
import glob
import numpy as np
import wfdb #WaveForm-Database package. A library of tools for reading, writing, and processing WFDB signals and annotations.
from pathlib import Path

def convert_to_csv(path='*.dat', new_folder=True):
    """
    Code to convert all .dat files (ECG signals) in a folder to CSV format
    Path - location of the dat files (str)
    new_fodlder - whether to put the files in a new csv folder (boolean)

    @authors: Abhishek Patil, Enes Ahmeti
    """
    print('Reading files...')
    if new_folder:
        Path("csv_files").mkdir(parents=True, exist_ok=True)
    dat_files = glob.glob(path) # Get list of all .dat files in the current folder
    for file in dat_files:
        print(file)
        filename = re.match("([^.]*)", file).group() # Get only the name from file.
        record, fields = wfdb.rdsamp(filename) # Read the data
        header = ",".join(["-".join(x) for x in zip(fields['sig_name'], fields['units'])]) # column headers
        filename = f"csv_files/{filename}.csv" if new_folder else f"{filename}.csv" # Add to the corresponding folder 
        np.savetxt(filename, record, delimiter=",", header=header) # Save text.
    print('All files read successfully!')


if __name__ == "__main__":
    convert_to_csv()

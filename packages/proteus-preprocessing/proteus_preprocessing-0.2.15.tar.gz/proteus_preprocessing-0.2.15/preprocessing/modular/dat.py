import numpy as np
import pandas as pd


def _get_file_dataframe(data_file, name):
    with open(data_file) as myfile:
        _ = next(myfile)
        ncol = int(next(myfile).rstrip(" \n"))
        colArray = [next(myfile).split()[0] for _ in range(0, ncol)]
        colArray[-1] = name
        data = np.loadtxt(myfile, skiprows=0)
        return pd.DataFrame(data, columns=colArray)


def preprocess(dat_file, mapping):
    return {
        keyword["name"]: _get_file_dataframe(dat_file[keyword.get("name")], keyword.get("name")) for keyword in mapping
    }

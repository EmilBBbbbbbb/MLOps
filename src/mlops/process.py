import numpy as np
import pandas as pd


def data_cleaner(path: str)->None:

    """The function cleans the data: it removes duplicates and fills in missing values."""

    data = pd.read_csv(path)

    data_clean = data.copy()

    data_clean = data_clean.drop_duplicates()
    numeric_columns = data_clean.select_dtypes(include=[np.number]).columns
    object_columns = [x for x in data_clean.columns if x not in numeric_columns]

    for n in numeric_columns:
        data_clean[n] =  data_clean[n].fillna(data_clean[n].median())
    for o in object_columns:
        data_clean[o] =  data_clean[o].fillna('unknown')

    data_clean.to_csv('output/result.csv')

if __name__=='__main__':
    data_cleaner('data/input.csv')

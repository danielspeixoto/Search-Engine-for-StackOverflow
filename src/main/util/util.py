import pandas as pd


def to_pandas_df(arr: [object]) -> pd.DataFrame:
    variables = arr[0].keys()
    df = pd.DataFrame([[getattr(i, j) for j in variables]
                       for i in arr], columns=variables)

    return df
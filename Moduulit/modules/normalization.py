import pandas as pd

def normalisointi(df):
    """[Normalisoi kaikki dataframen sarakkeet]

    Args:
        df ([DataFrame]): [yhdistetty dataframe.]

    Returns:
        [Dataframe]: [Normalisoitu dataframe.]
    """

    for col in df.columns:
        if col != "value_MenovesiLaskAs":
            df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
        
    return df
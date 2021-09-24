import pandas as pd
def delete_summer_months(df):
    """[positaa dataframesta rivit kuukausilta 6, 7 ja 8]

    Args:
        df ([DataFrame]): [yhdistetty dataframe]

    Returns:
        [DataFrame]: [Dataframe, josta poistettu kesäkuukaudet]
    """
    
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df["month"] = df.timestamp.dt.month
    df = df[df["month"] != 6]
    df = df[df["month"] != 7]
    df = df[df["month"] != 8]
    df = df.drop(columns=["month"])
    return df
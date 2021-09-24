import pandas as pd

def split_by_day(df, mod=4):
    
    """[Jakaa annetun dataframen kahteen dataframeen siten, etta saman paivan dataa ei voi kuulua kumpaankin dataframeen]

    Parameters:
        df ([Dataframe]): [Jaettava dataframe]
        mod ([int]): [joka neljannes paiva menee pienenpaan dataframeen]

    Returns:
        big_df [dataframe]: [Valtaosa datasta.]
        small_df [dataframe]: [joka neljannen paivan sisaltava dataframe.]
        
        """
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df["weekday"] = df.timestamp.dt.weekday
    df["week_diff"] = df["weekday"].diff()
    start_len = len(df)
    small_df = []
    big_df = []

    ix = 0
    
    save = True
    for row in df.itertuples():
        if row.week_diff > 0:
            ix += 1
            
            # Joka mod:nes päivä lisätään treenisettiin.
            if ix % mod == 0:
                save = False
            if ix % mod != 0:
                save = True
        if save == False:
            small_df.append(row)
        if save == True:
            big_df.append(row)


    print(f"Pienemmän datasetin osuus koko datasta: {round(len(small_df)/start_len,2)}")
    small_df = pd.DataFrame(small_df)
    big_df = pd.DataFrame(big_df)
    big_df.drop(columns=["Index", "week_diff"], inplace=True)
    small_df.drop(columns=["Index", "week_diff"], inplace=True)
    return big_df, small_df
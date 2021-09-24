def trendflagsit(df):
    """[Deletes all rows where trendFlags is start]

    Parameters:
        df   ([type]): [pandas Dataframe]
        

    Returns:
        pandas Dataframe
    """
    
    
    print('rows at the start: ', len(df))
    for col in df.columns:
        split = col.split("_")
        if split[0] == "trendFlags":
            if '{start}' in df[col].unique():
                df = df[df[col] != "{start}"]
    
    print('rows after operation: ', len(df))
    df = df.reset_index(drop=True)
    return df
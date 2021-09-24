def value_siivous(df):
    """[Deletes all rows where value_LTOS is under 100]

    Parameters:
        df   ([type]): [pandas Dataframe]
        

    Returns:
        pandas Dataframe
    """
    
    
    print('rows at the start: ', len(df))
    print('check how many NaN values there are and remove them: ',df.value_LTOS.isnull().sum())
    df = df.dropna(subset=['value_LTOS'])
    print('remove all rows where value_LTOS is under 100')
    df = df[df.value_LTOS == 100]
    print('rows after operation: ', len(df))
    df = df.reset_index(drop=True)
    return df
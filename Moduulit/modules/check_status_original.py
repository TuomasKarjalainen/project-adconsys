def check_status(df):
    """
    
    TUTKII STATUS-SARAKKEEN ARVOJA
    LÖYTYYKÖ STATUKSESTA FAULT TAI DOWN ARVOJA JA POISTAA NE AUTOMAATTISESTI
    JOS STATUKSESTA LÖYTYY OVERRIDDEN ARVOJA, NE VOI VALINNAINESTI POISTAA TAI OLLA POISTAMATTA

    
    Parameters
    ----------
    
    df :
        - Type: Pandas DataFrame
        
    
    Returns
    -------
    
    Nothing

    
    """
    print("Checking unique values of status...")
    print()
    print("Values in status-column:",df['status'].unique())
    
    if '{overridden}' in df['status'].unique():
        print("\nFOUND 'OVERRIDDEN' VALUES !!")
        ans = str(input("\nDo you want to drop them?  (y/n)"))
        
        if ans == "y":
            print("DataFrame's shape before:", df.shape)
            print("Dropping rows where's {overridden} -value in status-column...")
            df = df[df['status'] != "{overridden}"]
            print("\nDataFrame's shape now:", df.shape)                   
        else:
            print(df['status'].unique())
            print("\nDataFrame's shape", df.shape)  
    
    if '{fault}' in df['status'].unique():
        print("\nFOUND 'FAULT' VALUES !!")
        print("\nDropping all rows where's {fault} -value in status-column")
        df = df[df['status'] != "{fault}"]
        print("\nDataFrame's shape now:", df.shape)
        print("Values in status-column:",df['status'].unique())
        
    
    if '{down}' in df['status'].unique():
        print("\nFOUND 'DOWN' VALUES !!")
        print("\nDropping all rows where's {down} -value in status-column")
        df = df[df['status'] != "{down}"]
        print("\nDataFrame's shape now:", df.shape) 
        print("Values in status-column:",df['status'].unique())
        
    if '{fault,overridden}' in df['status'].unique():
        print("\nFOUND 'FAULT, OVERRIDDEN' VALUES !!")
        print("\nDropping all rows where's {fault,overridden} -value in status-column")
        df = df[df['status'] != "{fault,overridden}"]
        print("\nDataFrame's shape now:", df.shape) 
        print("Values in status-column:",df['status'].unique())
        
    
    
    return df
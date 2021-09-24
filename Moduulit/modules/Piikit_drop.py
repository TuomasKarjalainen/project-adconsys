from timeit import default_timer as timer 

def piikit_drop(df):
    """
    
    piikit_drop -function
    
    Remove all rows where value_LammitysS is 100
    
    Parameters:
    
        df(type): pandas DataFrame
        
    Returns:
        
        pandas DataFrame
    
    """
    
    start = timer()
    print("\nAll rows: ", df.shape)
    print("\nChecking the column 'value_LammitysS' for NaN values: ", df.value_LammitysS.isnull().sum())
    df = df.dropna(subset=['value_LammitysS'])
    print("\nChecking the rows for 100 values: ", df[df.value_LammitysS == 100].shape)
    print("\n-----------------------------------------")
    print("Removing all rows that contain a 100 value")
    print("-----------------------------------------")
    df = df[df.value_LammitysS != 100] 
    print("\nNew all rows: ", df.shape)
    
    end = timer()
    print("\nDone in", round(end-start,2),"seconds")
    
    return df
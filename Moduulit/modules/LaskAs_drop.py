from timeit import default_timer as timer 

def laskas_drop(df):
    """
    
    laskas_drop -function
    
    Remove all rows where value_LaskAs is 0
    
    Parameters:
    
        df(type): pandas DataFrame
        
    Returns:
        
        pandas DataFrame
    
    """
    
    start = timer()
    print("\nAll rows: ", df.shape)
    print("\nChecking the column 'value_1LaskAs' for NaN values: ", df.value_1LaskAs.isnull().sum())
    df = df.dropna(subset=['value_1LaskAs'])
    print("\nChecking the rows for 0 values: ", df[df.value_1LaskAs == 0].shape)
    print("\n-----------------------------------------")
    print("Removing all rows that contain a 0 value")
    print("-----------------------------------------")
    df = df[df.value_1LaskAs != 0] 
    print("\nNew all rows: ", df.shape)
    
    end = timer()
    print("\nDone in", round(end-start,2),"seconds")
    
    return df
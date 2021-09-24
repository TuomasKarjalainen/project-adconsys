from timeit import default_timer as timer 


# FUNKTIO POISTAA YHDISTETYSTÄ DATAFRAMESTA KAIKKI STATUS, TIMESTAMP, VALUE-DIFFERENCE JA TRENDFLAGS SARAKKEET
# JÄLJELLE JÄÄ VAIN 10 KPL VALUE-SARAKKEITA

def drop_columns(df):
    """
    Function for merged Dataframe.
    
    The last operation to Dataframe before it's feature matrix.
    
    Function removes all status, timestamp, trendFlags and value difference -columns.
    After function Dataframe contains only timestamp and 20 different value columns.
    
    Parameters
    ----------
    
    df :
        - Type: Pandas Dataframe
        - merged Dataframe
        

    Returns
    -------
    
    Pandas DataFrame
    
    """
    start = timer()
    print("-------------------------------------------------------------")
    print("---------------- Removing useless columns -------------------")
    print("-------------------------------------------------------------\n")
    for col in df.columns:
        split = col.split("_")
        if "trendFlags" in col:
            df = df.drop(columns=[col])
        if "status" in col:
            df = df.drop(columns=[col])
        if "value_difference" in col:
            df = df.drop(columns=[col])
        if "value_LTOS" in col:
            df = df.drop(columns=[col])
            
    end = timer()    
    print("\n Dataframe now:\n")
    display(df.head(3))
    print("\n\nDone in", round(end-start,2),"seconds.")
    
    return df 
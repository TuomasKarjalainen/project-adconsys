from timeit import default_timer as timer 



def checkstatus(df):
    """
    
    Datacleaning function for Merged Dataframe. 
    Function checks Merged Dataframe's all status columns and removes all rows that DO NOT have {ok} value.
    Keeps {overridden} values in:
    - TK1_TE1_3_Tuloilma_LaskettuAs
    - TK1_TF1_PE1_1_LaskAs
    - IV_TE3A_Menovesi_LaskAs
    
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
    print("Checking all status-columns...\n")
    print("DataFrame's shape before operation:", df.shape,"\n")
    before = df.shape[0]
    for col in df.columns:
        split = col.split("_")
        if split[0] == "status":
            print("\n------------------------\n")
            print("Column:", col)
            print("Values:",df[col].unique())        
            
  
            # Checks overriddens
            if '{overridden}' in df['status_PoistoM'].unique():  
                print("Dropping {overridden} -rows...")
                df = df[df['status_PoistoM'] != "{overridden}"]                         
  
 
            if '{overridden}' in df['status_MenoM'].unique():
                print("Dropping {overridden} -rows...")
                df = df[df['status_MenoM'] != "{overridden}"]                         
     
                    
            if '{overridden}' in df['status_PatterinPaluuvesiM'].unique():
                    print("Dropping {overridden} -rows...")
                    df = df[df['status_PatterinPaluuvesiM'] != "{overridden}"]                         

       
            if '{overridden}' in df['status_TuloM'].unique():
                print("Dropping {overridden} -rows...")
                df = df[df['status_TuloM'] != "{overridden}"]                         

            
            if '{overridden}' in df['status_LTOS'].unique():
                print("Dropping {overridden} -rows...")
                df = df[df['status_LTOS'] != "{overridden}"]     
                
            if '{overridden}' in df['status_LammitysS'].unique():
                print("Dropping {overridden} -rows...")
                df = df[df['status_LammitysS'] != "{overridden}"]  

                
            # Checks faults
            if '{fault}' in df[col].unique():
                print("Dropping {fault} -rows...")
                df = df[df[col] != "{fault}"]
                         
            # Checks downs
            if '{down}' in df[col].unique():
                print("Dropping {down} -rows...")
                df = df[df[col] != "{down}"]
                       
            # Checks fault,overriddens
            if '{fault,overridden}' in df[col].unique():
                print("Dropping {fault,overridden} -rows...")
                df = df[df[col] != "{fault,overridden}"]
                
            # Checks fault,downs  
            if '{fault,down}' in df[col].unique():
                print("Dropping {fault,overridden} -rows...")
                df = df[df[col] != "{fault,down}"]
    
    print("\nDataFrame's shape after operation:", df.shape)
    print("Rows removed:",before-df.shape[0])
    end = timer()
    print("\nDone in", round(end-start,2),"seconds.")
    
    return df
from timeit import default_timer as timer 

# YHDISTETYN DATAFRAMEN RIVIEN POISTOON

def removeoutliers(df, templim, perclim):
    """
    
    Function for merged Dataframe's cleaning.
    Function removes all rows wheres value_differences are above the limits.
    Define the limit for temperature values (templim) AND percentage values (perclim).
    
    
    Parameters
    ----------
    
    df :
        - Type: Pandas Dataframe
        - merged Dataframe
        
        
    templim :
        - Type: float
        - Default: True
        - If True, removes {overridden} values 
        - If False, keeps rows with {overridden} values
 
 
     perclim :
        - Type: float
        - Limit value for columns that has percentage values 


    Returns
    -------
    
    Pandas DataFrame
    
    """
    start = timer()
    before = df.shape[0]
    print("------------------------------------------------")
    print("------------- Removing outliers ----------------")
    print("------------------------------------------------")
    print("\nLimit value for temperatures is set:",templim)
    print("Limit value for percentages is set:",perclim)
    print()
    
    print("\nTemperature columns...")
    for col in df.columns:
        if col == "value_difference_TuloM":
            print("Removing rows from ", col)
            df = df[df['value_difference_TuloM'] < templim]
            
        if col == "value_difference_MenovesiLaskAs":
            print("Removing rows from ", col)
            df = df[df['value_difference_MenovesiLaskAs'] < templim]
         
    
        if col == "value_difference_PatterinPaluuvesiM":
            print("Removing rows from ", col)
            df = df[df['value_difference_PatterinPaluuvesiM'] < templim]     
    
        if col == "value_difference_MenoM":
            print("Removing rows from ", col)
            df = df[df['value_difference_MenoM'] < templim]    
    
        if col == "value_difference_TuloilmaLaskettuAs":
            print("Removing rows from ", col)
            df = df[df['value_difference_TuloilmaLaskettuAs'] < templim]
            
        if col == "value_difference_UlkoLampotila":
            print("Removing rows from ", col)
            df = df[df['value_difference_UlkoLampotila'] < templim]            
    print("Removed values:", before - df.shape[0])
    
    before2 = df.shape[0]
    
    print("\nPercentage columns...")
    for col in df.columns:
        if col == "value_difference_LammitysS":
            print("Removing rows from ", col)
            df = df[df['value_difference_LammitysS'] < templim]
            
        
        if col == "value_difference_1LaskAs":
            print("Removing rows from ", col)
            df = df[df['value_difference_1LaskAs'] < templim]   
        
    print("Removed values:", before2 - df.shape[0])
    
    print("\nRemoved values in total:", before - df.shape[0])
    print("Dataframe's shape before:",before)
    print("Dataframe's shape now:",df.shape[0])
    end = timer()
    print("\nDone in", round(end-start,2),"seconds.")
    
    return df
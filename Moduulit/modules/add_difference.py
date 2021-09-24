from timeit import default_timer as timer 

# FUNKTIO LISÄÄ value_difference -KOLUMNIT YHDISTETTYYN DATAFRAMEEN

def add_value_diff(df):
    """
    
    Function for merged Dataframe.
    Funtion adds value_difference columns for each value.
    It takes abs from adjusment/percentage values.
    
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
    print("------------- Adding column value_difference ----------------")
    print("-------------------------------------------------------------\n")
    
    for col in df.columns:
        split = col.split("_")
        if "value" in col:
                
                # PROSENTTIARVOISTA EI OTETA ITSEISARVOA
            
                if split[-1] == "1LaskAs":
                    df[f'value_difference_{split[-1]}'] = (df['value_1LaskAs'].diff())
                    print(f'value_difference_{split[-1]}')
                    
                if split[-1] == "LammitysS":
                    df[f'value_difference_{split[-1]}'] = (df[col].diff())
                    print(f'value_difference_{split[-1]}')
                    
                if split[-1] == "LTOS":
                    df[f'value_difference_{split[-1]}'] = (df[col].diff())                    
                    print(f'value_difference_{split[-1]}')
                        
                # LÄMPÖTILOISTA OTETAAN ITSEISARVO

                if split[-1] == "MenovesiLaskAs":
                    df[f'value_difference_{split[-1]}'] = abs(df[col].diff())
                    print(f'value_difference_{split[-1]}')
                    
                if split[-1] == "MenoM":
                    df[f'value_difference_{split[-1]}'] = abs(df[col].diff())
                    print(f'value_difference_{split[-1]}')
                    
                if split[-1] == "UlkoLampotila":
                    df[f'value_difference_{split[-1]}'] = abs(df[col].diff())
                    print(f'value_difference_{split[-1]}')
                    
                if split[-1] == "TuloM":
                    df[f'value_difference_{split[-1]}'] = abs(df[col].diff())
                    print(f'value_difference_{split[-1]}')
                    
                if split[-1] == "TuloilmaLaskettuAs":
                    df[f'value_difference_{split[-1]}'] = abs(df[col].diff())
                    print(f'value_difference_{split[-1]}')
                    
                if split[-1] == "PoistoM":
                    df[f'value_difference_{split[-1]}'] = abs(df[col].diff())
                    print(f'value_difference_{split[-1]}')
                    
                if split[-1] == "PatterinPaluuvesiM":
                    df[f'value_difference_{split[-1]}'] = abs(df[col].diff())
                    print(f'value_difference_{split[-1]}')
                    
                    
    end = timer()
    print("\nDataframe shape", df.shape)
    print("\nDone in", round(end-start,2),"seconds.")
    
    return df
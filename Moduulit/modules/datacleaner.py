import pandas as pd 
import numpy as np
from sklearn.preprocessing import LabelEncoder
from timeit import default_timer as timer 

# Siistitään aikaleimat
# Poistetaan duplikaatit
# Lisätään uudet columinit
# Muutetaan arvot numeromuotoon


def dataCleaner(df, newColumns=True, numericValues=False, rmd=True, abs_value=True):
    
    """
    
    dataCleaner -function
    
    Cleans timestamp, adds new columns (if newColumns=True) and transform status-values into numeric (if numericValues=True)
    Check duplicates and remove them
    Adds value_difference column 
    
    Parameters
    ----------
    
    df :
        - Type: Pandas DataFrame
        
 
    newColumns :
        - Type: boolean
        - Default: True
        - If True, adds new columns day, month, year and date
    
    numericValues :
        - Type: boolean
        - Default: False
        - If True, transforms values into numeric
    
    rmd :
        - Type: boolean
        - Default: True
        - If True, checks if DataFrame contains dublicates and then removes them
        
    abs_value :
        - Type: boolean
        - Default: True
        - If True, takes absolute value of value_difference
        - TRUE if value_difference is TEMPERATURE value
        - FALSE if value_difference is ADJUSTMENT value (säätöarvo)
        
        
    
    Returns
    -------
    
    Pandas DataFrame

    
    """
   

    start = timer()
    print("----------------------")
    print("Processing DataFrame:")
    print("----------------------")
    print("\nCleaning timestamp...")



    # Muokataan timestamp
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

    # Luodaan uudet columnit, jos se pn parametreissä määritetty
    if newColumns == True:
        print("Creating new columns...")
        df['day'] = df.timestamp.dt.day
        df['month'] = df.timestamp.dt.month
        df['year'] = df.timestamp.dt.year
        df['date'] = pd.to_datetime({'year':df['year'],'month':df['month'],'day':df['day']})


    if numericValues == True:
        # Muutetaan arvot numeeriseen muotoon
        print("Transforming values into numeric...")
        enc = LabelEncoder()
        status = df['status']
        status_new = pd.Series(enc.fit_transform(status.astype('str')))
        df['status'] = status_new
        # Jos dataframe sisältää myös trendFlags -sarakkeen, muutetaan sekin numeromuotoon
        if 'trendFlags' in df:
            trendFlags = df['trendFlags']
            trendFlags_new = pd.Series(enc.fit_transform(trendFlags.astype('str')))
            df['trendFlags'] = trendFlags_new
            
            
    if rmd == True:
        # Tarkistetaan duplikaatit
        # Jos niitä on, poistetaan automaattisesti
        print("Checking duplicates...")
        df_dups = df.duplicated().sum()
        if df_dups > 0:
            print(df_dups,"duplicates found.")
            print("Removing them.")
            print("DataFrame shape before", df.shape)
            df = df.drop_duplicates()
            print("DataFrame shape after", df.shape)
        
    if abs_value == True:
        print("Creating value_difference column (abs=True)")
        df['value_difference'] = abs(df['value'].diff())
    
    if abs_value == False:
        print("Creating value_difference column (abs=False)")
        df['value_difference'] = df['value'].diff()   
    
 
    end = timer()
    print("\ndone in", round(end-start,2),"seconds")

    return df
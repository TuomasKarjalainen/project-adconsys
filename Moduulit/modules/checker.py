import numpy as np
import pandas as pd 
from timeit import default_timer as timer 




def check_difference(df):
    
    """
    
    check_difference -function
    
    value_differences's values tells difference between current and previous value
    It should be around ~ 0.5
    
    Function shows the maximum difference so we can find out outliers easier
    
    Shows pandas dataframes with few rows around the maximum value of value_difference -column and row(s) with value of the maximum value_difference -value
    
    You can define the limit_value to check how many rows there are with higher limit value. Then you can print them.
    
    Parameters
    ----------
    
    df :
        - Type: Pre-cleaned Pandas DataFrame
        
    
    Returns
    -------
    
    Nothing

    
    """
    
    start = timer()
    print("--------------------------------------------")
    print("Getting max value_difference of DataFrame...")
    print("--------------------------------------------")
    max_dif = df['value_difference'].max()
    print("\nMax value_difference:", max_dif)
    print("\nMean value of value_difference:", df['value_difference'].mean())
    
    # print rows where is the max difference 
    max_diff_rows = df.loc[df['value_difference'] == max_dif]
    print()
    print("\nRows with the maximum value_difference")
    display(max_diff_rows)
    
    # Rows over the defined value
    limit_value = int(input("Define the limit value (e.g 0.75) : "))
    rows_over_lm = df.loc[df['value_difference'] >= limit_value]
    index = rows_over_lm.index
    number_of_rows = len(index) 
    print("\nRows with equal or higher value_difference than {}:".format(limit_value), number_of_rows, "rows.")
    ans = str(input("\nDo you want to print them? (y/n)"))
    if ans == "y":
        print_rows = df.loc[df['value_difference'] >= limit_value]
        print("\nPrinting rows")
        display(print_rows)
    else:
        print()

        
    # Get row indexes 
    row_indexes = []
    for row_num in max_diff_rows.index:
        print()
        print("\nRow indexes where value_difference is", max_dif)
        print(row_num)
        row_indexes.append(row_num)
    
    # print dataframe of rows around the max difference
    print()
    print("\nRows around the maximum value of difference:")
    for i in row_indexes:
        display(df.loc[i-2:i+2])
        print()
    end = timer()
    print("Done in", round(end-start,2), "seconds.")
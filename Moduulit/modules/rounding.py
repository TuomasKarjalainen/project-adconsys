import pandas as pd
def rounding(df):
    """[rounds dataframe values to closest 0.5. Dataframe cant't involve string values]

    Parameters:
        df ([type]): [Pandas Dataframe]
        

    Returns:
        [dataframe]: [Returns rounded dataframe.]
        
        """
    def round_of_rating(number):

        return round(number * 2) / 2
    
    
    df = df.apply(lambda x: round_of_rating(x))
    
    return df


    
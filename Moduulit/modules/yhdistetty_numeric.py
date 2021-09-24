import pandas as pd
def numeric_values(df):
    """[Turns every status column into numeric (0,1,2...)]
    You have to do this operation only with yhdistetty_df.csv-file
    Otherwise will not work

    Parameters:
        df ([type]): [pandas dataframe]
        
    Returns:
        returns pandas dataframe
    """
    
    print('turning values to numeric:')
    df.status_1LaskAs = pd.factorize(df['status_1LaskAs'])[0]
    df.status_MenovesiLaskAs = pd.factorize(df['status_MenovesiLaskAs'])[0]
    df.status_MenoM =pd.factorize(df['status_MenoM'])[0]
    df.status_UlkoLampotila =pd.factorize(df['status_UlkoLampotila'])[0]
    df.status_LammitysS =pd.factorize(df['status_LammitysS'])[0]
    df.status_LTOS =pd.factorize(df['status_LTOS'])[0]
    df.status_TuloM =pd.factorize(df['status_TuloM'])[0]
    df.status_TuloilmaLaskettuAs =pd.factorize(df['status_TuloilmaLaskettuAs'])[0]
    df.status_PoistoM =pd.factorize(df['status_PoistoM'])[0]
    df.status_PatterinPaluuvesiM = pd.factorize(df['status_PatterinPaluuvesiM'])[0]
    print('Done')
    return df
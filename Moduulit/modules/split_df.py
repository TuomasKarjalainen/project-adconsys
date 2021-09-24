from sklearn.model_selection import train_test_split 

def split_df(df, test_size= 0.2, valid_size=0.3):
    """[Jakaa piirrematriisin treeni-, testi- ja validointi -dataframeihin.]

    Args:
        df ([DataFrame]): [Piirrematriisi]
        test_size ([float]): [Testisetin koko prosentteina]
        valid_size ([float]): [Validointisetin koko prosentteina testisetin koosta.]
        

    Returns:
        [DataFrame]: [6kpl dataframen osia.]
    """

    df.drop_duplicates(inplace=True)
    df.reset_index(drop=True)
    
    # piirteet
    X = df.drop('value_MenovesiLaskAs', axis=1)
    X.head()

    # target
    y = df.value_MenovesiLaskAs
    y.head()

    # Jako train & test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size) 
    print("X_train : ", X_train.shape)
    print("X_test : ", X_test.shape)
    print("y_train : ", y_train.shape)
    print("y_test : ", y_test.shape)

    # Jako test & validointi
    X_test, X_val, y_test, y_val = train_test_split(X_test, y_test, test_size=valid_size) 
    print("X_test : ", X_test.shape)
    print("X_val : ", X_val.shape)
    print("y_test : ", y_test.shape)
    print("y_val : ", y_val.shape)
    return [X_train, y_train, X_test, y_test, X_val, y_val], ["X_train", "y_train", "X_test", "y_test", "X_val", "y_val"]
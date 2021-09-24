# Funktio joka poistaa rivit joissa on liian korkea value_difference

def remove_outliers(df):
    print("------------------------------------------------")
    print("Remove outliers")
    print("------------------------------------------------")
    limit_outlier = int(input("Define limit: "))
    print("\nRemoving row(s) where value_difference is equal or higher than ", limit_outlier)
    print("DataFrame's shape before:", df.shape)
    df = df[df['value_difference'] <= limit_outlier]
    print("DataFrame's shape after removing:", df.shape)
    return df
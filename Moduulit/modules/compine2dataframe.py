import sys
# sys.path.append("../modules")
from datacleaner import dataCleaner
import pandas as pd

def compine2dataframe(all_csv):
    """[Yhdistää kaikki siivotut csv-tiedostot yhteen dataframeen. Kaikissa tiedostoissa on samat nimet sarakkeilla, joten ne myös identifioidaan tiedoston nimellä.]

    Args:
        all_csv ([list]): [Sisältää reitit kansiorakenteessa jokaiseen dataframeen yhdistettävään tiedostoon.]

    Returns:
        comp [DataFrame]: [Dataframe, johon on yhdistetty kaikki tiedostot.]
    """
    # Luodaan kaikista datoista siivottu dataframe ja lisätään ne listaan.
    dataframes = []

    for f in all_csv:
        if "uusi_df" not in f:
            df_name= str(f'{f.split("/")[-1:]}').rstrip("]").lstrip("[")
            df_name = df_name.split(".")[-2].lstrip("'")
            print(df_name)
            df = dataCleaner(pd.read_csv(f), False, False, False, False)
            df.rename(columns={col:f"{col}_{''.join(df_name.split('_')[-2:])}" for col in df.columns[1:]}, inplace=True)
            dataframes.append(df)

    # Yhdistetään kaikki dataframet timestampin avulla. merge_ordered yhdistää dataframet siten, että jokainen timestamp kaikista dataframeista otetaan mukaan (Lisää treenidataa!!), 
    # ja täyttää kaikki puuttuvat arvot väleistä viimeisimmän arvon mukaan. 
    comp = dataframes.pop()
    for df in dataframes:
        df.sort_values(by="timestamp")
        comp = pd.merge_ordered(left=comp, right=df, on="timestamp", fill_method="ffill")
    comp = comp.dropna()
    comp = comp.drop_duplicates()
    return comp
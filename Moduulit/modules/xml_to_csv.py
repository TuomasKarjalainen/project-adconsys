from xml.etree.ElementTree import parse
import pandas as pd
import glob

def XML_to_dataframe(path):
    """
    [Muuttaa .xml tiedostot pandas-dataframeksi]

    Args:
        path ([str]): [Reitti kansioon, jossa .xml-tiedostot sijaitsevat]
    Returns:
        [DataFrame]: [Palauttaa .xml tiedostosta muokatun dataframen.]
    """

    root = parse(path).getroot()
    data = []
    for record in root.iter("record"):
        columns = []
        values = []
        for col in record:
            columns.append(col.tag)
            values.append(col.attrib["value"])
        data.append({x:y for x,y in zip(columns, values)})

    return pd.DataFrame(data)

def all_files_to_csv(path, destination):
    """
    [Käy läpi kaikki xml-tiedostot, muuttaa ne .csv-muotoon ja tallentaa destination-kansioon.]

    Args:
        path ([str]): [Reitti kansioon, jossa .xml-tiedostot sijaitsevat]
        destination ([str]): [Reitti kansioon, johon .csv tiedostot halutaan tallentaa]

    """
    all_files = glob.glob(f"{path}/*.xml")
    for f in all_files:
        data = XML_to_dataframe(f)
        df_name= str(f'{f.split("/")[-1:]}').rstrip("]").lstrip("[")
        df_name = df_name.split(".")[-2].lstrip("'")

        data.to_csv(f"{destination}{df_name}.csv", index=False)
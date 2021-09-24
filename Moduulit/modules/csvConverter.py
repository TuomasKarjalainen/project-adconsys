import os
import pandas as pd 
from bs4 import BeautifulSoup as b 
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse

def xmlToCsv(xml_file, csv_name):
    """
    xmlToCsv -function
    
    Converts XML-file to dataframe and csv-file
    
    NOTE: You must install BeautifulSoup and lxml first!
    (!pip install bs4)
    (!pip install lxml)


    Parameters
    ----------
    
    xml_file :
        - The xml-file you want to convert to csv format
        - file must be in quotation marks ("file name here")

        
    csv_name :
        - Define name to csv-file


    
    Returns
    -------
    
    Dataframe and csv-file

    
    """
    
    
    # Avataan XML-tiedosto
    with open(xml_file, "r") as f:
        content = f.read()
    soup = b(content, "lxml")

    # Luodaan lista
    list1 = []

    for values in soup.findAll("record"):

        if values.find("timestamp") is None:
            timestamp = " "
        else:
            timestamp = values.find("timestamp").get("value")

        if values.find("trendFlags") is None:
            trendFlags = " "
        else:
            trendFlags = values.find("trendFlags").get("value")

        if values.find("status") is None:
            status = " "
        else:
            status = values.find("status").get("value")

        if values.find("value") is None:
            value = " "
        else:
            value = values.find("value").get("value")

        # Lisätään arvot listaan
        list1.append(timestamp+','+trendFlags+','+status+','+value)
        # Luodaan dataframe listan sisältämistä elementeistä
        df = pd.DataFrame(list1)

    df = df[0].str.split(',', expand=True)
    # Kolumnit 
    df.columns = ['timestamp', 'trendFlags', 'status', 'value']

    # Luodaan csv-tiedosto
    df.to_csv(csv_name, index = False)

    return df 


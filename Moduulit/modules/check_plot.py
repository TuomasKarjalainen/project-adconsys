import matplotlib.pyplot as plt
import pandas as pd

def check_plot(df):
    """[plots all value columns from dataframe as subplots]

    Args:
        df ([DataFrame]): [Dataframe]

    """
    to_plot = [col for col in df.columns if "value" in col]    
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df = df[df["timestamp"] > "2020-05-18 20:30:00"]
    plt.figure(figsize=(20,40))
    for i in range(len(to_plot)):
        plt.subplot(10, 3, i+1)
        plt.plot(df["timestamp"], df[to_plot[i]])
        plt.title(to_plot[i].split("_")[1])
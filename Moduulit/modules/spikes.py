def remove_lammitysS_spikes(df):
    """[Poistaa dataframesta rivit, jolloin lämmityksen säädössä on selkeä, yli 50% nousu kahden peräkkäisen rivin välillä.]

    Args:
        df ([DataFrame]): [Yhdistetty dataframe.]

    Returns:
        [DataFrame]: [Yhdistetty dataframe, josta poistettu selkeimmät piikit.]
    """
    
    rem = [1]
    while len(rem) > 0:
        df["value_difference_LammitysS"] = df["value_LammitysS"].diff()
        poista = False
        rem = []
        for index, row in enumerate(df.itertuples()):
            if row.value_difference_LammitysS > 50:
                poista = True
            if row.value_difference_LammitysS < -35:
                poista = False
            if poista == True:
                rem.append(index)

        df = df.drop(df.index[rem])
        if len(rem) > 0:
            print(f"Poistettu rivejä: {len(rem)}")
    return df

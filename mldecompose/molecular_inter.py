from os import path
import pandas as pd

class MolecularInteraction:
    def __init__(self, rootfolder, type_na):
        self.type_na = type_na
        self.na_folder = path.join(rootfolder, type_na)
        self.df_file = path.join(self.na_folder, 'ml.decompose.mode1.to.mode8.csv')

    def read_df(self):
        df = pd.read_csv(self.df_file)
        df = df.rename(columns={"Unnamed: 0": 'Mode'})
        df = df.set_index('Mode')
        return df

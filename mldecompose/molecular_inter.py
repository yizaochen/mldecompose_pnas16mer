from os import path
import pandas as pd

class MolecularInteraction:
    
    def __init__(self, rootfolder, type_na):
        self.type_na = type_na
        self.na_folder = path.join(rootfolder, type_na)
        self.df_file = path.join(self.na_folder, 'ml.decompose.mode1.to.mode8.csv')
        self.df = None

    def read_df(self):
        df = pd.read_csv(self.df_file)
        df = df.rename(columns={"Unnamed: 0": 'Mode'})
        df = df.set_index('Mode')
        self.df = df
        return df

    def get_four_inter_contri_by_mode(self, mode_id):
        interaction_list = ['base-stacking', 'backbone', 
                            'ribose', 'base-pairing']
        d_result = dict()
        enm_lambda = self.df.loc[f'Mode {mode_id}']['enm_lambda']
        for interaction in interaction_list:
            lambda_contribution = self.__get_contribution_for_interaction(self.df, mode_id, interaction)                   
            d_result[interaction] = (lambda_contribution/enm_lambda) * 100
        return d_result
        
    def __get_contribution_for_interaction(self, df1, mode_id, interaction):
        interaction_map = {'base-stacking': ['st'],
                           'backbone': ['PP', 'PB'], 
                           'ribose': ['R', 'RB'],
                           'base-pairing': ['bp']}
        lambda_contribution = 0.
        for category in interaction_map[interaction]:
            lambda_contribution += df1.loc[f'Mode {mode_id}'][category]
        return lambda_contribution
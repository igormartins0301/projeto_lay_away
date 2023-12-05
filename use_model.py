import pickle
import pandas as pd


def criar_bases_modelagem(df_model):
    df_model_2 = df_model[['Odd_H', 'Odd_D', 'Odd_A', 'Odd_Over25',
        'Odd_Under2.5', 'Odd_H_Odd_Over25', 'Odd_H_Odd_Under2.5',
        'Odd_D_Odd_Over25', 'Odd_D_Odd_Under2.5', 'Odd_A_Odd_Over25',
        'Odd_A_Odd_Under2.5', 'Diff_HA', 'Diff_HD', 'Diff_DA', 'Diff_OU',
        'Avg_H', 'Max_H', 'Ratio_HA', 'Ratio_HD', 'Ratio_DA', 'Prob_H',
        'Prob_D', 'Prob_A', 'Mandante_Favorito', 'Log_Odd_H']]
    return df_model_2

def prever_probabilidade(caminho_arquivo_pickle, df):
    with open(caminho_arquivo_pickle, 'rb') as arquivo_pickle:
        modelo = pickle.load(arquivo_pickle)

    probabilidade_previsao = modelo.predict_proba(df)

    return probabilidade_previsao

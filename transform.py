import pandas as pd
import numpy as np

def criando_targets(df):
    df['target'] = np.where(df['Result'] == 'H', 1, 0)
    df['target_lay'] = np.where(df['Result'] == "A", 0, 1)
    df_model = df[['Date','Home', 'Away','Odd_H', 'Odd_D', 'Odd_A', 'Odd_Over25', 'Odd_Under2.5', 'target', 'Result', 'target_lay']]
    return df_model


def criar_variaveis(df):
    df_model = df 
    lista_resultado = ['Odd_H', 'Odd_D', 'Odd_A']
    lista_under_e_over = ['Odd_Over25', 'Odd_Under2.5']

    for coluna_resultado in lista_resultado:
        for coluna_under_over in lista_under_e_over:
            nova_coluna_nome = f"{coluna_resultado}_{coluna_under_over}"
            df_model[nova_coluna_nome] = df_model[coluna_resultado] / df_model[coluna_under_over]
    df_model['Diff_HA'] = df_model['Odd_H'] - df_model['Odd_A']
    df_model['Diff_HD'] = df_model['Odd_H'] - df_model['Odd_D']
    df_model['Diff_DA'] = df_model['Odd_D'] - df_model['Odd_A']
    df_model['Diff_OU'] = df_model['Odd_Over25'] - df_model['Odd_Under2.5']
    df_model['Avg_H'] = df_model[['Odd_H', 'Odd_D', 'Odd_A']].mean(axis=1)
    df_model['Max_H'] = df_model[['Odd_H', 'Odd_D', 'Odd_A']].max(axis=1)
    df_model['Ratio_HA'] = df_model['Odd_H'] / df_model['Odd_A']
    df_model['Ratio_HD'] = df_model['Odd_H'] / df_model['Odd_D']
    df_model['Ratio_DA'] = df_model['Odd_D'] / df_model['Odd_A']
    df_model['Prob_H'] = 1 / df_model['Odd_H']
    df_model['Prob_D'] = 1 / df_model['Odd_D']
    df_model['Prob_A'] = 1 / df_model['Odd_A']
    df_model['Mandante_Favorito'] = df_model[['Odd_H', 'Odd_D', 'Odd_A']].idxmin(axis=1) == 'Odd_H'
    df_model['Log_Odd_H'] = -1 * df_model['Odd_H'].apply(lambda x: 0 if x == 0 else (1 / x))
    return df_model
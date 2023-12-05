import pandas as pd 

def gerar_resultados(y_probas, df_transformado):
    df_result = pd.DataFrame()
    df_result['Home'] = df_transformado['Home']
    df_result['Away'] = df_transformado['Away']
    df_result['Odd_A'] = df_transformado['Odd_A']
    #df_result['result'] = df_base['Result']
    df_result['y_proba'] = y_probas[:, 1]
    df_result['prob_casa_de_aposta'] = 1 - df_transformado['Prob_A']
    #df_result['real'] = df_transformado['target_lay']
    df_result['odd_calculada'] = 1/(1 - df_result['y_proba'])
    df_result['diff_odds'] = df_result['Odd_A'] - df_result['odd_calculada']
    return df_result

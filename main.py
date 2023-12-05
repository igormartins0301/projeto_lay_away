#%%
import pandas as pd 
from transform import criando_targets, criar_variaveis
from use_model import prever_probabilidade, criar_bases_modelagem
from generate_results import gerar_resultados
import pickle
import warnings
warnings.filterwarnings("ignore")
from datetime import datetime



df_base = pd.read_excel(r'C:\Users\Igor\Desktop\DS\Projetos Portfolios\quant\trading esportivo\data\validacao.xlsx')

df_base = df_base.loc[df_base['Date'] == '2023-12-04']

df_transformado = criando_targets(df=df_base)
df_transformado = criar_variaveis(df=df_transformado)
df_modelo = criar_bases_modelagem(df_model=df_transformado)
caminho_pickle = r'C:\Users\Igor\Desktop\DS\Projetos Portfolios\quant\trading esportivo\seu_modelo.pkl'
y_probas = prever_probabilidade(caminho_arquivo_pickle=caminho_pickle
                    , df=df_modelo)
resultado = gerar_resultados(y_probas, df_transformado)

print('Nesse modelo estamos calculando a probabilidade do visitante vencer')
print('Procurar jogos que: a Odd_A seja alta, porém menor que a odd_calculada')
print('e alem disso um y_proba > 0.7')
resultado.loc[(resultado['diff_odds'] < 0) & (resultado['y_proba'] > 0.7)]


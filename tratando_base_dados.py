# Script para tratar uma base de dados em 8 passos
import pandas as pd

# Passo 01 - Importar a base de dados
tabela = pd.read_excel("EFETIVO.xlsx")

# Passo 02 - Padronizar as colunas ----- ou str.upper()
tabela.columns = tabela.columns.str.strip().str.upper()

# Passo 03 - Remover duplicadas (PY considera o que esta igual em todas as colunas)
# Para remover de uma coluna específica use: tabela.drop_duplicates(subset="COLUNA")

tabela = tabela.drop_duplicates()

# Passo 04 - Remover colunas vazias --- axis=0 (Remove linhas vazias)
tabela = tabela.dropna(axis=1, how="all")

# Passo 05 - Tratar os tipod de dados
# Garantir que a coluna de data esteja no formato yyyy-mm-dd
# errors = coerce força a coluna a preencher o valor vazio

#tabela['DATA'] = pd.to_datetime(tabela['DATA'],errors='coerce')

# Passo 06 - Tratar linhas com valores vazios

# Passo 07 - Exclua colunas desnecessárias
#tabela = tabela.drop(columns=['DIA_SEMANA','STATUS','EXTRA'])


# Passo 08 - Crie Colunas Auxiliares

# Passo 09 - Se necessário tabela.to_excel()
tabela = tabela



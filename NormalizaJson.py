import pandas as pd
import re

def normalize_json(input_json):
    # Remove quebra de linha e espaços extras
    input_json = re.sub(r'\s+', ' ', input_json)
    
    # Substituir aspas duplas duplicadas por aspas simples
    input_json = re.sub(r'""', r'"', input_json)
    
    # Normalizar aspas dentro do jsonData
    input_json = re.sub(r':\s*"{', ': {', input_json)
    input_json = re.sub(r'}"', '}', input_json)
    input_json = re.sub(r'\\\"', '\"', input_json)

    return input_json

# Ler arquivo Excel
df = pd.read_excel('dados1.xlsx')

# Aplicar normalização à coluna "details"
df['details'] = df['details'].apply(normalize_json)

# Salvar resultado em um novo arquivo Excel
df.to_excel('output_file.xlsx', index=False)

print("JSONs normalizados e salvos em 'output_file.xlsx'")
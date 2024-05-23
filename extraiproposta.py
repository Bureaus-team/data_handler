import pandas as pd
import re

def extract_proposta(details):
    match = re.search(r'"proposta": (\d+)', details)
    if match:
        return int(match.group(1))
    return None

def process_excel(input_file, output_file):
    # Carrega o arquivo Excel
    df = pd.read_excel(input_file)

    # Cria uma nova coluna 'proposta' extraindo os números da coluna 'details'
    df['proposta'] = df['details'].apply(extract_proposta)

    # Salva o DataFrame modificado em um novo arquivo Excel
    df.to_excel(output_file, index=False)

# Caminhos para o arquivo de entrada e saída
input_file = 'input.xlsx'
output_file = 'output.xlsx'

# Executa a função
process_excel(input_file, output_file)

import pandas as pd

def remove_single_quotes_with_space(file_path, output_path):
    # Carrega o arquivo Excel
    df = pd.read_excel(file_path)

    # Verifica se a coluna 'details' existe no DataFrame
    if 'details' in df.columns:
        # Remove as aspas simples seguidas de espaço (' ') da coluna 'details'
        df['details'] = df['details'].str.replace("' '", '', regex=False)

    # Salva o DataFrame modificado em um novo arquivo Excel
    df.to_excel(output_path, index=False)

# Exemplo de uso
input_file = 'output_file.xlsx'  # Substitua pelo caminho do arquivo Excel de entrada
output_file = 'output.xlsx'  # Substitua pelo caminho do arquivo Excel de saída

remove_single_quotes_with_space(input_file, output_file)

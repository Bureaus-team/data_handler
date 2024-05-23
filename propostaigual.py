import pandas as pd

def process_and_save_excel(file_path):
    # Carrega o arquivo Excel
    df = pd.read_excel(file_path)
    
    # Verifica se há alguma discrepância entre as colunas 'proposta' e 'proposta2'
    discrepancies = df[df['proposta']!= df['proposta2']]
    
    # Procura por valores que são iguais nas duas colunas e coloca-os lado a lado
    equal_values = discrepancies[discrepancies.apply(lambda row: row['proposta'] == row['proposta2'], axis=1)]
    
    # Cria um novo DataFrame com os valores iguais lado a lado
    new_df = pd.DataFrame(columns=['Details', 'Date', 'Proposta', 'Proposta2'])
    for _, row in equal_values.iterrows():
        new_row = {'Details': row['details'], 'Date': row['date'], 'Proposta': row['proposta'], 'Proposta2': row['proposta2']}
        new_df = new_df.append(new_row, ignore_index=True)
    
    # Salva o novo DataFrame em um novo arquivo Excel
    new_file_path = f"{file_path}_modified.xlsx"
    new_df.to_excel(new_file_path, index=False)
    
    print(f"Arquivo salvo como {new_file_path}")

# Substitua 'caminho_do_seu_arquivo.xlsx' pelo caminho real do seu arquivo Excel
process_and_save_excel('output3.xlsx')

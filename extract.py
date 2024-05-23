import pandas as pd
import re

def ocultar_senha(senha):
    return '*' * len(senha)

def remove_senha(json_data):
    print(json_data)
    # Expressão regular para encontrar "senha": "valor"
    pattern = r'(\"senha\"\s*:\s*\".*?\")'
    # Substitui por "senha": "*********" sem alterar outras partes do JSON
    return re.sub(pattern, lambda match: '"senha": "' + ocultar_senha(match.group(0).split(':')[1].strip('"')) + '"', json_data)

def processar_planilha(caminho_entrada, caminho_saida):
    # Carrega a planilha
    df = pd.read_excel(caminho_entrada)
    
    # Coluna que contém os dados JSON
    coluna = 'details'
    
    # Aplica a função remove_senha em cada célula da coluna
    df[coluna] = df[coluna].apply(remove_senha)
    
    # Salva a planilha processada
    df.to_excel(caminho_saida, index=False)

# Caminho para o arquivo de entrada e saída
caminho_entrada = r'C:\Users\J.Henrique\Desktop\teste\entrada\dados.xlsx'
caminho_saida = r'C:\Users\J.Henrique\Desktop\teste\saida\dados1.xlsx'

# Processa a planilha
processar_planilha(caminho_entrada, caminho_saida)
